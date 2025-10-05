import os,re,sys
import pickle
import argparse
import pandas as pd
from typing import List
import numpy as np
from Bio import SeqIO
import random
import features
import torch
import torch.nn as nn
from torch_scatter import scatter_mean
import torch_cluster
from torch_geometric.nn import TransformerConv
from torch_geometric.data import Data
from torch_geometric.data.batch import Batch
from einops import rearrange
from torch import einsum
from models.GET.modules.tools import BlockEmbedding
import time
from torch.utils.data import DataLoader
from src.pdb_utils import Protein, Atom, VOCAB, Residue


torch.set_num_threads(8)
torch.manual_seed(0)
torch.set_default_dtype(torch.float32)
import warnings
warnings.filterwarnings("ignore")
# if torch.cuda.is_available():
#    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
#    device = torch.device('cuda')
# else:
#    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
#    device = torch.device('cpu')
# 设备设置：默认CPU，可根据外部环境切换；模型缓存会记录设备
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
device = torch.device('cpu')

# 全局缓存
_MODEL_CACHE = {}
_PROTEASE_NAMES_CACHE = {}

def _emit(status_callback, msg):
    if status_callback:
        try:
            status_callback(msg)
        except Exception:
            pass

def get_model_and_names(mode: str, status_callback=None):
    """返回(模型, proteaseNames)；按模式与设备缓存，避免重复加载权重。"""
    key = (mode, device.type)
    if key in _MODEL_CACHE and key in _PROTEASE_NAMES_CACHE:
        return _MODEL_CACHE[key], _PROTEASE_NAMES_CACHE[key]
    t0 = time.perf_counter()
    if mode == 'Human-protease':
        model = LinkModel(256, 128, 256, 54).to(device)
        model.load_state_dict(torch.load('Gui_data/link_prediction_model_human.pth',
                                         map_location=torch.device('cpu')), strict=False)
        proteaseNames = list(np.load("Gui_data/proteaseNames_human54.npy"))
    else:
        model = LinkModel(256, 128, 256, 103).to(device)
        model.load_state_dict(torch.load('Gui_data/link_prediction_model_103_proteases.pth',
                                         map_location=torch.device('cpu')), strict=False)
        proteaseNames = list(np.load("Gui_data/proteaseNames103.npy"))
    model.eval()
    _MODEL_CACHE[key] = model
    _PROTEASE_NAMES_CACHE[key] = proteaseNames
    _emit(status_callback, f"Model loaded in {int((time.perf_counter()-t0))} s (cached)")
    return model, proteaseNames


def residue_to_pd_rows(chain: str, residue: Residue):
    rows = []
    res_id, insertion_code = residue.get_id()
    resname = residue.real_abrv if hasattr(residue, 'real_abrv') else VOCAB.symbol_to_abrv(residue.get_symbol())
    for atom_name in residue.get_atom_names():
        atom = residue.get_atom(atom_name)
        if atom.element == 'H':  # skip hydrogen
            continue
        rows.append((
            chain, insertion_code, res_id, resname,
            atom.coordinate[0], atom.coordinate[1], atom.coordinate[2],
            atom.element, atom.name
        ))
    return rows

class Block:
    def __init__(self, symbol: str, units: List[Atom]) -> None:
        self.symbol = symbol
        self.units = units

    def __len__(self):
        return len(self.units)
    
    def __iter__(self):
        return iter(self.units)

    def to_data(self):
        b = VOCAB.symbol_to_idx(self.symbol)
        x, a, positions = [], [], []
        for atom in self.units:
            a.append(VOCAB.atom_to_idx(atom.get_element()))
            x.append(atom.get_coord())
            positions.append(VOCAB.atom_pos_to_idx(atom.get_pos_code()))
        block_len = len(self)
        return b, a, x, positions, block_len
        
def blocks_to_data(blocks,inx):    
    B, A, X, atom_positions, block_lengths, segment_ids = [], [], [], [], [], []
  
    cur_B = []
    cur_A = []
    cur_X = []
    cur_atom_positions = []
    cur_block_lengths = []
    # other nodes
    for block in blocks:
        b, a, x, positions, block_len = block.to_data() 
        cur_B.append(b)
        cur_A.extend(a)
        cur_X.extend(x)
        cur_atom_positions.extend(positions)
        cur_block_lengths.append(block_len)
    
    # finish these blocks
    B.extend(cur_B)
    A.extend(cur_A)
    X.extend(cur_X)
    atom_positions.extend(cur_atom_positions)
    block_lengths.extend(cur_block_lengths)
    # segment_ids.extend(cur_segment_ids)

    subgraph_data = {
        f'X_{inx}': np.array(X),   # [Natom, 2, 3] 
        f'B_{inx}': B,             # [Nb], block (residue) type
        f'A_{inx}': A,             # [Natom]
        f'atom_positions_{inx}': atom_positions,  # [Natom]
        f'block_lengths_{inx}': block_lengths,  # [Nresidue]

    }


    

    return subgraph_data

def df_to_blocks(df, key_residue='residue', key_insertion_code='insertion_code', key_resname='resname',
                     key_atom_name='atom_name', key_element='element', key_x='x', key_y='y', key_z='z') -> List[Block]:
    last_res_id, last_res_symbol = None, None
    blocks, units = [], []
    for row in df.itertuples():  # each row is an atom (unit)
        residue = getattr(row, key_residue)
        if key_insertion_code is None:
            res_id = str(residue)
        else:
            insert_code = getattr(row, key_insertion_code)
            res_id = f'{residue}{insert_code}'.rstrip()
        if res_id != last_res_id:  # one block ended

            block = Block(last_res_symbol, units)
            blocks.append(block)
            # clear
            units = []
            last_res_id = res_id
            last_res_symbol = VOCAB.abrv_to_symbol(getattr(row, key_resname))
        atom = getattr(row, key_atom_name)
        element = getattr(row, key_element)
        if element == 'H':
            continue
        units.append(Atom(atom, [getattr(row, axis) for axis in [key_x, key_y, key_z]], element))
    blocks = blocks[1:]
    blocks.append(Block(last_res_symbol, units))
    return blocks

