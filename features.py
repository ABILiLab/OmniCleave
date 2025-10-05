import torch
from transformers import T5EncoderModel, T5Tokenizer
import re, argparse
import numpy as np
from tqdm import tqdm
import gc
import multiprocessing
import os, datetime
from Bio import pairwise2
import pickle
import math
import pandas as pd
from typing import Any, Dict, Optional
from Bio.Data.IUPACData import protein_letters_1to3
from Bio import PDB
import esm
from Bio.SeqIO import parse
from Bio.PDB import NACCESS
import pyrosetta as pr
from pyrosetta import *
from pyrosetta.rosetta.core.scoring import *

pr.init("-out:level 0")
# os.environ["CUDA_VISIBLE_DEVICES"] = "1"
AA_indx = {'A': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'K': 9, 'L': 10, 'M': 11, 'N': 12,
                   'P': 13, 'Q': 14, 'R': 15, 'S': 16, 'T': 17, 'V': 18, 'W': 19, 'Y': 20, '-': 0,'X': 0}
one_letter={'VAL': 'V','ILE': 'I','LEU': 'L','GLU': 'E','GLN': 'Q','ASP': 'D','ASN': 'N','HIS': 'H','TRP': 'W',\
    'PHE': 'F','TYR': 'Y','ARG': 'R','LYS': 'K','SER': 'S','THR': 'T','MET': 'M','ALA': 'A','GLY': 'G','PRO': 'P','CYS': 'C'}

def get_pdb_xyz(pdb_file,ref_seq,chain):
    with open(pdb_file) as r2:
        pdb_file_lines = r2.readlines()
    current_pos = -1000
    X = []
    # X1 =[]
    current_aa = {} # 'N', 'CA', 'C', 'O'
    # cuurent_aa1={}
    try:
        for line in pdb_file_lines:
            if 'ENDMDL' in line:
                break
            # if (line[0:4].strip() == "ATOM" and line[21].strip() =='B') or (line[0:4].strip() == "ATOM" and line[21].strip() =='C'): # 排除其它链
            #     break
            if (line[0:4].strip() == "ATOM" and int(line[22:26].strip()) != current_pos and line[21].strip() ==chain) or line[0:4].strip() == "TER":
                if current_aa != {}:
                    X.append([current_aa["N"], current_aa["CA"], current_aa["C"], current_aa["O"]])
                    # X1.append([current_aa1["N"], current_aa1["CA"], current_aa1["C"], current_aa1["O"]])
                    current_aa = {}
                    # current_aa1 = {}
                if line[0:4].strip() != "TER":
                    current_pos = int(line[22:26].strip())

            if line[0:4].strip() == "ATOM" and line[21].strip() ==chain:
                atom = line[13:16].strip()
                if atom in ['N', 'CA', 'C', 'O']:
                    xyz = np.array([line[30:38].strip(), line[38:46].strip(), line[46:54].strip()]).astype(np.float32)
                    current_aa[atom] = xyz
                    # aatype=np.arrat([AA_indx[one_letter[str(line[17:20].strip())]]]).astype(np.float32)
                    # cuurent_aa1[atom] = aatype
    except:
        return None

    if len(X) == len(ref_seq):          
        return np.array(X)#,np.array(X1)
    else:
        return None    


def get_coord(dataset,output_path,pdb_path,chain):
    print('pdb_path',pdb_path)
    for key in dataset.keys():
        # Uid=key.split('|')[0] #P02511|4
        Uid='|'.join(str(key).split('|')[:-1])
        # print('get_coord_feature_for_train',Uid,key)
        if not os.path.exists(output_path  + Uid + '_coord.npy'):
            coord = get_pdb_xyz(str(pdb_path) + '/' + Uid + '.pdb',dataset[key][1],chain) 
            np.save(output_path  + Uid + '_coord.npy', coord)