def _normalize(tensor, dim=-1):
    '''
    Normalizes a `torch.Tensor` along dimension `dim` without `nan`s.
    '''
    return torch.nan_to_num(
        torch.div(tensor, torch.norm(tensor, dim=dim, keepdim=True)))

def _rbf(D, D_min=0., D_max=20., D_count=16, device='cpu'):
    '''
    From https://github.com/jingraham/neurips19-graph-protein-design
    
    Returns an RBF embedding of `torch.Tensor` `D` along a new axis=-1.
    That is, shape [...dims],if `D` has  then the returned tensor will have
    shape [...dims, D_count].
    '''
    D_mu = torch.linspace(D_min, D_max, D_count) #, device=device
    D_mu = D_mu.view([1, -1])
    D_sigma = (D_max - D_min) / D_count
    D_expand = torch.unsqueeze(D, -1)

    RBF = torch.exp(-((D_expand - D_mu) / D_sigma) ** 2)
    return RBF

def radiusEdge(X_ca,r,mnn):
    return torch_cluster.radius_graph(X_ca, r=r,max_num_neighbors=mnn)

def knnEdge(X_ca,top_k):
    return torch_cluster.knn_graph(X_ca, k=top_k) 
  

def read_inputfiles(mode,inputfile,args,inputType=None,chain='A',dataType='train'):#

    if mode=='train':
        data={}
        tmp_fasta_file=args.outputpath+'/'+str(dataType)+'.fasta'
        f=open(tmp_fasta_file,'w')
        with open(inputfile) as r1:
            lines = r1.readlines()

        for line in lines:
            if '\t' in line:
                lineList=line.strip().split('\t')
            elif ',' in line:
                lineList=line.strip().split(',')
            else:
                lineList=line.strip().split()
            id_=lineList[1] # pdbid
            if id_ in []:
                continue
            label=int(lineList[-1])
            protease=lineList[0] 
            pos=int(lineList[2]) 
            chainType=lineList[3] 

            pdbpath=args.pdb_path+'/'+str(id_)+'.pdb' 
            if not os.path.exists(pdbpath):
                print(f'File not found:{pdbpath}')
                sys.exit(1)
            try:
                chainSeq = {str(record.id).split(':')[-1]: str(record.seq) for record in SeqIO.parse(pdbpath, 'pdb-atom')}
            except:
                print(f'Error in reading pdb file! Please check {str(id_)}.pdb ')
                sys.exit(1)
            # pdbid, ext = os.path.splitext(filename)
            if chainType not in list(chainSeq): 
                print(f'Error chaintype:{line}')
                continue
            seq=chainSeq[chainType]
            seq=re.sub('[^ACDEFGHIKLMNPQRSTVWYX]', 'X', ''.join(seq).upper())
            name=str(protease)+'|'+str(id_)+'|'+str(pos)
            # data[name] = (pos,label,seq)
            data[name] = (pos,seq)
            f.write('>'+name+' '+str(label)+'\n')
            f.write(str(seq)+'\n')
        f.close()
        return tmp_fasta_file,data
    elif mode=='predict':
        data={}
        tmp_fasta_file=args.outputpath+'/'+'predict.fasta'
        f=open(tmp_fasta_file,'w')
        pdbpath=inputfile # pdb file path
        # 获取pdb name
        pdb_name = os.path.basename(pdbpath).replace('.pdb', '')
        if not os.path.exists(pdbpath):
            print(f'File not found:{pdbpath}')
            sys.exit(1)
        try:
            chainSeq = {str(record.id).split(':')[-1]: str(record.seq) for record in SeqIO.parse(pdbpath, 'pdb-atom')}
        except:
            print(f'Error in reading pdb file! Please check {str(id_)}.pdb ')
            sys.exit(1)
        # pdbid, ext = os.path.splitext(filename)
        if chain not in list(chainSeq): 
            print(f'Error chaintype')
            sys.exit(1)
        seq=chainSeq[chain]
        seq=re.sub('[^ACDEFGHIKLMNPQRSTVWYX]', 'X', ''.join(seq).upper())
        
        poss=args.poss.strip().split(',')
        if len(poss)>20:
            sys.exit(f'Please enter the number of positions less than 50.')
        for pos in poss:
            if int(pos) < 4 or int(pos) > len(seq)-3:
                sys.exit(f'Error position:{pos}. Please enter a position between 4-{len(seq)-3}.')
            name=str(pdb_name)+'|'+str(pos)
            data[name] = (pos,seq)
            f.write('>'+name+' '+'0'+'\n')
            f.write(str(seq)+'\n')
        f.close()
        return tmp_fasta_file,data
    elif mode=='predict_for_all_pos':
        
        data={}
        pdbpath=inputfile # pdb file path
        # 获取pdb name
        pdb_name = os.path.basename(pdbpath).replace('.pdb', '')
        # tmp_fasta_file=args.outputpath+'/'+f'{pdb_name}_predict.fasta'
        tmp_fasta_file=args.outputpath+'/'+'predict.fasta'
        

        if not os.path.exists(pdbpath):
            print(f'File not found:{pdbpath}')
            sys.exit(1)
        try:
            chainSeq = {str(record.id).split(':')[-1]: str(record.seq) for record in SeqIO.parse(pdbpath, 'pdb-atom')}
        except:
            print(f'Error in reading pdb file! Please check {str(id_)}.pdb ')
            sys.exit(1)
        # pdbid, ext = os.path.splitext(filename)
        if chain not in list(chainSeq): 
            print(f'Error chaintype')
            sys.exit(1)
        seq=chainSeq[chain]
        seq=re.sub('[^ACDEFGHIKLMNPQRSTVWYX]', 'X', ''.join(seq).upper())
        
        f=open(tmp_fasta_file,'w')
        for pos in range(4,len(seq)-3):
            name=str(pdb_name)+'|'+str(pos)
            data[name] = (pos,seq)
            # f.write('>'+name+'\n')
            f.write('>'+name+' '+'0'+'\n')
            f.write(str(seq)+'\n')
        f.close()
        return tmp_fasta_file,data
    