def get_dsspfea(dataset, pdb_path, dssp_path,chain):
    # script_path = os.path.abspath(__file__)
    # script_dir = os.path.dirname(script_path)
    # DSSP = os.path.join(script_dir, 'dssp')
    DSSP = './dssp'
    # DSSP='/home/xudongguo/Projects/Guo/ProcleaveHub_new/ProcleaveContrastive/ProcleaveHub_GUI/GUI/dssp'
    def process_dssp(dssp_file,chain):
        aa_type = "ACDEFGHIKLMNPQRSTVWY"
        SS_type = "HBEGITSC"
        rASA_std = [115, 135, 150, 190, 210, 75, 195, 175, 200, 170,
                    185, 160, 145, 180, 225, 115, 140, 155, 255, 230]

        with open(dssp_file, "r") as f:
            lines = f.readlines()

        seq = ""
        dssp_feature = []

        p = 0
        while lines[p].strip()[0] != "#":
            p += 1
        for i in range(p + 1, len(lines)):
            if lines[i][11]==chain:
                aa = lines[i][13]
                if aa == "!" or aa == "*":
                    continue
                seq += aa
                SS = lines[i][16]
                if SS == " ":
                    SS = "C"
                SS_vec = np.zeros(9) # The last dim represents "Unknown" for missing residues
                SS_vec[SS_type.find(SS)] = 1
                PHI = float(lines[i][103:109].strip())
                PSI = float(lines[i][109:115].strip())
                ACC = float(lines[i][34:38].strip())
                ASA = min(100, round(ACC / rASA_std[aa_type.find(aa)] * 100)) / 100
                dssp_feature.append(np.concatenate((np.array([PHI, PSI, ASA]), SS_vec)))

        return seq, dssp_feature 

    def match_dssp(seq, dssp, ref_seq):
        alignments = pairwise2.align.globalxx(ref_seq, seq)
        ref_seq = alignments[0].seqA
        seq = alignments[0].seqB

        SS_vec = np.zeros(9) # The last dim represent "Unknown" for missing residues
        SS_vec[-1] = 1
        padded_item = np.concatenate((np.array([360, 360, 0]), SS_vec))

        new_dssp = []
        for aa in seq: # dssp seq
            if aa == "-":
                new_dssp.append(padded_item)
            else:
                new_dssp.append(dssp.pop(0)) 

        matched_dssp = []
        for i in range(len(ref_seq)):
            if ref_seq[i] == "-": 
                continue
            matched_dssp.append(new_dssp[i])

        return matched_dssp

    def transform_dssp(dssp_feature):
        dssp_feature = np.array(dssp_feature)
        angle = dssp_feature[:,0:2]
        ASA_SS = dssp_feature[:,2:]

        radian = angle * (np.pi / 180)
        dssp_feature = np.concatenate([np.sin(radian), np.cos(radian), ASA_SS], axis = 1)

        return dssp_feature


    def get_dssp(data_path,dssp_path, ID, ref_seq,chain):
        Uid='|'.join(str(ID).split('|')[:-1]) 
        
        try:
            if not os.path.exists(dssp_path + Uid + ".dssp"):
                # print(Uid,ID)
                os.system("{} -i {} -o {}.dssp".format(DSSP, data_path + '/' + Uid + '.pdb', dssp_path + Uid))

            dssp_seq, dssp_matrix = process_dssp(dssp_path + Uid + ".dssp",chain)
            # dssp_seq, dssp_matrix = process_dssp(dssp_path + ID + ".dssp")
            # print(dssp_seq,ref_seq)
            if dssp_seq != ref_seq: 
                dssp_matrix = match_dssp(dssp_seq, dssp_matrix, ref_seq)
            np.save(dssp_path + Uid + "_dssp.npy", transform_dssp(dssp_matrix))
            # os.system('rm {}.dssp'.format(dssp_path + ID))
            return 0
        except Exception as e:
            print(ID,Uid)
            return None       
            
    # name=list(pdbfasta.keys())[0]
    # sign = get_dssp2(pdb_path,dssp_path, name ,pdbfasta[name],chain)      
      
    fault_name = []
    for name in dataset.keys():
        # uid=name.split('|')[0]
        uid='|'.join(str(name).split('|')[:-1])
        # sign = get_dssp(pdb_path,dssp_path, name ,pdbfasta[name])
        if not os.path.exists(dssp_path + uid + "_dssp.npy"):
            sign = get_dssp(str(pdb_path),dssp_path, name ,dataset[name][1],chain)# 
            if sign == None:
                fault_name.append(uid)
    if fault_name != []:
        np.save(dssp_path+'dssp_fault.npy',fault_name)

def get_esmfea(dataset, output_file,Uid):
    
    # Load ESM-2 model
    model, alphabet = esm.pretrained.esm2_t33_650M_UR50D() #

    batch_converter = alphabet.get_batch_converter()
    # model.to(device).eval()  
    model.eval()   
    
    # for record in parse(fasta_file,'fasta'):
    for kk,vv in dataset.items():
        if not os.path.exists(output_file+Uid+'.npy'):

            seq=str(vv[1])
            protein='|'.join(str(kk).split('|')[:-1]) # P02671|4 0

            data=[(protein,seq)]
            batch_labels, batch_strs, batch_tokens = batch_converter(data)
            batch_lens = (batch_tokens != alphabet.padding_idx).sum(1)
            # Extract per-residue representations (on CPU)
            with torch.no_grad():
                results = model(batch_tokens, repr_layers=[30], return_contacts=True) #.to(device)
            token_representations = results["representations"][30]
            token_representations=token_representations[0, 1 : batch_lens[0]-1].cpu().numpy() 
            np.save(output_file+Uid+'.npy',token_representations)
   
def get_energyfea(pdb_file,output_file,Uid):
    if not os.path.exists(output_file + Uid + "_energy.npy"):
        pdb_file=str(pdb_file)+'/'+Uid+'.pdb'
        sfxn = get_fa_scorefxn()
        # energy_terms=[fa_intra_sol_xover4, rama_prepro, omega, p_aa_pp, fa_dun, ref]#, fa_intra_rep
        energy_terms=[fa_intra_sol_xover4, fa_intra_rep, rama_prepro, omega, p_aa_pp, fa_dun, ref,fa_atr, fa_rep, fa_sol, fa_elec, lk_ball_wtd]
        
        pose = pose_from_pdb(pdb_file)
        sfxn(pose)
        energies = pose.energies()
        energy_item_values=[]
        for ii in range(1,len(pose.sequence())+1):
            templist=[]
            for etm in energy_terms:
                templist.append(energies.residue_total_energies(ii)[etm])
            # print(templist)
            energy_item_values.append(templist)
        energy_feat_all=np.array(energy_item_values)
        np.save(output_file + Uid + "_energy.npy",energy_feat_all)