def construct_edges(edge_constructor, B, batch_id, segment_ids, X, block_id, complexity=-1):
    if complexity == -1:  # don't do splicing
        intra_edges,  global_global_edges, global_normal_edges, _ = edge_constructor(B, batch_id, segment_ids, X=X, block_id=block_id)
        return intra_edges,  global_global_edges, global_normal_edges

def get_edges(xyz,top_k,num_rbf,device):
    # edges = knnEdge(xyz, top_k)
    edges = radiusEdge(xyz, 8,10)
    E_vectors = xyz[edges [0]] - xyz[edges [1]]
    rbf = _rbf(E_vectors.norm(dim=-1), D_count=num_rbf, device=device)
    edge_v = _normalize(E_vectors)
    edge_attr=torch.cat([rbf,edge_v],dim=-1)
    return edges, edge_attr 

def get_data(blocks1,subgraph_energy_features,prottrans_pos_sub,dssp_pos_sub,ppi_x,ppi_edge_index,protease_index,X_ca_sub,top_k,num_rbf,device):
    data={}
    for i ,tuple_data in enumerate([(blocks1,subgraph_energy_features,prottrans_pos_sub,dssp_pos_sub)]):
        blocks,energy_fea,prottrans_fea,dssp_fea =tuple_data
        subgraph_data=blocks_to_data(blocks,i)
        subgraph_data[f'B_prottrans_fea_{i}']=prottrans_fea
        subgraph_data[f'B_dssp_fea_{i}']=dssp_fea
        subgraph_data[f'energy_fea_{i}']=energy_fea
        for k,v in subgraph_data.items():
            data[k]=v
    data['X_top_0']=X_ca_sub
    data['protease_index']=protease_index
    data['ppi_x']=ppi_x
    data['ppi_edge_index']=ppi_edge_index
    edge_index_atom,edge_attr_atom=get_edges(torch.tensor(subgraph_data['X_0'],dtype=torch.float32),top_k,num_rbf,device)
    data['edge_index_atom']=edge_index_atom
    data['edge_attr_atom']=edge_attr_atom
    edge_index_residue,edge_attr_residue=get_edges(X_ca_sub,top_k,num_rbf,device)
    data['edge_index_residue']=edge_index_residue
    data['edge_attr_residue']=edge_attr_residue
    return data

def extract_subsequence_with_padding(sequence, n, window=4):

    # 转换 n 为 0 基索引
    n_idx = n - 1
    
    # 上游序列包括第 n 个氨基酸，所以上游窗口是 n_idx 到 n_idx - window + 1
    start = max(0, n_idx - window + 1)
    # 下游窗口是从 n_idx + 1 开始，直到 n_idx + window
    end = min(len(sequence), n_idx + window + 1)
    
    # 提取上下游子序列
    subsequence = sequence[start:end]
    
    # 上游氨基酸数（包括第 n 个氨基酸本身）
    upstream_count = n_idx - start + 1
    # 下游氨基酸数
    downstream_count = end - (n_idx + 1)
    
    # 补齐上游不足部分（在左边补齐）
    if upstream_count < window:
        padding_left = 'X' * (window - upstream_count)
        subsequence = padding_left + subsequence

    # 补齐下游不足部分（在右边补齐）
    if downstream_count < window:
        padding_right = 'X' * (window - downstream_count)
        subsequence = subsequence + padding_right
    
    return subsequence

class BlockGeoAffDataset(torch.utils.data.Dataset):

    def __init__(self, dataset, args,chain='A',device='cpu',database=None, graph_type='knn',top_k=3,num_rbf=16,num_positional_embeddings=16,dist_th=6, n_cpu=2, suffix=''):

        super().__init__()

        self.dataset = dataset
        self.IDs = list(self.dataset.keys())
        
        # # random.shuffle(self.IDs)
        self.posDict={}
          
        for kk,vv in self.dataset.items():
            self.posDict[kk]=vv[0]
                
        # 定义20种常见氨基酸及其对应的索引
        self.amino_acid_to_idx = {
            'A': 0,  'R': 1,  'N': 2,  'D': 3,  'C': 4,
            'E': 5,  'Q': 6,  'G': 7,  'H': 8,  'I': 9,
            'L': 10, 'K': 11, 'M': 12, 'F': 13, 'P': 14,
            'S': 15, 'T': 16, 'W': 17, 'Y': 18, 'V': 19,'X':20
        }
        # 定义氨基酸类别的索引
        self.amino_acid_to_idx_chemi = {
            'C': 0, 'M': 0,  # 硫含量 sulfur-containing
            'A': 1, 'G': 1, 'P': 1,  # 脂肪族1  aliphatic 1
            'I': 2, 'L': 2, 'V': 2,  # 脂肪族2  aliphatic 2
            'D': 3, 'E': 3,  # 酸性  acidic
            'H': 4, 'K': 4, 'R': 4,  # 碱性  basic
            'F': 5, 'W': 5, 'Y': 5,  # 芳香族 aromatic
            'N': 6, 'Q': 6,  # 酰胺类 amide
            'S': 7, 'T': 7,  # 小羟基 small hydroxy
            'X':8
        }

        self.top_k=top_k
        self.graph_type=graph_type
        self.num_rbf = num_rbf
        self.num_positional_embeddings = num_positional_embeddings
        self.outputpath=args.outputpath
        self.dataset_path = args.dataset_path
        self.feature_path = args.feature_path

        self.pdb_path=args.pdb_path
        self.output_prottrans = args.output_prottrans
        self.output_esmfold = args.output_esmfold
        self.output_dssp = args.output_dssp
        self.output_residue = args.output_dssp
        self.chain=chain
        self.device=device
        # self.dist_th = dist_th
        self.letter_to_num = {'C': 4, 'D': 3, 'S': 15, 'Q': 5, 'K': 11, 'I': 9,
                       'P': 14, 'T': 16, 'F': 13, 'A': 0, 'G': 7, 'H': 8,
                       'E': 6, 'L': 10, 'R': 1, 'W': 17, 'V': 19, 
                       'N': 2, 'Y': 18, 'M': 12}
        if args.mode=='Human-protease':
            self.ppi_x=torch.tensor(np.load("Gui_data/proteases_features_esm150_dssp_energy_human54.npy"),dtype=torch.float32)
            self.ppi_edge_index=torch.LongTensor(np.load('Gui_data/protease_ppi_edge_index_human54.npy'))
            self.proteaseUids=list(np.load('Gui_data/proteaseUids_human54.npy'))
        else:
            self.ppi_x=torch.tensor(np.load("Gui_data/proteases_peptidase_unit_features_esm150_dssp_energy103.npy"),dtype=torch.float32)
            self.ppi_edge_index=torch.LongTensor(np.load('Gui_data/protease_ppi_edge_index.npy'))
            self.proteaseUids=list(np.load('Gui_data/proteaseUids103.npy'))
      
    def _subgraph_sampler(self,X_ca,pos,posL=None,d=10):
        subgraph_node_index=[]
        for i in range(len(X_ca)):

            dist=torch.dist(X_ca[int(pos)-1], X_ca[i])
            if dist<=d: 
                subgraph_node_index.append(i+1) 
        return subgraph_node_index

    def _preprocess(self, item_idx):
        name=self.IDs[item_idx] 

        # Uid=name.split('|')[0] 
        Uid='|'.join(name.split('|')[:-1])
        
        protease_index=[0]
       
        pdb_file = os.path.join(self.pdb_path, Uid + '.pdb')
        
        prot_ = Protein.from_pdb(pdb_file)
        item={}
        item['id']=name
        item['substrate_protein'] = prot_.get_chain(self.chain).get_seq()
        item['chains_protein'] = self.chain

        data_temp = []
        chain_obj = prot_.get_chain(self.chain)
        for residue in chain_obj:
            data_temp.extend(residue_to_pd_rows(self.chain, residue))
        columns = ['chain', 'insertion_code', 'residue', 'resname', 'x', 'y', 'z', 'element', 'name']                    
        item['atoms_protein'] = pd.DataFrame(data_temp, columns=columns)

        
        pos=self.posDict[name]
        
        with torch.no_grad():

            if not os.path.exists(self.feature_path + Uid + ".npy"):
                features11.get_esmfea(self.dataset, self.feature_path,Uid) 
            if not os.path.exists(self.dataset_path + Uid + "_coord.npy"):
                features11.get_coord(self.dataset, self.output_esmfold, self.pdb_path,self.chain)
            if not os.path.exists(self.dataset_path + Uid + "_dssp.npy"):
                features11.get_dsspfea(self.dataset, self.pdb_path, self.output_dssp,self.chain)
            if not os.path.exists(self.feature_path + Uid + "_energy.npy"):
                features11.get_energyfea(self.pdb_path,self.output_prottrans,Uid)
            coords_all = torch.tensor(np.load(self.dataset_path + Uid + "_coord.npy"),dtype=torch.float32)
            prottrans_feat_all = torch.tensor(np.load(self.feature_path + Uid + ".npy"),dtype=torch.float32) 
            # energy features
            energy_feat_all = torch.tensor(np.load(self.feature_path + Uid + "_energy.npy"),dtype=torch.float32) 
            
            dssp_all = torch.tensor(np.load(self.dataset_path + Uid + "_dssp.npy"),dtype=torch.float32)
            X_ca_all = coords_all[:, 1] 

            pos_subgraph=self._subgraph_sampler(X_ca_all,pos,posL=None,d=10)

            subset_pos = item['atoms_protein'][item['atoms_protein']['residue'].isin(pos_subgraph)]

            pos_subgraph=[inx-1 for inx in pos_subgraph]
            X_ca_sub=X_ca_all[pos_subgraph]
            prottrans_pos_sub=prottrans_feat_all[pos_subgraph]
            dssp_pos_sub=dssp_all[pos_subgraph]
            subgraph_energy_features=energy_feat_all[pos_subgraph] 
            
            blocks1 = df_to_blocks(subset_pos, key_atom_name='name')    

            data = get_data(blocks1,subgraph_energy_features,prottrans_pos_sub,dssp_pos_sub,self.ppi_x,self.ppi_edge_index,protease_index,X_ca_sub,self.top_k,self.num_rbf,device)
            # Chemical seq indices
            seq_win=extract_subsequence_with_padding(self.dataset[name][1], int(self.dataset[name][0]))
            indices_chemi = [self.amino_acid_to_idx_chemi[aa] for aa in seq_win]
            # aa tupe indices
            indices_aatype = [self.amino_acid_to_idx[aa] for aa in seq_win]

            data['indices_tensor_chemi']=indices_chemi
            data['indices_tensor_aatype']=indices_aatype
            data['label'] = 0 # for prediction
            data['name']=name
        return data
    
    def __len__(self):
        return len(self.IDs)
    
    def __getitem__(self, idx):
        '''
        an example of the returned data
        {
            'X': [Natom, n_channel, 3],
            'B': [Nblock],
            'A': [Natom],
            'atom_positions': [Natom],
            'block_lengths': [Natom]
            'segment_ids': [Nblock]
            'label': [1]
        }
        '''
        item = self._preprocess(idx)
        return item

    @classmethod
    def collate_fn(cls, batch):
        keys = ['X_0', 'B_0', 'A_0', 'atom_positions_0', 'block_lengths_0','B_prottrans_fea_0','B_dssp_fea_0','protease_index']
        types = [torch.float32, torch.long, torch.long, torch.long, torch.long,torch.float32,torch.float32, torch.long]
        res = {}
        for key, _type in zip(keys, types):
            val = []
            for item in batch:
                val.append(torch.tensor(item[key], dtype=_type))
            res[key] = torch.cat(val, dim=0)
        val1 = []
        for item in batch:
            val1.append(item['X_top_0'].to(torch.float32))
        res['X_top_0'] = torch.cat(val1, dim=0)    

        res['label'] = torch.tensor([item['label'] for item in batch], dtype=torch.float32)
        lengths_0 = [len(item['B_0']) for item in batch] 
        res['lengths_0'] = torch.tensor(lengths_0, dtype=torch.long)
        res['X_0'] = res['X_0'].unsqueeze(-2)
        res['X_top_0']=res['X_top_0'].unsqueeze(-2)
        res['name']=[item['name'] for item in batch]

        res['indices_tensor_chemi'] = torch.tensor([item['indices_tensor_chemi'] for item in batch], dtype=torch.long)
        res['indices_tensor_aatype'] = torch.tensor([item['indices_tensor_aatype'] for item in batch], dtype=torch.long)
        data_list_residue=[]
        data_list_atom=[]
        for item in batch:

            edge_index_atom=item['edge_index_atom']
            edge_attr_atom=item['edge_attr_atom']
            edge_index_residue=item['edge_index_residue']
            edge_attr_residue=item['edge_attr_residue']
            node_x_residue=torch.cat([item['B_prottrans_fea_0'],item['B_dssp_fea_0'],item['energy_fea_0']],dim=-1)
            
            data_list_atom.append(Data(edge_index=edge_index_atom,edge_attr=edge_attr_atom))
            data_list_residue.append(Data(x=node_x_residue,edge_index=edge_index_residue,edge_attr=edge_attr_residue))
        AtomGraphData= Batch.from_data_list(data_list_atom)
        ResidueGraphData= Batch.from_data_list(data_list_residue)
        res['AtomGraphData']=AtomGraphData
        res['ResidueGraphData']=ResidueGraphData
        res['PPI_X']=batch[0]['ppi_x']
        res['PPI_edge_index']=batch[0]['ppi_edge_index']
        return res

class PretrainModel(nn.Module):

    def __init__(self, model_type, hidden_size, n_channel,
                 n_rbf=16, cutoff=7.0, n_head=2,
                 radial_size=16, edge_size=19, k_neighbors=3, n_layers=2,
                 sigma_begin=10, sigma_end=0.01, n_noise_level=50,
                 dropout=0.2, std=10, global_message_passing=True, hierarchical=True, no_block_embedding=False,device='cuda') -> None:
        super().__init__()
        self.device=device
        self.model_type = model_type
        self.hidden_size = hidden_size
        self.n_channel = n_channel
        self.n_rbf = n_rbf
        self.cutoff = cutoff
        self.n_head = n_head
        self.radial_size = radial_size
        self.edge_size = edge_size
        self.k_neighbors = k_neighbors
        self.n_layers = n_layers
        self.dropout = dropout
        self.std = std
        self.global_message_passing = global_message_passing
        self.hierarchical = hierarchical
        self.no_block_embedding = no_block_embedding
        self.global_block_id = VOCAB.symbol_to_idx(VOCAB.GLB)
        self.block_embedding = BlockEmbedding(
            num_block_type=len(VOCAB),
            num_atom_type=VOCAB.get_num_atom_type(),
            num_atom_position=VOCAB.get_num_atom_pos(),
            embed_size=hidden_size,
            no_block_embedding=no_block_embedding
        )
        self.block_embedding = nn.Embedding(20, hidden_size) 
        self.position_embedding = nn.Embedding(VOCAB.get_num_atom_pos(), hidden_size)
        self.atom_embedding = nn.Embedding(VOCAB.get_num_atom_type(), hidden_size)
        
        z_requires_grad = False
        if model_type == 'GET':
            from models.GET.encoder import GETEncoder
            self.encoder = GETEncoder(
                hidden_size, radial_size, n_channel,
                n_rbf, cutoff, edge_size, n_layers,
                n_head, dropout=dropout,
                z_requires_grad=z_requires_grad
            )
        else:
            raise NotImplementedError(f'Model type {model_type} not implemented!')
        
        if self.hierarchical:
            self.top_encoder = GETEncoder(
                hidden_size*2, radial_size, n_channel,
                n_rbf, cutoff, edge_size, n_layers,
                n_head, dropout=dropout,
                z_requires_grad=z_requires_grad
            )
            
        self.prottran_dssp_ffn = nn.Sequential(
            nn.Linear(1306, hidden_size*2), 
            nn.SiLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size*2, hidden_size),
            nn.Dropout(dropout)
        )
  

            
        # TODO: add zero noise level
        sigmas = torch.tensor(np.exp(np.linspace(np.log(sigma_begin), np.log(sigma_end), n_noise_level)), dtype=torch.float)
        self.sigmas = nn.Parameter(sigmas, requires_grad=False)  # [n_noise_level]
        
    def weights_init(self, m):
        if isinstance(m, nn.Linear):
            # torch.nn.init.xavier_uniform_(m.weight.data)
            torch.nn.init.kaiming_normal_(m.weight.data)
            if m.bias is not None:
                m.bias.data.fill_(0.0)
    @torch.no_grad()
    def _normalize(self,tensor, dim=-1):
        '''
        Normalizes a `torch.Tensor` along dimension `dim` without `nan`s.
        '''
        return torch.nan_to_num(
        torch.div(tensor, torch.norm(tensor, dim=dim, keepdim=True)))
   

    def forward(self, Z, Z_top, B, A, atom_positions, block_lengths, lengths,AtomGraph,ResidueGraph):
        
        # batch_id and block_id
        with torch.no_grad():
            batch_id=ResidueGraph.batch            
            block_id = torch.zeros_like(A) # [Nu]
            block_id[torch.cumsum(block_lengths, dim=0)[:-1]] = 1
            block_id.cumsum_(dim=0)  # [Nu], block (residue) id of each unit (atom)
                          
            if self.hierarchical:
                bottom_batch_id =AtomGraph.batch
                bottom_block_id = torch.arange(0, len(block_id), device=block_id.device)  #[Nu]
            batch_size = lengths.shape[0]
            Z = self._normalize(Z)
            Z_top = self._normalize(Z_top)
        Z.requires_grad_(True)
        Z_top.requires_grad_(True)
        # embedding
        if self.hierarchical:  
            bottom_H_0 = self.atom_embedding(A) + self.position_embedding(atom_positions) 
        else:
            H_0 = self.block_embedding(B)
        # encoding
        if self.hierarchical:
            prottrans_dssp_fea_0=self.prottran_dssp_ffn(ResidueGraph.x)
            edges_atom,edge_attr_atom = AtomGraph.edge_index,AtomGraph.edge_attr
            unit_repr, _, atomGraphRepr, pred_Z = self.encoder(bottom_H_0, Z, bottom_block_id, bottom_batch_id, edges_atom, edge_attr_atom)            
            top_block_id = torch.arange(0, len(batch_id), device=batch_id.device)

            # top level message passing
            edges_residue,edge_attr_residue = ResidueGraph.edge_index,ResidueGraph.edge_attr
            top_H_0 =torch.cat((prottrans_dssp_fea_0,scatter_mean(unit_repr, block_id, dim=0)), dim=1)
            _, block_repr, graph_repr,_ = self.top_encoder(top_H_0, Z_top, top_block_id, batch_id, edges_residue, edge_attr_residue)

        else:
            top_block_id = torch.arange(0, len(batch_id), device=batch_id.device)
            edges, edge_attr =ResidueGraph.edge_index,ResidueGraph.edge_attr
            H_0=torch.cat((ResidueGraph.x,H_0), dim=1)
            unit_repr, block_repr, graph_repr, pred_Z = self.encoder(H_0, Z_top, top_block_id, batch_id, edges, edge_attr)
        return block_repr,graph_repr,atomGraphRepr

class CrossAttention(nn.Module):
    def __init__(self, query_dim, context_dim=None, heads=8, dim_head=64, dropout=0.0,protease_num=54):
        super().__init__()
        inner_dim = dim_head * heads
        context_dim = context_dim if context_dim is not None else query_dim

        self.scale = dim_head**-0.5
        self.heads = heads

        self.to_q = nn.Linear(query_dim, inner_dim, bias=False)
        self.to_k = nn.Linear(context_dim, inner_dim, bias=False)
        self.to_v = nn.Linear(context_dim, inner_dim, bias=False)

        self.to_out = nn.Sequential(
            nn.Linear(protease_num, protease_num), nn.Dropout(dropout)
        )

    def forward(self, x, context=None, mask=None):
        h = self.heads
        q = self.to_q(x) 
        context = context if context is not None else x
        k = self.to_k(context)  
        v = self.to_v(x)  
        q, k, v = map(lambda t: rearrange(t, "b n (h d) -> (b h) n d", h=h), (q, k, v))
        sim = einsum("b i d, b j d -> b i j", q, k) * self.scale
        attn = sim.softmax(dim=-1)
        out = einsum("b i j, b j d -> b i j", attn, v)
        out = rearrange(out, "(b h) n d -> b n (h d)", h=h)

        return self.to_out(out).squeeze(1)

class LinkModel(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels,proteases_num):
        super(LinkModel, self).__init__()
        self.conv1 = TransformerConv(in_channels, hidden_channels)
        self.conv2 = TransformerConv(hidden_channels, out_channels)
        self.AAType_embedding = nn.Embedding(21, 3)
        self.Chemical_embedding = nn.Embedding(9, 3)
        
        self.graphencoder=PretrainModel('GET', 128, 1,n_layers=1)
        self.protease_x_ffn = nn.Sequential(
            nn.Linear(666, 256*2),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256*2, 256),
            nn.Dropout(0.2)
        )
        self.fc=nn.Sequential(
            nn.Linear(out_channels*3+128+24*2+proteases_num, 128),#
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(128, 1)
        )
        self.cross_attention = CrossAttention(query_dim=256, context_dim=256, heads=1, dim_head=256,protease_num=proteases_num)
        self.dropout=nn.Dropout(0.2)
        for m in self.modules():
            self.weights_init(m)
            
    def weights_init(self, m):
        if isinstance(m, nn.Linear):
            torch.nn.init.xavier_uniform_(m.weight.data)
            # torch.nn.init.kaiming_normal_(m.weight.data)
            if m.bias is not None:
                m.bias.data.fill_(0.0)
                
    def encode(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        return self.conv2(x, edge_index)

    def decode(self, z, edge_label_index,graph_repr,atom_graph_repr,indices_tensor_chemi,indices_tensor_aatype,ppi_x):

        Em=z[edge_label_index[0]] # 0
        Ed=z[edge_label_index[1]] # 54/103
        aa_chemical_embedding=self.Chemical_embedding(indices_tensor_chemi)
        aa_chemical_embedding=aa_chemical_embedding.view(indices_tensor_chemi.size(0), -1)
        
        aa_type_embedding=self.AAType_embedding(indices_tensor_aatype)
        aa_type_embedding=aa_type_embedding.view(indices_tensor_aatype.size(0), -1)

        Ed_ = Ed.unsqueeze(1) 
        ppi_x = ppi_x.unsqueeze(0).expand(Ed.size(0), -1, -1)  
        protease_substrate_attn = self.cross_attention(Ed_, context=ppi_x).view(-1,ppi_x.size(1)) 
        x = torch.cat((Em, Ed,graph_repr,atom_graph_repr,aa_chemical_embedding,aa_type_embedding,protease_substrate_attn),dim=1) 
        x=self.dropout(x)
        return self.fc(x)

    def decode_all(self, Z, Z_top,B, A, atom_positions, block_lengths, lengths,AtomGraph,ResidueGraph,ppi_x,ppi_edge_index,protease_site_index,indices_tensor_chemi,indices_tensor_aatype,proteases_str,proteaseNames):
        block_repr,graph_repr,atom_graph_repr=self.graphencoder(
            Z=Z, Z_top=Z_top,B=B, A=A,
            atom_positions=atom_positions,
            block_lengths=block_lengths,
            lengths=lengths,
            AtomGraph=AtomGraph,
            ResidueGraph=ResidueGraph,
            )
        ppi_x=self.protease_x_ffn(ppi_x)
        combined_x = torch.cat([ppi_x,graph_repr], dim=0)
        
        site_block_index=torch.arange(0, lengths.size(0), device=device)+ppi_x.size(0)
        site_block_index=site_block_index.unsqueeze(1).repeat(1, ppi_x.size(0)).view(-1)
        all_protease_index=torch.arange(0, ppi_x.size(0), device=device).repeat(lengths.size(0))
        protease_site_edges=torch.vstack([all_protease_index,site_block_index])
        # protease_site_edges
        # 0,1,2,
        # 103,103,103
        combined_edge_index = torch.cat([ppi_edge_index,protease_site_edges], dim=1)
        z = self.encode(combined_x, combined_edge_index) 
        out_all=[]
        # proteasesL=proteases_str
        proteasesL_index=[list(proteaseNames).index(item) for item in proteases_str]
        # for ii in range(protease_site_edges.size(1)): 
        for ii in proteasesL_index: 
            out = self.decode(z, protease_site_edges[:,ii:ii+1],graph_repr,atom_graph_repr,indices_tensor_chemi,indices_tensor_aatype,ppi_x).view(-1)
            out_all.append(out)
        return torch.cat(out_all, dim=0)
    def forward(self, Z, Z_top,B, A, atom_positions, block_lengths, lengths,AtomGraph,ResidueGraph,ppi_x,ppi_edge_index,protease_site_index,indices_tensor_chemi,indices_tensor_aatype):
        block_repr,graph_repr,atom_graph_repr=self.graphencoder(
            Z=Z, Z_top=Z_top,B=B, A=A,
            atom_positions=atom_positions,
            block_lengths=block_lengths,
            lengths=lengths,
            AtomGraph=AtomGraph,
            ResidueGraph=ResidueGraph,
            )

        ppi_x=self.protease_x_ffn(ppi_x) 
        combined_x = torch.cat([ppi_x,graph_repr], dim=0)
        site_block_index=torch.arange(0, lengths.size(0), device=device)+ppi_x.size(0)
        protease_site_edges=torch.vstack([protease_site_index,site_block_index])
        combined_edge_index = torch.cat([ppi_edge_index,protease_site_edges], dim=1)
        z = self.encode(combined_x, combined_edge_index) 
        out = self.decode(z, protease_site_edges,graph_repr,atom_graph_repr,indices_tensor_chemi,indices_tensor_aatype,ppi_x).view(-1)
        
        return out
def Cleavage_site_prediction(outputpath,chain,mode,inputpath,pdb_path,inputType,proteases_str,num_workers,poss, status_callback=None):
    
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    args.chain=chain
    args.mode=mode
    args.outputpath=outputpath
    args.inputpath=inputpath
    args.pdb_path=pdb_path
    args.inputType=inputType
    args.poss=poss
    args.proteases_str=proteases_str
    
    args.dataset_path=args.outputpath+'/proteases_structure_data/'
    args.feature_path=args.outputpath+'/proteases_prottrans/'
    args.output_prottrans=args.outputpath+'/proteases_prottrans/'
    args.output_esmfold=args.outputpath+'/proteases_structure_data/'
    args.output_dssp=args.outputpath+'/proteases_structure_data/'
    os.makedirs(args.output_prottrans, exist_ok=True)
    os.makedirs(args.dataset_path, exist_ok=True)
    os.makedirs(args.feature_path, exist_ok=True)
    _emit(status_callback, "Prepare inputs...")
    if poss =='':
        print("poss",poss)
        pre_fasta_file,predict_data=read_inputfiles('predict_for_all_pos',args.inputpath,args,args.inputType,dataType='predict')
    else:
        pre_fasta_file,predict_data=read_inputfiles('predict',args.inputpath,args,args.inputType,dataType='predict')    
    proteases_str=args.proteases_str.split(',')
    # 加载/复用模型
    t0_model = time.perf_counter()
    model, proteaseNames = get_model_and_names(args.mode, status_callback)
    protease_num = len(proteases_str)
    _emit(status_callback, f"Model ready in {int((time.perf_counter()-t0_model))} s")

    # # protease_num=103
    # protease_num=len(proteases_str)
    testdataset=BlockGeoAffDataset(predict_data, args)

    collate_fn = testdataset.collate_fn
    test_loader = DataLoader(testdataset, batch_size=1,
                            num_workers=num_workers,
                            shuffle=False,
                            sampler=None,persistent_workers=True,
                            collate_fn=collate_fn)

    model.eval()
    all_predictions=[]
    all_targets=[]
    names=[]
    proteaseNs=[]
    pre_labels=[]
    # accum_iter = 10
    with torch.no_grad():  
        for i,batchData in enumerate(test_loader):
            t_iter = time.perf_counter()
            Z=batchData['X_0'].to(device) 
            Z_top=batchData['X_top_0'].to(device)
            B=batchData['B_0'].to(device) 
            A=batchData['A_0'].to(device)
            atom_positions=batchData['atom_positions_0'].to(device)
            block_lengths=batchData['block_lengths_0'].to(device) 
            lengths=batchData['lengths_0'].to(device)

            ppi_x=batchData['PPI_X'].to(device)
            ppi_edge_index=batchData['PPI_edge_index'].to(device)
            protease_index=batchData['protease_index'].to(device)
            label=batchData['label'].to(device)
            AtomGraph=batchData['AtomGraphData'].to(device)
            ResidueGraph=batchData['ResidueGraphData'].to(device)

            names_tmp=[item for item in batchData['name'] for _ in range(protease_num)]
            names.extend(names_tmp)
            # proteaseNames_tmp=proteaseNames*len(batchData['name'])
            proteaseNames_tmp=args.proteases_str.split(',')*len(batchData['name'])
            proteaseNs.extend(proteaseNames_tmp)
            
            indices_tensor_chemi=batchData['indices_tensor_chemi'].to(device)
            indices_tensor_aatype=batchData['indices_tensor_aatype'].to(device)
            # 推理
            out = model.decode_all(Z, Z_top,B, A, atom_positions, block_lengths, lengths,AtomGraph,ResidueGraph,ppi_x,ppi_edge_index,protease_index,indices_tensor_chemi,indices_tensor_aatype,proteases_str,proteaseNames)

            out_sig= torch.sigmoid(out).cpu().detach().numpy().tolist()   
            all_predictions.extend(out_sig) 
            targets_tmp=[item1 for item1 in label.cpu().detach().numpy().tolist() for _ in range(protease_num)]
            all_targets.extend(targets_tmp)
            pre_label_tmp=[1 if value >= 0.5 else 0 for value in out_sig]
            pre_labels.extend(pre_label_tmp)
            _emit(status_callback, f"Position {i+1} / {len(test_loader)}: infer position {i+1} scores in {int((time.perf_counter()-t_iter))} s")
    res=pd.DataFrame()
    # print('proteaseNs',len(proteaseNs),proteaseNs)
    # print('names',len(names),names)
    res['Proteases']=proteaseNs
    res['Protein|position']=names
    res['Pre_Score']=all_predictions
    res['Pre_label']=pre_labels
    res.to_csv(args.outputpath+f'/result.csv')
    return res

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--chain', type=str, default='A',help='A or B')
    parser.add_argument('--mode', type=str, default='Human-protease',help='Human-protease or Multi-protease')
    parser.add_argument('--outputpath', type=str,default='./Results', help='The path of output.') 
    parser.add_argument('--inputpath', type=str, default='./data/example.pdb',help='The path of the input file(.pdb).')
    parser.add_argument('--pdb_path', type=str, default='./data',help='The path of the pdb files.')
    parser.add_argument('--inputType', type=str, default='pdb',help='pdb')
    parser.add_argument('--poss', type=str, default='4,5,6,7',help='The position to be predicted should satisfy 4=< pos <= len(sequence).len(sequence) indicates the length of the protein sequence.')
    parser.add_argument('--proteases_str', type=str, default='C14.003,M10.002',help='The position to be predicted should satisfy 4=< pos <= len(sequence).len(sequence) indicates the length of the protein sequence.')
    parser.add_argument('--num_workers', type=int, default=2,help='Set number of parallel processing worker threads')
    args = parser.parse_args()
    
    args.dataset_path=args.outputpath+'/proteases_structure_data/'
    args.feature_path=args.outputpath+'/proteases_prottrans/'
    args.output_prottrans=args.outputpath+'/proteases_prottrans/'
    args.output_esmfold=args.outputpath+'/proteases_structure_data/'
    args.output_dssp=args.outputpath+'/proteases_structure_data/'
    os.makedirs(args.output_prottrans, exist_ok=True)
    os.makedirs(args.dataset_path, exist_ok=True)
    os.makedirs(args.feature_path, exist_ok=True)
    if args.poss =='':
        print("poss",args.poss)
        pre_fasta_file,predict_data=read_inputfiles('predict_for_all_pos',args.inputpath,args,args.inputType,dataType='predict')
    else:
        pre_fasta_file,predict_data=read_inputfiles('predict',args.inputpath,args,args.inputType,dataType='predict')    
    # pre_fasta_file,predict_data=read_inputfiles('predict',args.inputpath,args,args.inputType,dataType='predict')    
    proteases_str=args.proteases_str.split(',')
    # 加载参数
    if args.mode=='Human-protease':
        # 初始化模型
        model=LinkModel(256, 128, 256,54).to(device)
        model.load_state_dict(torch.load('Gui_data/link_prediction_model_v25_speci_human_epoch_1_83.pth',
                                         map_location=torch.device('cpu')),strict=False)#,map_location=torch.device('cpu')
        proteaseNames=list(np.load("Gui_data/proteaseNames_human54.npy"))
        # protease_num=54
        protease_num=len(proteases_str)
    elif args.mode=='Multi-protease':
        # 初始化模型
        model=LinkModel(256, 128, 256,103).to(device)
        model.load_state_dict(torch.load('Gui_data/link_prediction_model_v26_103_proteases_2_epoch_299.pth',
                                         map_location=torch.device('cpu')),strict=False)
        proteaseNames=list(np.load("Gui_data/proteaseNames103.npy"))

        # protease_num=103
        protease_num=len(proteases_str)
    testdataset=BlockGeoAffDataset(predict_data, args)

    collate_fn = testdataset.collate_fn
    test_loader = DataLoader(testdataset, batch_size=1,
                            num_workers=args.num_workers,
                            shuffle=False,
                            sampler=None,
                            collate_fn=collate_fn)

    model.eval()
    all_predictions=[]
    all_targets=[]
    names=[]
    proteaseNs=[]
    pre_labels=[]
    # accum_iter = 10
    with torch.no_grad():  
        for i,batchData in enumerate(test_loader):
            Z=batchData['X_0'].to(device) 
            Z_top=batchData['X_top_0'].to(device)
            B=batchData['B_0'].to(device) 
            A=batchData['A_0'].to(device)
            atom_positions=batchData['atom_positions_0'].to(device)
            block_lengths=batchData['block_lengths_0'].to(device) 
            lengths=batchData['lengths_0'].to(device)

            ppi_x=batchData['PPI_X'].to(device)
            ppi_edge_index=batchData['PPI_edge_index'].to(device)
            protease_index=batchData['protease_index'].to(device)
            label=batchData['label'].to(device)
            AtomGraph=batchData['AtomGraphData'].to(device)
            ResidueGraph=batchData['ResidueGraphData'].to(device)

            names_tmp=[item for item in batchData['name'] for _ in range(protease_num)]
            names.extend(names_tmp)
            # proteaseNames_tmp=proteaseNames*len(batchData['name'])
            proteaseNames_tmp=args.proteases_str.split(',')*len(batchData['name'])
            proteaseNs.extend(proteaseNames_tmp)
            
            indices_tensor_chemi=batchData['indices_tensor_chemi'].to(device)
            indices_tensor_aatype=batchData['indices_tensor_aatype'].to(device)
            out = model.decode_all(Z, Z_top,B, A, atom_positions, block_lengths, lengths,AtomGraph,ResidueGraph,ppi_x,ppi_edge_index,protease_index,indices_tensor_chemi,indices_tensor_aatype,proteases_str,proteaseNames)

            out_sig= torch.sigmoid(out).cpu().detach().numpy().tolist()   
            all_predictions.extend(out_sig) 
            targets_tmp=[item1 for item1 in label.cpu().detach().numpy().tolist() for _ in range(protease_num)]
            all_targets.extend(targets_tmp)
            pre_label_tmp=[1 if value >= 0.5 else 0 for value in out_sig]
            pre_labels.extend(pre_label_tmp)    

    res=pd.DataFrame()
    # print('proteaseNs',len(proteaseNs),proteaseNs)
    # print('names',len(names),names)
    res['Proteases']=proteaseNs
    res['Protein|position']=names
    res['Pre_Score']=all_predictions
    res['Pre_label']=pre_labels
    res.to_csv(args.outputpath+f'/result.csv')
    

if __name__ == '__main__':
    main()
