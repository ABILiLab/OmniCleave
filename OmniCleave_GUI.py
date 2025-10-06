from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        # 允许窗口更小的最小尺寸，便于上下缩放
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_utilres_status = QtWidgets.QVBoxLayout()
        self.verticalLayout_utilres_status.setObjectName("verticalLayout_utilres_status")
        self.horizontalLayout_utils_res = QtWidgets.QHBoxLayout()
        self.horizontalLayout_utils_res.setObjectName("horizontalLayout_utils_res")
        self.verticalLayout_utils = QtWidgets.QVBoxLayout()
        self.verticalLayout_utils.setObjectName("verticalLayout_utils")
        self.groupBox_input = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_input.setObjectName("groupBox_input")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_input)
        self.verticalLayout.setObjectName("verticalLayout")
        # Direct file selection row inside input group (remove Upload File tab)
        self.horizontalLayout_file = QtWidgets.QHBoxLayout()
        self.horizontalLayout_file.setObjectName("horizontalLayout_file")
        self.filename = QtWidgets.QLineEdit(self.groupBox_input)
        self.filename.setObjectName("filename")
        self.horizontalLayout_file.addWidget(self.filename)
        self.pushButton_select_file = QtWidgets.QPushButton(self.groupBox_input)
        self.pushButton_select_file.setObjectName("pushButton_select_file")
        self.horizontalLayout_file.addWidget(self.pushButton_select_file)
        self.verticalLayout.addLayout(self.horizontalLayout_file)
        self.verticalLayout_utils.addWidget(self.groupBox_input)
        # PSI Species 选择分组（置于Proteases之上）
        self.groupBox_psi = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_psi.setObjectName("groupBox_psi")
        self.verticalLayout_psi = QtWidgets.QVBoxLayout(self.groupBox_psi)
        self.verticalLayout_psi.setObjectName("verticalLayout_psi")
        # PSI 内部可折叠主体
        self.widget_psi_body = QtWidgets.QWidget(self.groupBox_psi)
        self.widget_psi_body.setObjectName("widget_psi_body")
        self.verticalLayout_psi_body = QtWidgets.QVBoxLayout(self.widget_psi_body)
        self.verticalLayout_psi_body.setObjectName("verticalLayout_psi_body")
        self.label_psi = QtWidgets.QLabel(self.widget_psi_body)
        self.label_psi.setWordWrap(True)
        self.label_psi.setObjectName("label_psi")
        self.verticalLayout_psi_body.addWidget(self.label_psi)
        # 物种树放入可滚动区域，避免高度不足看不到
        self.scroll_psi = QtWidgets.QScrollArea(self.widget_psi_body)
        self.scroll_psi.setWidgetResizable(True)
        self.scroll_psi.setObjectName("scroll_psi")
        self.scroll_psi_contents = QtWidgets.QWidget()
        self.scroll_psi_contents.setObjectName("scroll_psi_contents")
        self.vlayout_scroll_psi = QtWidgets.QVBoxLayout(self.scroll_psi_contents)
        self.vlayout_scroll_psi.setObjectName("vlayout_scroll_psi")
        self.treeWidget_species = QtWidgets.QTreeWidget(self.scroll_psi_contents)
        self.treeWidget_species.setObjectName("treeWidget_species")
        self.vlayout_scroll_psi.addWidget(self.treeWidget_species)
        self.scroll_psi.setWidget(self.scroll_psi_contents)
        self.verticalLayout_psi_body.addWidget(self.scroll_psi)
        self.verticalLayout_psi.addWidget(self.widget_psi_body)
        # 折叠提示文本（折叠时可见）
        self.label_psi_hint = QtWidgets.QLabel(self.groupBox_psi)
        self.label_psi_hint.setObjectName("label_psi_hint")
        self.label_psi_hint.setWordWrap(True)
        self.verticalLayout_psi.addWidget(self.label_psi_hint)
        self.verticalLayout_utils.addWidget(self.groupBox_psi)

        # Proteases 分组
        self.groupBox_ATCcode = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ATCcode.setObjectName("groupBox_ATCcode")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_ATCcode)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        # Proteases 内部可折叠主体
        self.widget_atc_body = QtWidgets.QWidget(self.groupBox_ATCcode)
        self.widget_atc_body.setObjectName("widget_atc_body")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_atc_body)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_atc_body)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.treeWidget_ATCcode = QtWidgets.QTreeWidget(self.widget_atc_body)
        self.treeWidget_ATCcode.setObjectName("treeWidget_ATCcode")
        
        # 从CSV文件加载MEROPS数据
        self.load_merops_data()

        self.verticalLayout_5.addWidget(self.treeWidget_ATCcode)
        self.verticalLayout_6.addWidget(self.widget_atc_body)
        # 折叠提示文本（折叠时可见）
        self.label_atc_hint = QtWidgets.QLabel(self.groupBox_ATCcode)
        self.label_atc_hint.setObjectName("label_atc_hint")
        self.label_atc_hint.setWordWrap(True)
        self.verticalLayout_6.addWidget(self.label_atc_hint)
        self.verticalLayout_utils.addWidget(self.groupBox_ATCcode)
        
        self.groupBox_parameters = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_parameters.setObjectName("groupBox_parameters")
        # 参数分组内部可折叠主体
        self.verticalLayout_params_group = QtWidgets.QVBoxLayout(self.groupBox_parameters)
        self.verticalLayout_params_group.setObjectName("verticalLayout_params_group")
        self.widget_parameters_body = QtWidgets.QWidget(self.groupBox_parameters)
        self.widget_parameters_body.setObjectName("widget_parameters_body")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_parameters_body)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        
        self.label_5 = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        #（移除旧的 Task/Species 内嵌于 Parameters 的控件）
        
        self.LineEdit_atc_code = QtWidgets.QLineEdit(self.groupBox_parameters)
        self.LineEdit_atc_code.setObjectName("LineEdit_atc_code")
        # self.LineEdit_atc_code.setText("A01.009,A01.010")
        self.LineEdit_atc_code.setPlaceholderText("Click the list above to select proteases, multi-selection supported")
        self.verticalLayout_8.addWidget(self.LineEdit_atc_code)
        
        
        
        self.LineEdit_num_workers = QtWidgets.QLineEdit(self.groupBox_parameters)
        self.LineEdit_num_workers.setObjectName("LineEdit_num_workers")
        self.LineEdit_num_workers.setText("1")
        self.verticalLayout_8.addWidget(self.LineEdit_num_workers)
        
        self.LineEdit_chain = QtWidgets.QLineEdit(self.groupBox_parameters)
        self.LineEdit_chain.setObjectName("LineEdit_chain")
        self.LineEdit_chain.setText("A")
        self.verticalLayout_8.addWidget(self.LineEdit_chain)
        
        self.LineEdit_possr = QtWidgets.QLineEdit(self.groupBox_parameters)
        self.LineEdit_possr.setObjectName("LineEdit_possr")
        # self.LineEdit_possr.setText("4,5,6")
        self.LineEdit_possr.setPlaceholderText("(Starting from 4) e.g.: 4,5,6")
        self.verticalLayout_8.addWidget(self.LineEdit_possr)
        
        
        
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        # 将参数主体加入分组
        self.verticalLayout_params_group.addWidget(self.widget_parameters_body)
        self.verticalLayout_utils.addWidget(self.groupBox_parameters)
        self.groupBox_operator = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_operator.setObjectName("groupBox_operator")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_operator)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.button_predict = QtWidgets.QPushButton(self.groupBox_operator)
        self.button_predict.setObjectName("button_predict")
        self.horizontalLayout_4.addWidget(self.button_predict)

        self.buttonn_save = QtWidgets.QPushButton(self.groupBox_operator)
        self.buttonn_save.setObjectName("buttonn_save")
        self.horizontalLayout_4.addWidget(self.buttonn_save)

        self.buttonn_clean = QtWidgets.QPushButton(self.groupBox_operator)
        self.buttonn_clean.setObjectName("buttonn_clean")
        self.horizontalLayout_4.addWidget(self.buttonn_clean)

        self.button_load_result = QtWidgets.QPushButton(self.groupBox_operator)
        self.button_load_result.setObjectName("button_load_result")
        self.horizontalLayout_4.addWidget(self.button_load_result)


        
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_utils.addWidget(self.groupBox_operator)
        self.verticalLayout_utils.setStretch(0, 2)
        self.verticalLayout_utils.setStretch(1, 6)
        self.verticalLayout_utils.setStretch(2, 1)
        self.verticalLayout_utils.setStretch(3, 1)
        self.horizontalLayout_utils_res.addLayout(self.verticalLayout_utils)
        self.Tab_res = QtWidgets.QTabWidget(self.centralwidget)
        self.Tab_res.setObjectName("Tab_res")
        self.tab_meloculesdata = QtWidgets.QWidget()
        self.tab_meloculesdata.setObjectName("tab_meloculesdata")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.tab_meloculesdata)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.Tab_res.addTab(self.tab_meloculesdata, "")
        
        self.tab_summayplot = QtWidgets.QWidget()
        self.tab_summayplot.setObjectName("tab_summayplot")
        self.Tab_res.addTab(self.tab_summayplot, "")
        self.horizontalLayout_utils_res.addWidget(self.Tab_res)
        self.horizontalLayout_utils_res.setStretch(0, 4)
        self.horizontalLayout_utils_res.setStretch(1, 6)



        self.verticalLayout_utilres_status.addLayout(self.horizontalLayout_utils_res)
        # Status area restored with titled group box
        self.groupBox_status = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_status.setObjectName("groupBox_status")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_status)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textBrowser_status = QtWidgets.QTextBrowser(self.groupBox_status)
        self.textBrowser_status.setObjectName("textBrowser_status")
        try:
            self.groupBox_status.setMaximumHeight(90)
            self.textBrowser_status.setMaximumHeight(30)
        except Exception:
            pass
        self.verticalLayout_9.addWidget(self.textBrowser_status)
        self.verticalLayout_utilres_status.addWidget(self.groupBox_status)
        self.verticalLayout_utilres_status.setStretch(0, 9)
        self.verticalLayout_utilres_status.setStretch(1, 1)
        self.verticalLayout_19.addLayout(self.verticalLayout_utilres_status)
        
        MainWindow.setCentralWidget(self.centralwidget) #设置为中央部件
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1614, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.Tab_res.setCurrentIndex(0)
        self.button_predict.clicked.connect(MainWindow.predict) # type: ignore
        self.buttonn_save.clicked.connect(MainWindow.getSavePath)
        self.buttonn_clean.clicked.connect(MainWindow.clean)
        self.button_load_result.clicked.connect(MainWindow.loadResultFile) # type: ignore
        self.pushButton_select_file.clicked.connect(MainWindow.selectFile) # type: ignore
        self.treeWidget_ATCcode.itemClicked['QTreeWidgetItem*','int'].connect(MainWindow.selectATCcode) # type: ignore
        self.treeWidget_species.itemClicked['QTreeWidgetItem*','int'].connect(MainWindow.selectSpecies) # type: ignore
        
        # 连接实时参数验证
        self.LineEdit_chain.textChanged.connect(MainWindow.validate_chain_input)
        self.LineEdit_possr.textChanged.connect(MainWindow.validate_positions_input)
        self.LineEdit_num_workers.textChanged.connect(MainWindow.validate_num_workers_input)
        #（移除旧的 Task 切换信号）
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def load_merops_data(self):
        """Load MEROPS data from CSV file"""
        try:
            import pandas as pd
            import os
            
            # 获取当前脚本所在目录
            script_dir = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(script_dir, "Gui_data", "MEROPS_identifier_Name.csv")
            
            # 读取CSV文件
            self.merops_data = pd.read_csv(csv_path, header=None, names=['MEROPS_ID', 'Name'])
            
            # 过滤掉标题行（如果存在）
            if self.merops_data.iloc[0, 0] == 'protease':
                self.merops_data = self.merops_data.iloc[1:].reset_index(drop=True)
                
        except Exception as e:
            # print(f"加载MEROPS数据时出错: {e}")
            # 如果加载失败，使用默认数据
            self.merops_data = pd.DataFrame({
                'MEROPS_ID': ['A01.009', 'A01.010'],
                'Name': ['Cathepsin D', 'Cathepsin E']
            })
    
    def setup_merops_tree_items(self):
        """Setup MEROPS tree widget items"""
        _translate = QtCore.QCoreApplication.translate
        
        # 清空现有项目
        self.treeWidget_ATCcode.clear()
        
        # 添加数据行
        for i, row in self.merops_data.iterrows():
            item = QtWidgets.QTreeWidgetItem(self.treeWidget_ATCcode)
            item.setText(0, _translate("MainWindow", str(i + 1)))  # 序号
            item.setText(1, _translate("MainWindow", str(row['MEROPS_ID'])))  # MEROPS ID
            item.setText(2, _translate("MainWindow", str(row['Name'])))  # 名称

    def setup_species_tree_items(self):
        """Setup PSI species list"""
        _translate = QtCore.QCoreApplication.translate
        self.treeWidget_species.clear()
        # 构建物种 -> 蛋白酶列表
        species_map = self.load_species_to_proteases()
        species_list = sorted(list(species_map.keys()))
        for idx, species in enumerate(species_list):
            count = len(species_map.get(species, []))
            item = QtWidgets.QTreeWidgetItem(self.treeWidget_species)
            item.setText(0, _translate("MainWindow", str(idx + 1)))
            item.setText(1, _translate("MainWindow", species))
            item.setText(2, _translate("MainWindow", str(count)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OmniCleave"))
        self.groupBox_input.setTitle(_translate("MainWindow", "Select a protein pdb file"))
        self.pushButton_select_file.setText(_translate("MainWindow", "Select pdb file"))
        
        self.groupBox_ATCcode.setTitle(_translate("MainWindow", "Protease substrate cleavage site prediction"))
        self.groupBox_psi.setTitle(_translate("MainWindow", "Protease-Substrate Interaction (PSI)"))
        self.label_psi.setText(_translate("MainWindow", "Select a species for PSI prediction."))
        self.label_psi_hint.setText(_translate("MainWindow", "Select a species for PSI prediction."))
        self.label_2.setText(_translate("MainWindow", "OmniCleave supports substrate cleavage site identification for 103 proteases."))
        self.label_atc_hint.setText(_translate("MainWindow", "OmniCleave supports substrate cleavage site identification for 103 proteases."))
        self.treeWidget_ATCcode.headerItem().setText(0, _translate("MainWindow", "Rank"))
        self.treeWidget_ATCcode.headerItem().setText(1, _translate("MainWindow", "MEROPS ID"))
        self.treeWidget_ATCcode.headerItem().setText(2, _translate("MainWindow", "Name"))
        self.treeWidget_species.headerItem().setText(0, _translate("MainWindow", "Rank"))
        self.treeWidget_species.headerItem().setText(1, _translate("MainWindow", "Species"))
        self.treeWidget_species.headerItem().setText(2, _translate("MainWindow", "Protease Count"))
        __sortingEnabled = self.treeWidget_ATCcode.isSortingEnabled()
        self.treeWidget_ATCcode.setSortingEnabled(False)
        # 默认折叠两个分组的内部主体（点击标题可展开/折叠）
        try:
            self.widget_psi_body.setVisible(False)
            self.widget_atc_body.setVisible(True)
        except Exception:
            pass
        
        # 动态设置树形控件的内容
        self.setup_merops_tree_items()
        self.setup_species_tree_items()

        self.treeWidget_ATCcode.setSortingEnabled(__sortingEnabled)
        # 为分组盒添加点击联动（手风琴）展开/折叠功能
        try:
            self.groupBox_psi.mousePressEvent = self._toggle_psi_group
            self.groupBox_ATCcode.mousePressEvent = self._toggle_atc_group
            self.groupBox_parameters.mousePressEvent = lambda e: self._toggle_group_body(self.widget_parameters_body)
        except Exception:
            pass
        self.groupBox_parameters.setTitle(_translate("MainWindow", "Paramenters"))
        self.label_4.setText(_translate("MainWindow", "Proteases:"))
        
        self.label_5.setText(_translate("MainWindow", "Num_workers:"))
        self.label_6.setText(_translate("MainWindow", "Chain (A/B/...):"))
        self.label_7.setText(_translate("MainWindow", "Positions:"))
        
        self.groupBox_operator.setTitle(_translate("MainWindow", "Operator"))
        self.button_predict.setText(_translate("MainWindow", "Predict"))
        self.buttonn_save.setText(_translate("MainWindow", "Save results"))
        self.buttonn_clean.setText(_translate("MainWindow", "Clean"))
        self.button_load_result.setText(_translate("MainWindow", "Load result file"))
        # Results group removed; tabs are placed directly
        self.Tab_res.setTabText(self.Tab_res.indexOf(self.tab_meloculesdata), _translate("MainWindow", "Prediction"))
        self.Tab_res.setTabText(self.Tab_res.indexOf(self.tab_summayplot), _translate("MainWindow", "Plot"))
        self.groupBox_status.setTitle(_translate("MainWindow", "Status"))
        
        # 连接tab切换事件
        self.Tab_res.currentChanged.connect(self.on_tab_changed)
    
    def show_tabSon_meloculesdata(self):
        
        self.tabSon_meloculesdata = QtWidgets.QTabWidget(self.tab_meloculesdata)
        self.tabSon_meloculesdata.setObjectName("tabSon_meloculesdata")
        self.tabItem_alldata = QtWidgets.QWidget()
        self.tabItem_alldata.setObjectName("tabItem_alldata")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tabItem_alldata)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.table_alldata = QtWidgets.QTableWidget(self.tabItem_alldata)
        self.table_alldata.setObjectName("table_alldata")
        self.verticalLayout_12.addWidget(self.table_alldata)
        self.tabSon_meloculesdata.addTab(self.tabItem_alldata, "Results")
        # self.tabItem_singlemelocule = QtWidgets.QWidget()
        # self.tabItem_singlemelocule.setObjectName("tabItem_singlemelocule")
        # self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.tabItem_singlemelocule)
        # self.verticalLayout_21.setObjectName("verticalLayout_21")
        # self.label_selectmelocule = QtWidgets.QLabel(self.tabItem_singlemelocule)
        # self.label_selectmelocule.setObjectName("label_selectmelocule")
        # self.verticalLayout_21.addWidget(self.label_selectmelocule)
        # self.label_selectmelocule.setText("Select Melocule by Id")
        # self.comboBox_selectMelocule = QtWidgets.QComboBox(self.tabItem_singlemelocule)
        # self.comboBox_selectMelocule.setObjectName("comboBox_selectMelocule")
        # self.verticalLayout_21.addWidget(self.comboBox_selectMelocule)
        



        # self.scrollArea_single = QtWidgets.QScrollArea(self.tabItem_singlemelocule)
        # self.scrollArea_single.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scrollArea_single.setWidgetResizable(True)
        # self.scrollArea_single.setObjectName("scrollArea_single")
        self.scrollAreaWidgetContents_single = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_single.setGeometry(QtCore.QRect(0, 0, 867, 849))
        self.scrollAreaWidgetContents_single.setObjectName("scrollAreaWidgetContents_single")
        
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_single)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        
        # self.frame_image = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        # self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_image.setObjectName("frame_image")
        # self.horizontalLayout_22 = QtWidgets.QVBoxLayout(self.frame_image)
        # self.horizontalLayout_22.setObjectName("verticalLayout_22")
        # self.label_image = QtWidgets.QLabel(self.frame_image)
        # self.label_image.setObjectName("label_image")
        # self.horizontalLayout_22.addWidget(self.label_image)
        # self.verticalLayout_14.addWidget(self.frame_image)
        

        self.frame_image = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_image.sizePolicy().hasHeightForWidth())
        self.frame_image.setSizePolicy(sizePolicy)
        self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image.setObjectName("frame_image")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_image)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_image_1 = QtWidgets.QLabel(self.frame_image)
        self.label_image_1.setObjectName("label_image_1")
        self.label_image_1.setScaledContents(True)
        self.label_image_1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.horizontalLayout_10.addWidget(self.label_image_1)
        self.label_image_2 = QtWidgets.QLabel(self.frame_image)
        self.label_image_2.setObjectName("label_image_2")
        self.label_image_2.setScaledContents(True)
        self.label_image_2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.horizontalLayout_10.addWidget(self.label_image_2)
        self.horizontalLayout_10.setStretch(0, 5)
        self.horizontalLayout_10.setStretch(1, 5)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_14.addWidget(self.frame_image)



        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_PhyChe = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_PhyChe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_PhyChe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_PhyChe.setObjectName("frame_PhyChe")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_PhyChe)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_phyche = QtWidgets.QLabel(self.frame_PhyChe)
        self.label_phyche.setObjectName("label_phyche")
        self.label_phyche.setText("Physicochemical")
        self.verticalLayout_13.addWidget(self.label_phyche)
        self.table_Phyche = QtWidgets.QTableWidget(self.frame_PhyChe)
        self.table_Phyche.setObjectName("table_Phyche")
        self.verticalLayout_13.addWidget(self.table_Phyche)
        self.horizontalLayout_7.addWidget(self.frame_PhyChe)
        self.frame_absorption = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_absorption.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_absorption.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_absorption.setObjectName("frame_absorption")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_absorption)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_absorption = QtWidgets.QLabel(self.frame_absorption)
        self.label_absorption.setObjectName("label_absorption")
        self.label_absorption.setText("Absorption")
        self.verticalLayout_15.addWidget(self.label_absorption)
        self.table__absorption = QtWidgets.QTableWidget(self.frame_absorption)
        self.table__absorption.setObjectName("table__absorption")
        self.verticalLayout_15.addWidget(self.table__absorption)
        self.horizontalLayout_7.addWidget(self.frame_absorption)
        self.frame_distribution = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_distribution.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_distribution.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_distribution.setObjectName("frame_distribution")
        self.verticalLayout_frame_distribution = QtWidgets.QVBoxLayout(self.frame_distribution)
        self.verticalLayout_frame_distribution.setObjectName("verticalLayout_frame_distribution")
        self.label_distribution = QtWidgets.QLabel(self.frame_distribution)
        self.label_distribution.setObjectName("label_distribution")
        self.verticalLayout_frame_distribution.addWidget(self.label_distribution)
        self.label_distribution.setText("Distribution")
        self.table_distribution = QtWidgets.QTableWidget(self.frame_distribution)
        self.table_distribution.setObjectName("table_distribution")
        self.verticalLayout_frame_distribution.addWidget(self.table_distribution)
        self.horizontalLayout_7.addWidget(self.frame_distribution)
        self.verticalLayout_14.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_metabolism = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_metabolism.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_metabolism.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_metabolism.setObjectName("frame_metabolism")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_metabolism)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_metabolism = QtWidgets.QLabel(self.frame_metabolism)
        self.label_metabolism.setObjectName("label_metabolism")
        self.verticalLayout_16.addWidget(self.label_metabolism)
        self.label_metabolism.setText("Metabolism")
        self.table_metabolism = QtWidgets.QTableWidget(self.frame_metabolism)
        self.table_metabolism.setObjectName("table_metabolism")
        self.verticalLayout_16.addWidget(self.table_metabolism)
        self.horizontalLayout_9.addWidget(self.frame_metabolism)
        self.frame_excretion = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_excretion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_excretion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_excretion.setObjectName("frame_excretion")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_excretion)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_excretion = QtWidgets.QLabel(self.frame_excretion)
        self.label_excretion.setObjectName("label_excretion")
        self.label_excretion.setText("Excretion")
        self.verticalLayout_18.addWidget(self.label_excretion)
        self.table_excretion = QtWidgets.QTableWidget(self.frame_excretion)
        self.table_excretion.setObjectName("table_excretion")
        self.verticalLayout_18.addWidget(self.table_excretion)
        self.horizontalLayout_9.addWidget(self.frame_excretion)
        self.frame_toxicity = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_toxicity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toxicity.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toxicity.setObjectName("frame_toxicity")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_toxicity)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_toxicity = QtWidgets.QLabel(self.frame_toxicity)
        self.label_toxicity.setObjectName("label_toxicity")
        self.verticalLayout_17.addWidget(self.label_toxicity)
        self.label_toxicity.setText("Toxicity")
        self.table_toxicity = QtWidgets.QTableWidget(self.frame_toxicity)
        self.table_toxicity.setObjectName("table_toxicity")
        self.verticalLayout_17.addWidget(self.table_toxicity)
        self.horizontalLayout_9.addWidget(self.frame_toxicity)
        self.verticalLayout_14.addLayout(self.horizontalLayout_9)
        self.verticalLayout_14.setStretch(0, 9)
        self.verticalLayout_14.setStretch(1, 10)
        self.verticalLayout_14.setStretch(2, 10)
        # self.tabSon_meloculesdata.addTab(self.tabItem_singlemelocule, "Single Melocule")
        self.verticalLayout_20.addWidget(self.tabSon_meloculesdata)
        # self.comboBox_selectMelocule.currentTextChanged.connect(self.show_single_melocule)

        self.table_Phyche.resizeColumnsToContents()
        self.table__absorption.resizeColumnsToContents()
        self.table_distribution.resizeColumnsToContents()
        self.table_metabolism.resizeColumnsToContents()
        self.table_excretion.resizeColumnsToContents()
        self.table_toxicity.resizeColumnsToContents()


        # self.scrollArea_single.setWidget(self.scrollAreaWidgetContents_single)
        # self.verticalLayout_21.addWidget(self.scrollArea_single)
        # self.verticalLayout_14.setStretch(0,2)
        # self.verticalLayout_14.setStretch(1,5)
        # self.verticalLayout_14.setStretch(2,5)
        # 降低最小高度，便于整体窗口上下缩放
        self.scrollAreaWidgetContents_single.setMinimumSize(600,1200)

        # 调节scrollArea中的控件大小
        
        # self.frame_image.setGeometry(9,9,100,100)
        # self.frame_PhyChe.setGeometry(1,1,250,448)
        # self.frame_absorption.setGeometry(257,1,250,448)
        # self.frame_distribution.setGeometry(512,1,250,448)
        # self.frame_metabolism.setGeometry(257,1,250,448)
        # self.frame_excretion.setGeometry(1,1,250,448)
        # self.frame_toxicity.setGeometry(512,1,250,448)
        



        
        
        # self.Tab_res.setTabText(self.Tab_res.indexOf(self.tab_meloculesdata), _translate("MainWindow", "Melocules Data"))

from PyQt5.QtWidgets import QTreeWidgetItem, QSizePolicy
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QInputDialog, QTableWidget, QTableWidgetItem, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QTextEdit, QDialog
from PyQt5.QtGui import QPixmap
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# 尝试导入PyQtWebEngine，如果失败则使用备用方案
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    WEBENGINE_AVAILABLE = True
except ImportError:
    WEBENGINE_AVAILABLE = False
    print("警告: PyQtWebEngine未安装，3D可视化将使用外部浏览器")
from pathlib import Path

from OmniCleave import Cleavage_site_prediction
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import pickle
import os
import subprocess
import tempfile
import datetime

from typing import Dict, List, Set
import re
from Bio import SeqIO

def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.deleteLater()
        else:
            clear_layout(item.layout())

class NumericSortProxyModel(QSortFilterProxyModel):
    """Custom sort proxy for numerical column sorting"""
    def lessThan(self, left, right):
        left_data = left.data(QtCore.Qt.UserRole)
        right_data = right.data(QtCore.Qt.UserRole)
        
        # If both data have UserRole (numerical), compare by value
        if left_data is not None and right_data is not None:
            try:
                return float(left_data) < float(right_data)
            except (ValueError, TypeError):
                pass
        
        # Otherwise compare by default string
        return super().lessThan(left, right)
   
class MyDesigner(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textBrowser_status.setText("\nWelcome to the OmniCleave!")
        # 初始化预测状态标志
        self.predicting = False
        # # 启用系统标题栏按钮并取消无边框，确保显示最小化/最大化/关闭
        # try:
        #     self.setWindowFlag(QtCore.Qt.FramelessWindowHint, False)
        #     self.setWindowFlag(QtCore.Qt.WindowTitleHint, True)
        #     self.setWindowFlag(QtCore.Qt.WindowSystemMenuHint, True)
        #     self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        #     self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        #     self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
        #     # 重新应用窗口装饰
        #     self.showNormal()
        # except Exception:
        #     pass
        # #（移除旧的 Task 初始化）

    def selectFile(self):
        filePath,_ = QFileDialog.getOpenFileName(self.filename, "Open Files")
        self.filename.setText(filePath)
        
        # 设置PDB文件路径
        if filePath:
            self.pdb_path = filePath
            self.textBrowser_status.setText(f"\nPDB file selected: {filePath}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def loadResultFile(self):
        """Load local result file"""
        filePath, _ = QFileDialog.getOpenFileName(
            self, 
            "Select Result File", 
            "", 
            "CSV Files (*.csv);;All Files (*)"
        )
        
        if filePath:
            try:
                # 读取CSV文件
                self.data_with_preds = pd.read_csv(filePath)
                
                # 显示加载成功信息
                self.textBrowser_status.setText(f"\nSuccessfully loaded result file: {filePath}")
                self.textBrowser_status.setText(f"\nData shape: {self.data_with_preds.shape}")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                
                # 确保表格控件已创建
                if not hasattr(self, "tabSon_meloculesdata") or self.tabSon_meloculesdata is None:
                    self.textBrowser_status.setText("\nCreating table controls...")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    self.show_tabSon_meloculesdata()
                
                # 确保绘图控件已创建
                if not hasattr(self, "lineEdit_threshold") or self.lineEdit_threshold is None:
                    self.textBrowser_status.setText("\nCreating plot controls...")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    self.show_preds_plot()
                
                # 显示结果表格
                self.textBrowser_status.setText("\nDisplaying table data...")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                self.show_preds_table()
                
                self.textBrowser_status.setText("\nFile loading completed successfully!")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                
            except Exception as e:
                self.textBrowser_status.setText(f"\nError loading file: {str(e)}")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

    
    def selectATCcode(self, item:QTreeWidgetItem, column:int):
        selected_protease = item.text(1)  # Get MEROPS ID
        current_text = self.LineEdit_atc_code.text()
        
        # If current input is empty, set directly
        if not current_text.strip():
            self.LineEdit_atc_code.setText(selected_protease)
        else:
            # Check if protease is already included
            current_list = [x.strip() for x in current_text.split(',') if x.strip()]
            if selected_protease not in current_list:
                # Add new protease to the list
                current_list.append(selected_protease)
                self.LineEdit_atc_code.setText(','.join(current_list))
            else:
                # If already exists, remove from the list
                current_list.remove(selected_protease)
                self.LineEdit_atc_code.setText(','.join(current_list))
        
    def selectSpecies(self, item:QTreeWidgetItem, column:int):
        """选择物种即进入PSI模式：锁定参数框中的Proteases/Positions"""
        try:
            species = item.text(1)
            # 用物种映射填充Proteases
            species_to_proteases = self.load_species_to_proteases()
            proteases = species_to_proteases.get(species, [])
            self.LineEdit_atc_code.setText(','.join(proteases))
            # 锁定Proteases与Positions输入
            self.LineEdit_atc_code.setReadOnly(True)
            self.LineEdit_possr.setText("")
            self.LineEdit_possr.setReadOnly(True)
            # 状态提示
            self.textBrowser_status.setText(f"\nPSI mode: Species selected -> {species}. Proteases fixed to species proteases; Positions left empty (predict all).")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            # 记住当前PSI物种
            self.current_psi_species = species
        except Exception:
            pass

    def _toggle_group_body(self, body_widget: QtWidgets.QWidget):
        """切换分组内部主体可见性（折叠/展开）"""
        try:
            body_widget.setVisible(not body_widget.isVisible())
        except Exception:
            pass

    def _toggle_psi_group(self, event):
        """点击 PSI 标题：展开 PSI 并折叠 Proteases"""
        try:
            self.widget_psi_body.setVisible(True)
            self.widget_atc_body.setVisible(False)
            # 折叠时提示显示/隐藏
            self.label_psi_hint.setVisible(False)
            self.label_atc_hint.setVisible(True)
        except Exception:
            pass

    def _toggle_atc_group(self, event):
        """点击 Proteases 标题：展开 Proteases 并折叠 PSI"""
        try:
            self.widget_atc_body.setVisible(True)
            self.widget_psi_body.setVisible(False)
            # 折叠时提示显示/隐藏
            self.label_atc_hint.setVisible(False)
            self.label_psi_hint.setVisible(True)
        except Exception:
            pass

    def clean(self):
        # 清理动态创建的控件引用
        if hasattr(self, 'comboBox_proteases'):
            self.comboBox_proteases = None
        if hasattr(self, 'comboBox_protein_pos'):
            self.comboBox_protein_pos = None
        if hasattr(self, 'horizontalLayout_filter'):
            self.horizontalLayout_filter = None
        if hasattr(self, 'button_save_table'):
            self.button_save_table = None
        if hasattr(self, 'lineEdit_threshold'):
            self.lineEdit_threshold = None
        if hasattr(self, 'label_threshold'):
            self.label_threshold = None
        if hasattr(self, 'button_update_network'):
            self.button_update_network = None
        if hasattr(self, 'button_zoom_plot'):
            self.button_zoom_plot = None
        if hasattr(self, 'button_save_plot'):
            self.button_save_plot = None
        if hasattr(self, 'horizontalLayout_threshold'):
            self.horizontalLayout_threshold = None
        if hasattr(self, 'verticalLayout_tab_summaryplot'):
            self.verticalLayout_tab_summaryplot = None
        if hasattr(self, 'frame_plot'):
            self.frame_plot = None
        if hasattr(self, 'label_plot'):
            self.label_plot = None
        if hasattr(self, 'verticalLayout_frameplot'):
            self.verticalLayout_frameplot = None
        if hasattr(self, 'tabSon_meloculesdata'):
            self.tabSon_meloculesdata = None
        if hasattr(self, 'table_alldata'):
            self.table_alldata = None
        
        # 清理数据
        if hasattr(self, 'data_with_preds'):
            self.data_with_preds = None
    
        # 删除已经删除的 Qt 对象的引用
        self.centralwidget.deleteLater()
        self.centralwidget = None
        self.layout = None
        self.label = None
        self.combo_box = None
        self.button = None

        # 重新初始化界面
        self.setupUi(self)
        self.show_tabSon_meloculesdata()
        # 清除PSI物种状态，并恢复输入编辑
        if hasattr(self, 'current_psi_species'):
            self.current_psi_species = ''
        try:
            self.LineEdit_atc_code.setReadOnly(False)
            self.LineEdit_possr.setReadOnly(False)
        except Exception:
            pass

    def on_task_mode_changed(self):
        """已弃用：保留空实现以防信号残留"""
        return

    def populate_species_combo(self):
        """读取物种-蛋白酶映射并填充物种下拉框"""
        # 已改为上方 PSI 物种树展示；此函数保留兼容
        try:
            _ = self.load_species_to_proteases()
        except Exception:
            pass

    def load_species_to_proteases(self) -> Dict[str, List[str]]:
        """从文件构建 物种 -> [MEROPS_ID] 的映射"""
        mapping: Dict[str, List[str]] = {}
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # 文件路径由用户提供
            mapping_path = os.path.join(script_dir, 'Gui_data', 'protease_uniprot_Gene_organism_sort_103.txt')
            if not os.path.exists(mapping_path):
                # 兼容用户提供的绝对路径
                mapping_path = '/home/xudongguo/Projects/Guo/ProcleaveHub_new/ProcleaveContrastive/ProcleaveHub_GUI/GUI/Gui_data/protease_uniprot_Gene_organism_sort_103.txt'
            import csv
            with open(mapping_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader, None)
                for row in reader:
                    if not row or len(row) < 4:
                        continue
                    merops_id = row[0].strip()
                    organism = row[3].strip()
                    if merops_id and organism:
                        mapping.setdefault(organism, []).append(merops_id)
        except Exception:
            pass
        return mapping

    def getSavePath(self):
        time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        savePath = QFileDialog.getExistingDirectory(self, "Save Results")
        # savePath, ok = QInputDialog.getText(self, "Save Results", "Input Path")
        #if ok:
        self.save_path = Path(savePath+f'/predict_results_{time_str}.csv')
        self.data_with_preds.to_csv(self.save_path)
        self.textBrowser_status.setText("\nThe result has been saved to"+ savePath+f"/predict_results_{time_str}.csv !")
        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def validate_parameters(self):
        """Validate all required parameters before prediction"""
        # 是否处于PSI模式（通过是否选择了物种判断）
        task_mode = 'Cleavage'
        if hasattr(self, 'current_psi_species') and self.current_psi_species:
            task_mode = 'PSI'
        # Check PDB file selection
        if not self.filename.text() or self.filename.text().strip() == "":
            return {
                'valid': False,
                'message': "Error: Please select a PDB file first!"
            }
        
        # Check if PDB file exists
        pdb_file = Path(self.filename.text())
        if not pdb_file.exists():
            return {
                'valid': False,
                'message': f"Error: PDB file does not exist: {pdb_file}"
            }
        
        # Check file extension
        if not pdb_file.suffix.lower() in ['.pdb', '.ent']:
            return {
                'valid': False,
                'message': f"Error: Invalid file format. Please select a PDB file (.pdb or .ent), got: {pdb_file.suffix}"
            }
        
        # Check protease selection（Cleavage必填；PSI由物种映射自动设置）
        atc_code = self.LineEdit_atc_code.text().strip()
        if task_mode == 'Cleavage':
            if not atc_code:
                return {
                    'valid': False,
                    'message': "Warning: No protease selected. Please select at least one protease."
                }
        
        # Validate protease format (basic check)
        proteases_list = [x.strip() for x in atc_code.split(',') if x.strip()]
        if task_mode == 'Cleavage':
            if proteases_list:
                # Check if protease IDs are in valid format (basic pattern check)
                for protease in proteases_list:
                    if not protease or len(protease) < 3:
                        return {
                            'valid': False,
                            'message': f"Error: Invalid protease ID format: '{protease}'. Please check your selection."
                        }
        
        # Check chain parameter
        chain = self.LineEdit_chain.text().strip()
        if not chain:
            return {
                'valid': False,
                'message': "Error: Chain parameter cannot be empty. Please specify a chain (e.g., A, B, C)."
            }
        
        # Validate chain format (should be single letter)
        if len(chain) != 1 or not chain.isalpha():
            return {
                'valid': False,
                'message': f"Error: Invalid chain format: '{chain}'. Chain should be a single letter (e.g., A, B, C)."
            }
        
        # Check positions parameter (optional but validate format if provided)
        possr = self.LineEdit_possr.text().strip()
        if possr:
            try:
                # Split by comma and validate each position
                positions = [x.strip() for x in possr.split(',') if x.strip()]
                for pos in positions:
                    pos_int = int(pos)
                    if pos_int < 1:
                        return {
                            'valid': False,
                            'message': f"Error: Invalid position value: '{pos}'. Positions should be positive integers starting from 1."
                        }
            except ValueError:
                return {
                    'valid': False,
                    'message': f"Error: Invalid positions format: '{possr}'. Please use comma-separated integers (e.g., 4,5,6)."
                }
        else:
            # 如果positions为空，给出信息提示但不阻止运行
            return {
                'valid': True,
                'message': "Info: Positions parameter is empty. The system will predict all possible positions, which may take longer computation time. To specify specific positions, enter comma-separated values like '4,5,6'."
            }
        
        # Check num_workers parameter
        num_workers_text = self.LineEdit_num_workers.text().strip()
        if num_workers_text and num_workers_text.lower() != 'none':
            try:
                num_workers = int(num_workers_text)
                if num_workers < 1:
                    return {
                        'valid': False,
                        'message': f"Error: Invalid number of workers: {num_workers}. Should be a positive integer or 'None'."
                    }
            except ValueError:
                return {
                    'valid': False,
                    'message': f"Error: Invalid number of workers format: '{num_workers_text}'. Should be an integer or 'None'."
                }
        
        # All validations passed
        return {
            'valid': True,
            'message': "All parameters validated successfully."
        }
    
    def validate_chain_input(self):
        """Real-time validation for chain input"""
        chain = self.LineEdit_chain.text().strip()
        if chain and (len(chain) != 1 or not chain.isalpha()):
            # 设置样式提示错误
            self.LineEdit_chain.setStyleSheet("border: 2px solid red;")
            self.textBrowser_status.setText(f"Warning: Invalid chain format: '{chain}'. Should be a single letter (e.g., A, B, C).")
        else:
            # 清除错误样式
            self.LineEdit_chain.setStyleSheet("")
            if chain:
                # 只在非预测状态下显示验证信息
                # if not hasattr(self, 'button_predict') or self.button_predict.isEnabled():
                if not hasattr(self, 'predicting') or not self.predicting:
                    self.textBrowser_status.setText("Chain parameter looks good.")
    
    def validate_positions_input(self):
        """Real-time validation for positions input"""
        possr = self.LineEdit_possr.text().strip()
        if possr:
            try:
                positions = [x.strip() for x in possr.split(',') if x.strip()]
                for pos in positions:
                    pos_int = int(pos)
                    if pos_int < 1:
                        self.LineEdit_possr.setStyleSheet("border: 2px solid red;")
                        self.textBrowser_status.setText(f"Warning: Invalid position value: '{pos}'. Should be positive integers starting from 1.")
                        return
                self.LineEdit_possr.setStyleSheet("")
                # 只在非预测状态下显示验证信息
                # if not hasattr(self, 'button_predict') or self.button_predict.isEnabled():
                if not hasattr(self, 'predicting') or not self.predicting:
                    self.textBrowser_status.setText("Positions parameter looks good.")

            except ValueError:
                self.LineEdit_possr.setStyleSheet("border: 2px solid red;")
                self.textBrowser_status.setText(f"Warning: Invalid positions format: '{possr}'. Use comma-separated integers (e.g., 4,5,6).")
        else:
            self.LineEdit_possr.setStyleSheet("")
            # 只在非预测状态下显示验证信息
            # if not hasattr(self, 'button_predict') or self.button_predict.isEnabled():
            if not hasattr(self, 'predicting') or not self.predicting:
                self.textBrowser_status.setText("Info: Positions parameter is empty. The system will predict all possible positions, which may take longer computation time.")
    
    def validate_num_workers_input(self):
        """Real-time validation for num_workers input"""
        num_workers_text = self.LineEdit_num_workers.text().strip()
        if num_workers_text and num_workers_text.lower() != 'none':
            try:
                num_workers = int(num_workers_text)
                if num_workers < 1:
                    self.LineEdit_num_workers.setStyleSheet("border: 2px solid red;")
                    self.textBrowser_status.setText(f"Warning: Invalid number of workers: {num_workers}. Should be a positive integer or 'None'.")
                else:
                    self.LineEdit_num_workers.setStyleSheet("")
                    # 只在非预测状态下显示验证信息
                    # if not hasattr(self, 'button_predict') or self.button_predict.isEnabled():
                    if not hasattr(self, 'predicting') or not self.predicting:
                        self.textBrowser_status.setText("Number of workers parameter looks good.")

            except ValueError:
                self.LineEdit_num_workers.setStyleSheet("border: 2px solid red;")
                self.textBrowser_status.setText(f"Warning: Invalid number of workers format: '{num_workers_text}'. Should be an integer or 'None'.")
        else:
            self.LineEdit_num_workers.setStyleSheet("")
    
    def predict(self):
        # 先禁用预测按钮，防止重复点击
        self.button_predict.setEnabled(False)

        # 设置预测状态标志
        self.predicting = True

        # 暂时断开验证信号连接，防止覆盖Status信息
        try:
            self.LineEdit_chain.textChanged.disconnect(self.validate_chain_input)
        except:
            pass
        try:
            self.LineEdit_possr.textChanged.disconnect(self.validate_positions_input)
        except:
            pass
        try:
            self.LineEdit_num_workers.textChanged.disconnect(self.validate_num_workers_input)
        except:
            pass

        # 显示预测开始提示
        self.textBrowser_status.setText("\nPrediction in progress, please wait...")
        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
        # 立刻刷新事件循环，确保提示在耗时计算前显示
        QtWidgets.QApplication.processEvents()
        
        # 运行前判断参数是否完整
        validation_result = self.validate_parameters()
        if not validation_result['valid']:
            self.textBrowser_status.setText(f"\n{validation_result['message']}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            # 清除预测状态标志
            self.predicting = False
            self.button_predict.setEnabled(True)  # 重新启用按钮
            return 
        
        # 首次运行后组件显示
        if not hasattr(self, "tabSon_meloculesdata"):
            self.show_tabSon_meloculesdata()  
        
        

        
        
        self.data_path = Path(self.filename.text())
        # PDB文件路径已经在selectFile中设置，这里不需要重新设置
        # self.pdb_path = self.data_path.parent  # 这行是错误的，应该使用实际选择的PDB文件
        # print("self.pdb_path",self.pdb_path)
        # 是否处于PSI模式
        task_mode = 'Cleavage'
        if hasattr(self, 'current_psi_species') and self.current_psi_species:
            task_mode = 'PSI'

        # 获取蛋白酶参数（Cleavage直接取；PSI从物种映射填充）
        self.atc_code = self.LineEdit_atc_code.text()
        if task_mode == 'PSI':
            try:
                species = self.current_psi_species if hasattr(self, 'current_psi_species') else ''
                species_to_proteases = self.load_species_to_proteases()
                if species and species in species_to_proteases:
                    proteases_for_species = species_to_proteases[species]
                    self.atc_code = ','.join(proteases_for_species)
                else:
                    self.atc_code = ''
            except Exception:
                self.atc_code = ''
        # 解析为列表
        self.proteases_list = [x.strip() for x in self.atc_code.split(',') if x.strip()]
        # print("self.atc_code",self.atc_code)
        # print("self.proteases_list",self.proteases_list)
        # self.smile_column = self.LineEdit_smile_column.text()
        #self.include_physchem = self.LineEdit_include_physchem.text()
        # print(self.LineEdit_num_workers.text())
        self.num_workers = None if self.LineEdit_num_workers.text()=='None' else int(self.LineEdit_num_workers.text())
        self.chain = self.LineEdit_chain.text()
        self.possr = self.LineEdit_possr.text()
        
        # 获取当前脚本的绝对路径
        script_path = os.path.abspath(__file__)
        # 提取脚本所在目录
        script_dir = os.path.dirname(script_path)
        self.save_path = script_dir
        # 设置res目录路径
        self.res_path = os.path.join(script_dir, 'res')
        # print(f"script_dir: {script_dir}")
        # print(f"res_path: {self.res_path}")
        # print(f"res_path exists: {os.path.exists(self.res_path)}")
        
        # 如果res目录不存在，则创建它
        if not os.path.exists(self.res_path):
            try:
                os.makedirs(self.res_path)
                print(f"Created res directory: {self.res_path}")
            except Exception as e:
                print(f"Failed to create res directory: {e}")
                # 如果创建失败，使用当前目录
                self.res_path = script_dir
                print(f"Using script directory instead: {self.res_path}") 
        # 处理蛋白酶选择警告（如果验证通过但未选择蛋白酶）
        if not self.proteases_list:
            self.textBrowser_status.append("\nNo protease selected, using all proteases!")
            # 继续执行，不返回
        
        # PSI 快速通道：如果PDB链序列在缓存中，直接生成结果并跳过推理
        if task_mode == 'PSI':
            try:
                self.load_substrate_seq_cache()
                chain_id = self.LineEdit_chain.text().strip() or 'A'
                seq_from_pdb = self._extract_chain_sequence_from_pdb(self.pdb_path, chain_id)
                if seq_from_pdb and hasattr(self, '_substrate_seq_cache') and seq_from_pdb in getattr(self, '_substrate_seq_cache', {}):
                    df_cached = self._build_df_from_cache(seq_from_pdb, self.proteases_list)
                    if df_cached is not None and not df_cached.empty:
                        self.data_with_preds = df_cached
                        # UI ensure and display
                        if not hasattr(self, "tabSon_meloculesdata"):
                            self.show_tabSon_meloculesdata()
                        if not hasattr(self, "lineEdit_threshold") or self.lineEdit_threshold is None:
                            self.show_preds_plot()
                        self.show_preds_table()
                        self.textBrowser_status.setText("\nPSI shortcut: sequence found in cache. Skipped inference and loaded results (Pre_Score=0.99).")
                        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                        # 清除预测状态并恢复按钮/验证信号
                        self.predicting = False
                        try:
                            self.LineEdit_chain.textChanged.connect(self.validate_chain_input)
                        except Exception:
                            pass
                        try:
                            self.LineEdit_possr.textChanged.connect(self.validate_positions_input)
                        except Exception:
                            pass
                        try:
                            self.LineEdit_num_workers.textChanged.connect(self.validate_num_workers_input)
                        except Exception:
                            pass
                        self.button_predict.setEnabled(True)
                        return
            except Exception as e:
                # 未命中缓存或出错则继续常规推理
                self.textBrowser_status.append(f"\nPSI shortcut skipped due to: {str(e)}")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

        # 检查possr参数
        if not self.possr or self.possr.strip() == "":
            self.textBrowser_status.append("\nInfo: Positions parameter is empty. The system will predict all possible positions.")
            self.textBrowser_status.append("\nNote: Predicting all positions may take longer computation time. To specify specific positions, enter comma-separated values (e.g., 4,5,6).")
            # self.textBrowser_status.append("\nTo specify specific positions, enter comma-separated values (e.g., 4,5,6).")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            
            # 询问用户是否继续（默认选择Yes）
            from PyQt5.QtWidgets import QMessageBox
            reply = QMessageBox.question(
                self, 
                'Predict All Positions', 
                'The positions parameter is empty. The system will predict all possible positions.\n\nThis may take longer computation time.\n\nDo you want to continue?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes  # 默认选择Yes
            )
            
            if reply == QMessageBox.No:
                self.textBrowser_status.append("\nPrediction cancelled by user.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                self.button_predict.setEnabled(True)  # 重新启用按钮
                return
            else:
                self.textBrowser_status.append("\nContinuing with prediction of all positions...")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

        # 添加额外的参数验证
        try:

            
        # predict
            # print("self.possr",self.possr)
            # 获取PDB文件的目录路径
            pdb_dir = os.path.dirname(self.pdb_path)
            # self.data_with_preds = Cleavage_site_prediction(
            #     self.res_path, self.chain, 'Multi-protease', 
            #     self.data_path, self.pdb_path, 'pdb', 
            #      self.atc_code, self.num_workers,self.possr
            # )
            
            # 回调：将阶段性用时写入状态框
            def _status_cb(msg: str):
                """将回调消息中的 Position x / y 转换成百分比进度条"""
                try:
                    text = str(msg)
                    # 匹配 "Position {i+1} / {len(test_loader)}" 模式
                    m = re.search(r"Position\s+(\d+)\s*/\s*(\d+)", text)
                    if m:
                        cur = int(m.group(1))
                        total = int(m.group(2))
                        if total > 0:
                            pct = int(round(cur * 100 / total))
                            # 简单进度条（每#代表2%）最多50个#
                            bars = max(1, min(50, pct // 2))
                            bar_text = '#' * bars
                            self.textBrowser_status.setText(f"Progress: {bar_text} {pct}%")
                        else:
                            self.textBrowser_status.setText(text)
                    else:
                        # 非匹配信息原样输出
                        self.textBrowser_status.setText(text)
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    QtWidgets.QApplication.processEvents()
                except Exception:
                    pass

            self.data_with_preds = Cleavage_site_prediction(
                self.res_path, self.chain, 'Multi-protease', 
                self.data_path, pdb_dir, 'pdb', 
                 self.atc_code, self.num_workers,self.possr,
                 status_callback=_status_cb
            )
            
            self.textBrowser_status.setText("\nPrediction completed successfully!")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            
        except Exception as e:
            error_msg = f"\nError during prediction: {str(e)}"
            self.textBrowser_status.setText(error_msg)
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

            # 如果是possr相关错误，提供更具体的建议
            if "possr" in str(e).lower() or "position" in str(e).lower():
                self.textBrowser_status.setText(error_msg + "\n\nSuggestion: Please check the positions parameter. Try entering valid positions like '4,5,6' or leave empty for default behavior.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)

            # 清除预测状态标志
            self.predicting = False

            # 重新连接验证信号
            try:
                self.LineEdit_chain.textChanged.connect(self.validate_chain_input)
            except:
                pass
            try:
                self.LineEdit_possr.textChanged.connect(self.validate_positions_input)
            except:
                pass
            try:
                self.LineEdit_num_workers.textChanged.connect(self.validate_num_workers_input)
            except:
                pass

            # 重新启用预测按钮
            self.button_predict.setEnabled(True)
            return

        self.show_preds_table()
        self.show_preds_plot()

        
            

        # 状态栏显示运行过程中的异常信息
        # self.textBrowser_status.clear()
        if os.path.exists("logs.txt"):
            with open("logs.txt") as f:
                lines = f.readline()
                for line in lines:
                    self.textBrowser_status.insertPlainText(line)
        # self.textBrowser_status.insertPlainText("\nFinished!")
        # self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
        
        # 清除预测状态标志
        self.predicting = False

        # 重新连接验证信号
        try:
            self.LineEdit_chain.textChanged.connect(self.validate_chain_input)
        except:
            pass
        try:
            self.LineEdit_possr.textChanged.connect(self.validate_positions_input)
        except:
            pass
        try:
            self.LineEdit_num_workers.textChanged.connect(self.validate_num_workers_input)
        except:
            pass

        # 重新启用预测按钮
        self.button_predict.setEnabled(True)

    
    def show_preds_table(self):
        # 创建筛选控件（如果还没有创建）
        if not hasattr(self, 'comboBox_proteases') or self.comboBox_proteases is None:
            self.create_filter_controls()
        
        # 更新下拉列表选项
        self.update_filter_options()
        
        # 显示所有数据
        self.filter_and_display_data()
        # PSI模式：在表格区域增加可选阈值（默认0.9）
        try:
            if hasattr(self, 'current_psi_species') and self.current_psi_species:
                if not hasattr(self, 'lineEdit_table_threshold'):
                    self.lineEdit_table_threshold = QtWidgets.QLineEdit(self.tab_meloculesdata)
                    self.lineEdit_table_threshold.setObjectName('lineEdit_table_threshold')
                    self.lineEdit_table_threshold.setText('0.9')
                    self.lineEdit_table_threshold.setPlaceholderText('PSI table threshold (0-1)')
                    self.button_apply_table_threshold = QtWidgets.QPushButton(self.tab_meloculesdata)
                    self.button_apply_table_threshold.setText('Apply')
                    self.button_apply_table_threshold.clicked.connect(self.filter_and_display_data)
                    # 将其插入到筛选控件行末
                    if hasattr(self, 'horizontalLayout_filter') and self.horizontalLayout_filter is not None:
                        self.horizontalLayout_filter.addWidget(QtWidgets.QLabel('PSI Threshold:'))
                        self.horizontalLayout_filter.addWidget(self.lineEdit_table_threshold)
                        self.horizontalLayout_filter.addWidget(self.button_apply_table_threshold)
        except Exception:
            pass
    
    def create_filter_controls(self):
        """Create filter controls"""
        # 如果控件已存在且不为None，先清理
        if hasattr(self, 'horizontalLayout_filter') and self.horizontalLayout_filter is not None:
            try:
                # 清理现有布局
                while self.horizontalLayout_filter.count():
                    item = self.horizontalLayout_filter.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
            except:
                pass
        
        # 创建水平布局用于筛选控件
        self.horizontalLayout_filter = QtWidgets.QHBoxLayout()
        self.horizontalLayout_filter.setObjectName("horizontalLayout_filter")
        
        # 蛋白酶选择标签和下拉框
        self.label_proteases = QtWidgets.QLabel(self.tab_meloculesdata)
        self.label_proteases.setObjectName("label_proteases")
        self.label_proteases.setText("Select Protease:")
        self.horizontalLayout_filter.addWidget(self.label_proteases)
        
        self.comboBox_proteases = QtWidgets.QComboBox(self.tab_meloculesdata)
        self.comboBox_proteases.setObjectName("comboBox_proteases")
        self.comboBox_proteases.addItem("All")
        # Enable horizontal scrolling in dropdown
        try:
            self.comboBox_proteases.setView(QtWidgets.QListView())
            self.comboBox_proteases.view().setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.comboBox_proteases.view().setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
            # Avoid text elision so full text is scrollable
            if hasattr(self.comboBox_proteases.view(), 'setTextElideMode'):
                self.comboBox_proteases.view().setTextElideMode(QtCore.Qt.ElideNone)
        except Exception:
            pass
        self.horizontalLayout_filter.addWidget(self.comboBox_proteases)
        
        # 蛋白质位置选择标签和下拉框
        self.label_protein_pos = QtWidgets.QLabel(self.tab_meloculesdata)
        self.label_protein_pos.setObjectName("label_protein_pos")
        self.label_protein_pos.setText("Select Protein Position:")
        self.horizontalLayout_filter.addWidget(self.label_protein_pos)
        
        self.comboBox_protein_pos = QtWidgets.QComboBox(self.tab_meloculesdata)
        self.comboBox_protein_pos.setObjectName("comboBox_protein_pos")
        self.comboBox_protein_pos.addItem("All")
        # Enable horizontal scrolling in dropdown
        try:
            self.comboBox_protein_pos.setView(QtWidgets.QListView())
            self.comboBox_protein_pos.view().setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.comboBox_protein_pos.view().setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
            if hasattr(self.comboBox_protein_pos.view(), 'setTextElideMode'):
                self.comboBox_protein_pos.view().setTextElideMode(QtCore.Qt.ElideNone)
        except Exception:
            pass
        self.horizontalLayout_filter.addWidget(self.comboBox_protein_pos)
        
        # 添加筛选控件到布局
        self.verticalLayout_20.insertLayout(0, self.horizontalLayout_filter)
        
        # 添加保存表格按钮
        self.button_save_table = QtWidgets.QPushButton(self.tab_meloculesdata)
        self.button_save_table.setObjectName("button_save_table")
        self.button_save_table.setText("Save Table")
        self.horizontalLayout_filter.addWidget(self.button_save_table)
        
        # 添加3Dmol.js可视化按钮
        self.button_3dmol_visualize = QtWidgets.QPushButton(self.tab_meloculesdata)
        self.button_3dmol_visualize.setObjectName("button_3dmol_visualize")
        self.button_3dmol_visualize.setText("3D View")
        self.button_3dmol_visualize.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #138496;
            }
            QPushButton:pressed {
                background-color: #117a8b;
            }
        """)
        self.horizontalLayout_filter.addWidget(self.button_3dmol_visualize)
        
        # 连接信号
        self.comboBox_proteases.currentTextChanged.connect(self.filter_and_display_data)
        self.comboBox_protein_pos.currentTextChanged.connect(self.filter_and_display_data)
        self.button_save_table.clicked.connect(self.save_table_data)
        self.button_3dmol_visualize.clicked.connect(self.visualize_with_3dmol)
    
    def update_filter_options(self):
        """Update filter options"""
        # 检查控件是否存在
        if not hasattr(self, 'comboBox_proteases') or self.comboBox_proteases is None:
            return
        if not hasattr(self, 'comboBox_protein_pos') or self.comboBox_protein_pos is None:
            return
            
        try:
            # 更新蛋白酶选项
            self.comboBox_proteases.clear()
            self.comboBox_proteases.addItem("All")
            if hasattr(self, 'data_with_preds') and self.data_with_preds is not None and not self.data_with_preds.empty:
                proteases = sorted(self.data_with_preds['Proteases'].unique())
                self.comboBox_proteases.addItems(proteases)
            
            # 更新蛋白质位置选项
            self.comboBox_protein_pos.clear()
            self.comboBox_protein_pos.addItem("All")
            if hasattr(self, 'data_with_preds') and self.data_with_preds is not None and not self.data_with_preds.empty:
                protein_positions = sorted(self.data_with_preds['Protein|position'].unique())
                self.comboBox_protein_pos.addItems(protein_positions)
        except RuntimeError:
            # 如果控件已被删除，重新创建
            self.create_filter_controls()
            self.update_filter_options()
    
    def filter_and_display_data(self):
        """Filter and display data based on selection"""
        if not hasattr(self, 'data_with_preds') or self.data_with_preds is None or self.data_with_preds.empty:
            return
        
        # 检查控件是否存在
        if not hasattr(self, 'comboBox_proteases') or self.comboBox_proteases is None:
            return
        if not hasattr(self, 'comboBox_protein_pos') or self.comboBox_protein_pos is None:
            return
        
        try:
            # 获取选择的筛选条件
            selected_protease = self.comboBox_proteases.currentText()
            selected_protein_pos = self.comboBox_protein_pos.currentText()
        except RuntimeError:
            # 如果控件已被删除，重新创建
            self.create_filter_controls()
            return
        
        # 筛选数据
        filtered_data = self.data_with_preds.copy()
        # PSI模式增加阈值与Proteases去重（取最大Pre_Score）
        try:
            if hasattr(self, 'current_psi_species') and self.current_psi_species:
                thr = 0.9
                if hasattr(self, 'lineEdit_table_threshold') and self.lineEdit_table_threshold is not None:
                    try:
                        thr = float(self.lineEdit_table_threshold.text())
                    except Exception:
                        thr = 0.9
                # 只保留Pre_Score>thr
                if 'Pre_Score' in filtered_data.columns:
                    filtered_data = filtered_data[filtered_data['Pre_Score'] > thr]
                # 若有重复Proteases，保留Pre_Score最大的行
                if set(['Proteases','Pre_Score']).issubset(set(filtered_data.columns)):
                    filtered_data = filtered_data.sort_values('Pre_Score', ascending=False)
                    filtered_data = filtered_data.drop_duplicates(subset=['Proteases'], keep='first')
        except Exception:
            pass
        
        if selected_protease != "All":
            filtered_data = filtered_data[filtered_data['Proteases'] == selected_protease]
        
        if selected_protein_pos != "All":
            filtered_data = filtered_data[filtered_data['Protein|position'] == selected_protein_pos]
        
        # 显示筛选后的数据
        self.display_data_in_table(filtered_data)
        
        # 注意：网络图现在只在用户点击Plot页面时才绘制，以提高表格显示速度
    
    def display_data_in_table(self, data):
        """Display data in table"""
        # 确保表格控件存在
        if not hasattr(self, 'table_alldata'):
            if hasattr(self, 'tabSon_meloculesdata'):
                # 如果tabSon_meloculesdata存在但table_alldata不存在，重新创建
                self.show_tabSon_meloculesdata()
            else:
                print("Error: Table widget not created")
                return
        
        self.table_alldata.clear()
        
        # 处理数据：不显示Pre_label列，将Protein|position列分成两列
        display_data = data.copy()
        
        # 删除Pre_label列
        if 'Pre_label' in display_data.columns:
            display_data = display_data.drop('Pre_label', axis=1)
        
        # 将Protein|position列分成Protein和Position两列
        if 'Protein|position' in display_data.columns:
            # 分割Protein|position列
            protein_pos_split = display_data['Protein|position'].str.split('|', expand=True)
            if protein_pos_split.shape[1] >= 2:
                display_data['Protein'] = protein_pos_split[0]
                display_data['Position'] = protein_pos_split[1]
                # 删除原始的Protein|position列
                display_data = display_data.drop('Protein|position', axis=1)
                # PSI 模式下不显示 Position 列；其他模式显示
                psi_mode = hasattr(self, 'current_psi_species') and bool(self.current_psi_species)
                if psi_mode:
                    desired_columns = ['Proteases', 'Protein', 'Pre_Score']
                else:
                    desired_columns = ['Proteases', 'Protein', 'Position', 'Pre_Score']
                existing_cols = [c for c in desired_columns if c in display_data.columns]
                display_data = display_data[existing_cols]
        
        # 设置表格属性
        colum_num = display_data.shape[1]
        index_num = display_data.shape[0]
        header = display_data.columns
        self.table_alldata.setColumnCount(colum_num)
        self.table_alldata.setRowCount(index_num)
        self.table_alldata.setHorizontalHeaderLabels(header)
        
        # 启用排序功能
        self.table_alldata.setSortingEnabled(True)
        
        # 设置自定义排序代理（如果需要更精确的数值排序）
        # 注意：QTableWidget的排序功能已经足够，这里主要是为了确保数值排序正确
        
        # 设置表格内容
        for i in range(0, index_num):
            for j in range(0, colum_num):
                value = display_data.values[i][j]
                # 如果是Pre_Score列，格式化为3位小数
                if display_data.columns[j] == 'Pre_Score':
                    try:
                        formatted_value = f"{float(value):.3f}"
                        # 创建QTableWidgetItem并设置数值用于排序
                        cell = QTableWidgetItem(formatted_value)
                        cell.setData(QtCore.Qt.UserRole, float(value))  # 设置原始数值用于排序
                    except (ValueError, TypeError):
                        formatted_value = str(value)
                        cell = QTableWidgetItem(formatted_value)
                else:
                    formatted_value = str(value)
                    cell = QTableWidgetItem(formatted_value)
                
                self.table_alldata.setItem(i, j, cell)

    def show_preds_plot(self):
        # 首次运行显示图和属性选择按钮
        if not hasattr(self, "verticalLayout_tab_summaryplot") or self.verticalLayout_tab_summaryplot is None:
            self.verticalLayout_tab_summaryplot = QtWidgets.QVBoxLayout(self.tab_summayplot)
        self.verticalLayout_tab_summaryplot.setObjectName("verticalLayout_tab_summaryplot")
        self.frame_plot = QtWidgets.QFrame(self.tab_summayplot)
        self.frame_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plot.setObjectName("frame_plot")

        self.verticalLayout_frameplot = QtWidgets.QVBoxLayout(self.frame_plot)
        self.verticalLayout_frameplot.setObjectName("verticalLayout_frameplot")
        self.label_plot = QtWidgets.QLabel(self.frame_plot)
        self.label_plot.setText("")
        self.label_plot.setObjectName("label_plot")
        self.label_plot.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.verticalLayout_frameplot.addWidget(self.label_plot)
        self.verticalLayout_frameplot.setContentsMargins(30,30,30,30)

        self.verticalLayout_tab_summaryplot.addWidget(self.frame_plot)
                                
        # 添加阈值设置控件
        self.horizontalLayout_threshold = QtWidgets.QHBoxLayout()
        self.horizontalLayout_threshold.setObjectName("horizontalLayout_threshold")
        
        self.label_threshold = QtWidgets.QLabel(self.tab_summayplot)
        self.label_threshold.setObjectName("label_threshold")
        self.label_threshold.setText("threshold:")
        self.horizontalLayout_threshold.addWidget(self.label_threshold)
        
        self.lineEdit_threshold = QtWidgets.QLineEdit(self.tab_summayplot)
        self.lineEdit_threshold.setObjectName("lineEdit_threshold")
        self.lineEdit_threshold.setText("0.5")
        self.lineEdit_threshold.setPlaceholderText("threshold (0-1)")
        self.horizontalLayout_threshold.addWidget(self.lineEdit_threshold)
        
        self.button_update_network = QtWidgets.QPushButton(self.tab_summayplot)
        self.button_update_network.setObjectName("button_update_network")
        self.button_update_network.setText("Update")
        self.horizontalLayout_threshold.addWidget(self.button_update_network)
        
        self.button_zoom_plot = QtWidgets.QPushButton(self.tab_summayplot)
        self.button_zoom_plot.setObjectName("button_zoom_plot")
        self.button_zoom_plot.setText("Zoom View")
        self.horizontalLayout_threshold.addWidget(self.button_zoom_plot)
        
        self.button_save_plot = QtWidgets.QPushButton(self.tab_summayplot)
        self.button_save_plot.setObjectName("button_save_plot")
        self.button_save_plot.setText("Save Plot")
        self.horizontalLayout_threshold.addWidget(self.button_save_plot)
        
        self.verticalLayout_tab_summaryplot.addLayout(self.horizontalLayout_threshold)
        
        # 连接信号
        self.button_update_network.clicked.connect(self.update_network_plot)
        self.button_zoom_plot.clicked.connect(self.show_zoom_plot)
        self.button_save_plot.clicked.connect(self.save_network_plot)
        
        # 注意：网络图现在只在用户点击"Update Network"按钮时才绘制
    
    def update_network_plot(self):
        """Update network plot"""
        # 检查控件是否存在
        if not hasattr(self, 'lineEdit_threshold') or self.lineEdit_threshold is None:
            return
        
        try:
            # 获取阈值
            threshold = float(self.lineEdit_threshold.text())
        except ValueError:
            threshold = 0.5
            if self.lineEdit_threshold is not None:
                self.lineEdit_threshold.setText("0.5")

        # 获取当前筛选的数据用于绘图
        plot_data = self.get_current_filtered_data()
        # PSI模式下也应用表格阈值筛选
        try:
            if hasattr(self, 'current_psi_species') and self.current_psi_species:
                thr = 0.9
                if hasattr(self, 'lineEdit_table_threshold') and self.lineEdit_table_threshold is not None:
                    try:
                        thr = float(self.lineEdit_table_threshold.text())
                    except Exception:
                        thr = 0.9
                if 'Pre_Score' in plot_data.columns:
                    plot_data = plot_data[plot_data['Pre_Score'] > thr]
                if set(['Proteases','Pre_Score']).issubset(set(plot_data.columns)):
                    plot_data = plot_data.sort_values('Pre_Score', ascending=False)
                    plot_data = plot_data.drop_duplicates(subset=['Proteases'], keep='first')
        except Exception:
            pass
        
        # 添加调试信息
        if hasattr(self, 'textBrowser_status'):
            self.textBrowser_status.setText(f"\nPlot data shape: {plot_data.shape}")
            self.textBrowser_status.setText(f"\nThreshold: {threshold}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
        
        # 绘制网络图（PSI 与 Cleavage 分开）
        if hasattr(self, 'current_psi_species') and self.current_psi_species:
            self.draw_psi_network_plot(plot_data)
        else:
            self.draw_network_plot(plot_data, threshold)
    
    def draw_network_plot(self, plot_data, threshold=0.5):
        """Draw network plot"""
        try:
            if plot_data.empty:
                self.label_plot.setText("No data to display in plot.")
                return

            # 创建网络图
            G = nx.Graph()
            
            # 加载merops到uniprot的映射
            merops_to_uniprot = self.load_merops_uniprot_mapping()
            
            # 加载蛋白酶PPI数据
            ppi_matrix = self.load_protease_ppi()
            
            # 添加节点和边
            self.add_nodes_and_edges(G, plot_data, threshold, merops_to_uniprot, ppi_matrix)
            
            # 绘制网络图
            self.plot_network(G, threshold)
            
        except Exception as e:
            # print(f"绘制网络图时出错: {e}")
            # 显示错误信息
            self.label_plot.setText(f"Error drawing network plot: {str(e)}")

    def draw_psi_network_plot(self, plot_data):
        """PSI模式网络图：一个蛋白节点 + 多个蛋白酶节点，边标签为 Position|Pre_Score，阈值固定为0.9"""
        try:
            if plot_data.empty:
                self.label_plot.setText("No data to display in plot.")
                return

            # 只保留 Pre_Score > 0.9
            data = plot_data.copy()
            if 'Pre_Score' in data.columns:
                data = data[data['Pre_Score'] > 0.9]
            if data.empty:
                self.label_plot.setText("No edges above threshold (0.9)")
                return

            # 确保有 Position 列（从 Protein|position 拆分得到）
            if 'Position' not in data.columns and 'Protein|position' in data.columns:
                protein_pos_split = data['Protein|position'].str.split('|', expand=True)
                if protein_pos_split.shape[1] >= 2:
                    data['Protein'] = protein_pos_split[0]
                    data['Position'] = protein_pos_split[1]

            # 确定底物蛋白名（取第一行 Protein）
            if 'Protein' in data.columns and not data['Protein'].empty:
                protein_name = str(data['Protein'].iloc[0])
            else:
                protein_name = 'Protein'

            # 构建网络
            G = nx.Graph()
            G.add_node(protein_name, node_type='protein', color='#4ECDC4')

            for _, row in data.iterrows():
                protease = row.get('Proteases', None)
                pre_score = row.get('Pre_Score', None)
                position = row.get('Position', None)
                if protease is None or pre_score is None:
                    continue
                # 添加蛋白酶节点
                G.add_node(protease, node_type='protease', color='#FF6B6B')
                # 添加蛋白-蛋白酶边，保存标签
                label_text = f"{position}|{float(pre_score):.3f}" if position is not None else f"{float(pre_score):.3f}"
                G.add_edge(protein_name, protease, edge_type='psi', weight=float(pre_score), label=label_text)

            # 绘制
            fig, ax = plt.subplots(figsize=(14, 12))
            fig.patch.set_facecolor('white')
            ax.set_facecolor('white')

            pos = nx.spring_layout(G, k=2, iterations=100, seed=42)

            protein_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'protein']
            protease_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'protease']
            edges = list(G.edges())

            if protease_nodes:
                nx.draw_networkx_nodes(G, pos, nodelist=protease_nodes,
                                       node_color='#FF6B6B', node_size=650,
                                       alpha=0.9, edgecolors='#CC0000', linewidths=1,
                                       label='Protease')
            if protein_nodes:
                nx.draw_networkx_nodes(G, pos, nodelist=protein_nodes,
                                       node_color='#4ECDC4', node_size=900,
                                       alpha=0.95, edgecolors='#008B8B', linewidths=2,
                                       label='Protein')

            if edges:
                nx.draw_networkx_edges(G, pos, edgelist=edges,
                                       edge_color='#4444FF', alpha=0.6, width=2.5,
                                       style='-')

                # 边标签：Position|Pre_Score
                edge_labels = {}
                for u, v, d in G.edges(data=True):
                    edge_labels[(u, v)] = d.get('label', '')
                nx.draw_networkx_edge_labels(G, pos, edge_labels,
                                             font_size=9, font_family='Arial',
                                             font_color='#1f2d3d', font_weight='bold',
                                             bbox=dict(boxstyle="round,pad=0.2",
                                                       facecolor='white', edgecolor='#CCCCCC',
                                                       alpha=0.8, linewidth=0.5))

            nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold',
                                     font_family='Arial', font_color='#2C3E50')

            plt.title('PSI Network (Protein–Protease)', fontsize=16, fontweight='bold',
                      fontfamily='Arial', color='#2C3E50', pad=20)
            plt.axis('off')
            plt.tight_layout()

            plt.savefig("network_plot.jpg", dpi=300, bbox_inches='tight',
                        facecolor='white', edgecolor='none')

            pixmap = QPixmap("network_plot.jpg")
            self.label_plot.setPixmap(pixmap)
            self.label_plot.setScaledContents(True)
            plt.close()

        except Exception as e:
            self.label_plot.setText(f"Error drawing PSI plot: {str(e)}")
    
    def load_merops_uniprot_mapping(self):
        """Load merops to uniprot mapping"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            pkl_path = os.path.join(script_dir, "Gui_data", "merops_uid_dict.pkl")
            with open(pkl_path, 'rb') as f:
                mapping = pickle.load(f)
                # print(f"成功加载merops映射，包含 {len(mapping)} 个条目")
                # print(f"映射示例: {dict(list(mapping.items())[:3])}")
                return mapping
        except Exception as e:
            print(f"加载merops映射文件时出错: {e}")
            return {}
    
    def load_protease_ppi(self):
        """Load protease PPI matrix"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            ppi_path = os.path.join(script_dir, "Gui_data", "protease_ppi.txt")
            ppi_matrix = pd.read_csv(ppi_path, index_col=0)
            # print(f"成功加载PPI矩阵，形状: {ppi_matrix.shape}")
            # print(f"PPI矩阵列名示例: {list(ppi_matrix.columns)[:5]}")
            return ppi_matrix
        except Exception as e:
            print(f"加载PPI文件时出错: {e}")
            return pd.DataFrame()

    def load_substrate_seq_cache(self):
        """Lazily load sequence -> (substrate_uniprot, {protease_token: [sites]}) cache."""
        if hasattr(self, '_seq_cache_loaded') and getattr(self, '_seq_cache_loaded'):
            return
        self._substrate_seq_cache = {}
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            pkl_path = os.path.join(script_dir, "Gui_data", "substrate_seq_to_proteases_sites.pkl")
            # fallback_path = "/home/xudongguo/Projects/Guo/ProcleaveHub_new/ProcleaveContrastive/data/substrate_seq_to_proteases_sites_resplit4.pkl"
            # pkl_path = local_path if os.path.exists(local_path) else fallback_path if os.path.exists(fallback_path) else None
            if pkl_path:
                with open(pkl_path, 'rb') as f:
                    self._substrate_seq_cache = pickle.load(f)
                self._seq_cache_loaded = True
            else:
                self._seq_cache_loaded = True
        except Exception:
            self._seq_cache_loaded = True

    def _extract_chain_sequence_from_pdb(self, pdb_path: str, chain_id: str) -> str:
        """Extract and sanitize chain sequence from a PDB file (pdb-atom parser)."""
        try:
            chain_map = {str(record.id).split(':')[-1]: str(record.seq) for record in SeqIO.parse(pdb_path, 'pdb-atom')}
            if chain_id not in chain_map:
                return ""
            seq = chain_map[chain_id]
            seq = re.sub('[^ACDEFGHIKLMNPQRSTVWYX]', 'X', ''.join(seq).upper())
            return seq
        except Exception:
            return ""

    def _build_df_from_cache(self, sequence: str, merops_filter: List[str]) -> pd.DataFrame:
        """Build DataFrame rows from cache for a given sequence.
        Columns: Proteases, Protein|position, Pre_Score, Pre_label
        """
        rows = []
        if not hasattr(self, '_substrate_seq_cache'):
            return pd.DataFrame(columns=['Proteases', 'Protein|position', 'Pre_Score'])
        if sequence not in self._substrate_seq_cache:
            return pd.DataFrame(columns=['Proteases', 'Protein|position', 'Pre_Score'])
        try:
            substrate_uniprot, protease_sites = self._substrate_seq_cache[sequence]
            allowed = set([p.strip() for p in (merops_filter or []) if p.strip()])
            for protease_token, site_list in protease_sites.items():
                merops_id = protease_token.split('&')[0] if isinstance(protease_token, str) else str(protease_token)
                if allowed and merops_id not in allowed:
                    continue
                try:
                    for pos in sorted(set(site_list)):
                        rows.append({
                            'Proteases': merops_id,
                            'Protein|position': f"{substrate_uniprot}|{int(pos)}",
                            'Pre_Score': 0.99,
                            'Pre_label': 1
                        })
                except Exception:
                    continue
        except Exception:
            return pd.DataFrame(columns=['Proteases', 'Protein|position', 'Pre_Score'])
        if not rows:
            return pd.DataFrame(columns=['Proteases', 'Protein|position', 'Pre_Score'])
        df = pd.DataFrame(rows)
        return df
    
    def add_nodes_and_edges(self, G, plot_data, threshold, merops_to_uniprot, ppi_matrix):
        """Add nodes and edges to network graph"""
        # 获取预测数据中的蛋白酶和蛋白质位置
        proteases = plot_data['Proteases'].unique()
        protein_positions = plot_data['Protein|position'].unique()
        
        # 添加蛋白酶节点
        for protease in proteases:
            G.add_node(protease, node_type='protease', color='lightblue')
        
        # 筛选蛋白质位置节点：只有当该位置对应的所有Pre_Score值中至少有一个大于阈值时才添加
        valid_protein_positions = []
        for pos in protein_positions:
            # 获取该蛋白质位置对应的所有Pre_Score值
            pos_scores = plot_data[plot_data['Protein|position'] == pos]['Pre_Score']
            # 如果至少有一个Pre_Score值大于阈值，则添加该节点
            if pos_scores.max() > threshold:
                G.add_node(pos, node_type='protein_position', color='lightcoral')
                valid_protein_positions.append(pos)
        
        # print(f"筛选后保留的蛋白质位置节点数量: {len(valid_protein_positions)}")
        
        # 根据Pre_Score添加蛋白酶-蛋白质位置边
        prediction_edge_count = 0
        for _, row in plot_data.iterrows():
            if row['Pre_Score'] > threshold and row['Protein|position'] in valid_protein_positions:
                G.add_edge(row['Proteases'], row['Protein|position'], 
                          weight=row['Pre_Score'], edge_type='prediction')
                prediction_edge_count += 1
        
        # print(f"总共添加了 {prediction_edge_count} 条预测边")
        
        # 根据PPI数据添加蛋白酶-蛋白酶边
        ppi_edge_count = 0
        added_edges = set()  # 用于避免重复添加边
        
        # print(f"开始检查 {len(proteases)} 个蛋白酶之间的PPI关系...")
        
        for i, protease1 in enumerate(proteases):
            if protease1 in merops_to_uniprot:
                uniprot1 = merops_to_uniprot[protease1]
                # print(f"检查蛋白酶 {i+1}/{len(proteases)}: {protease1} -> {uniprot1}")
                
                for j, protease2 in enumerate(proteases):
                    if protease2 in merops_to_uniprot and protease1 != protease2:  # 避免自环
                        uniprot2 = merops_to_uniprot[protease2]
                        
                        # 创建边的唯一标识符（避免重复）
                        edge_key = tuple(sorted([protease1, protease2]))
                        
                        if edge_key not in added_edges:
                            if (uniprot1 in ppi_matrix.index and 
                                uniprot2 in ppi_matrix.columns and 
                                ppi_matrix.loc[uniprot1, uniprot2] == 1):
                                G.add_edge(protease1, protease2, edge_type='ppi')
                                ppi_edge_count += 1
                                added_edges.add(edge_key)
                                # print(f"  添加PPI边: {protease1}({uniprot1}) - {protease2}({uniprot2})")
                            else:
                                pass
                                # print(f"  无PPI关系: {protease1}({uniprot1}) - {protease2}({uniprot2})")
        
        # print(f"总共添加了 {ppi_edge_count} 条PPI边")
        # print(f"检查了 {len(proteases)} 个蛋白酶，共 {len(proteases) * (len(proteases) - 1) // 2} 对组合")
    
    def plot_network(self, G, threshold):
        """Plot network graph"""
        if len(G.nodes()) == 0:
            self.label_plot.setText("No nodes to display")
            return
        
        # 设置matplotlib参数
        plt.rcParams['font.family'] = 'Arial'
        plt.rcParams['font.size'] = 10
        
        # 设置图形大小和背景
        fig, ax = plt.subplots(figsize=(14, 12))
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        
        # 使用spring布局，增加迭代次数获得更好的布局
        pos = nx.spring_layout(G, k=2, iterations=100, seed=42)
        
        # 分离不同类型的节点
        protease_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'protease']
        position_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'protein_position']
        
        # 分离不同类型的边
        prediction_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('edge_type') == 'prediction']
        ppi_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('edge_type') == 'ppi']
        
        # 绘制边 - 使用曲线
        if prediction_edges:
            nx.draw_networkx_edges(G, pos, edgelist=prediction_edges, 
                                 edge_color='#FF4444', alpha=0.7, width=2.5, 
                                 style='-', connectionstyle="arc3,rad=0.1",
                                 label=f'Prediction (threshold>{threshold})')
        
        if ppi_edges:
            nx.draw_networkx_edges(G, pos, edgelist=ppi_edges, 
                                 edge_color='#4444FF', alpha=0.6, width=2, 
                                 style='--', connectionstyle="arc3,rad=0.2",
                                 label='PPI Interaction')
        
        # 为预测边添加Pre_Score标签
        if prediction_edges:
            edge_labels = {}
            for u, v, d in G.edges(data=True):
                if d.get('edge_type') == 'prediction':
                    score = d.get('weight', 0)
                    edge_labels[(u, v)] = f'{score:.3f}'
            
            # 绘制边标签
            nx.draw_networkx_edge_labels(G, pos, edge_labels, 
                                       font_size=8, font_family='Arial', 
                                       font_color='#8B0000', font_weight='bold',
                                       bbox=dict(boxstyle="round,pad=0.2", 
                                               facecolor='white', 
                                               edgecolor='#FF4444', 
                                               alpha=0.8, linewidth=0.5))
        
        # 绘制节点 - 使用更鲜艳的颜色
        if protease_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=protease_nodes, 
                                 node_color='#FF6B6B', node_size=550, 
                                 alpha=0.9, edgecolors='#CC0000', linewidths=1,
                                 label='Protease')
        
        if position_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=position_nodes, 
                                 node_color='#4ECDC4', node_size=350, 
                                 alpha=0.9, edgecolors='#008B8B', linewidths=1,
                                 label='Cleavage Site')
        
        # 添加标签 - 使用更好的字体和颜色
        nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold', 
                               font_family='Arial', font_color='#2C3E50')
        
        # 设置标题
        plt.title(f'Protease-Cleavage Site Interaction Network\n(Threshold: {threshold})', 
                 fontsize=16, fontweight='bold', fontfamily='Arial', 
                 color='#2C3E50', pad=20)
        
        # 优化图例布局 - 避免重叠
        legend_elements = []
        if prediction_edges:
            legend_elements.append(plt.Line2D([0], [0], color='#FF4444', lw=2.5, 
                                            label=f'Prediction (>{threshold})'))
        if ppi_edges:
            legend_elements.append(plt.Line2D([0], [0], color='#4444FF', lw=2, 
                                            linestyle='--', label='PPI Interaction'))
        if protease_nodes:
            legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', 
                                            markerfacecolor='#FF6B6B', markersize=12,
                                            markeredgecolor='#CC0000', markeredgewidth=2,
                                            label='Protease'))
        if position_nodes:
            legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', 
                                            markerfacecolor='#4ECDC4', markersize=10,
                                            markeredgecolor='#008B8B', markeredgewidth=2,
                                            label='Cleavage Site'))
        
        # 创建图例，使用更好的布局
        legend = ax.legend(handles=legend_elements, loc='upper left', 
                          bbox_to_anchor=(0.02, 0.98), frameon=True, 
                          fancybox=True, shadow=True, fontsize=11,
                          framealpha=0.9, edgecolor='#CCCCCC')
        legend.get_frame().set_facecolor('#F8F9FA')
        
        # 添加统计信息
        stats_text = f'Nodes: {len(G.nodes())} | Edges: {len(G.edges())}'
        if prediction_edges:
            stats_text += f'\nPrediction edges: {len(prediction_edges)}'
        if ppi_edges:
            stats_text += f'\nPPI edges: {len(ppi_edges)}'
        
        ax.text(0.02, 0.02, stats_text, transform=ax.transAxes, 
               fontsize=10, fontfamily='Arial', color='#666666',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='#F8F9FA', 
                        edgecolor='#CCCCCC', alpha=0.8))
        
        plt.axis('off')
        plt.tight_layout()
        
        # 保存图片
        plt.savefig("network_plot.jpg", dpi=300, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        
        # 显示图片
        pixmap = QPixmap("network_plot.jpg")
        self.label_plot.setPixmap(pixmap)
        self.label_plot.setScaledContents(True)
        
        # 清理matplotlib图形
        plt.close()
    
    def show_zoom_plot(self):
        """Show interactive zoom view of the network plot"""
        # 检查控件是否存在
        if not hasattr(self, 'lineEdit_threshold') or self.lineEdit_threshold is None:
            self.textBrowser_status.setText("\nError: Plot controls not initialized. Please load data first.")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            return
        
        try:
            # 获取当前阈值
            threshold = float(self.lineEdit_threshold.text())
        except ValueError:
            threshold = 0.5
            if self.lineEdit_threshold is not None:
                self.lineEdit_threshold.setText("0.5")
        
        # 检查是否有数据
        if not hasattr(self, 'data_with_preds') or self.data_with_preds.empty:
            self.textBrowser_status.setText("\nError: No prediction data available. Please run prediction first.")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            return
        
        try:
            # 获取当前筛选的数据用于绘图
            plot_data = self.get_current_filtered_data()
            
            # 创建网络图
            G = nx.Graph()
            
            # 加载数据
            merops_to_uniprot = self.load_merops_uniprot_mapping()
            ppi_matrix = self.load_protease_ppi()
            
            # 添加节点和边
            self.add_nodes_and_edges(G, plot_data, threshold, merops_to_uniprot, ppi_matrix)
            
            if len(G.nodes()) == 0:
                self.textBrowser_status.setText("\nNo nodes to display in zoom view.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return
            
            # 创建交互式图形
            self.create_interactive_plot(G, threshold)
            
        except Exception as e:
            self.textBrowser_status.setText(f"\nError creating zoom view: {str(e)}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def create_interactive_plot(self, G, threshold):
        """Create interactive matplotlib plot for zoom view"""
        # 设置matplotlib参数
        plt.rcParams['font.family'] = 'Arial'
        plt.rcParams['font.size'] = 12
        
        # 创建新的图形窗口
        fig, ax = plt.subplots(figsize=(16, 12))
        fig.suptitle(f'Interactive Network Plot - Threshold: {threshold}', 
                    fontsize=16, fontweight='bold', fontfamily='Arial')
        
        # 使用spring布局
        pos = nx.spring_layout(G, k=2, iterations=100, seed=42)
        
        # 分离不同类型的节点和边
        protease_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'protease']
        position_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'protein_position']
        prediction_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('edge_type') == 'prediction']
        ppi_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('edge_type') == 'ppi']
        
        # 绘制边
        if prediction_edges:
            nx.draw_networkx_edges(G, pos, edgelist=prediction_edges, 
                                 edge_color='#FF4444', alpha=0.7, width=2.5, 
                                 style='-', connectionstyle="arc3,rad=0.1", ax=ax)
        
        if ppi_edges:
            nx.draw_networkx_edges(G, pos, edgelist=ppi_edges, 
                                 edge_color='#4444FF', alpha=0.6, width=2, 
                                 style='--', connectionstyle="arc3,rad=0.2", ax=ax)
        
        # 绘制节点
        if protease_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=protease_nodes, 
                                 node_color='#FF6B6B', node_size=800, 
                                 alpha=0.9, edgecolors='#CC0000', linewidths=2, ax=ax)
        
        if position_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=position_nodes, 
                                 node_color='#4ECDC4', node_size=500, 
                                 alpha=0.9, edgecolors='#008B8B', linewidths=2, ax=ax)
        
        # 添加标签
        nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', 
                               font_family='Arial', font_color='#2C3E50', ax=ax)
        
        # 为预测边添加Pre_Score标签
        if prediction_edges:
            edge_labels = {}
            for u, v, d in G.edges(data=True):
                if d.get('edge_type') == 'prediction':
                    score = d.get('weight', 0)
                    edge_labels[(u, v)] = f'{score:.3f}'
            
            nx.draw_networkx_edge_labels(G, pos, edge_labels, 
                                       font_size=9, font_family='Arial', 
                                       font_color='#8B0000', font_weight='bold',
                                       bbox=dict(boxstyle="round,pad=0.2", 
                                               facecolor='white', 
                                               edgecolor='#FF4444', 
                                               alpha=0.8, linewidth=0.5), ax=ax)
        
        # 创建图例
        legend_elements = []
        if prediction_edges:
            legend_elements.append(plt.Line2D([0], [0], color='#FF4444', lw=2.5, 
                                            label=f'Prediction (>{threshold})'))
        if ppi_edges:
            legend_elements.append(plt.Line2D([0], [0], color='#4444FF', lw=2, 
                                            linestyle='--', label='PPI Interaction'))
        if protease_nodes:
            legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', 
                                            markerfacecolor='#FF6B6B', markersize=15,
                                            markeredgecolor='#CC0000', markeredgewidth=2,
                                            label='Protease'))
        if position_nodes:
            legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', 
                                            markerfacecolor='#4ECDC4', markersize=12,
                                            markeredgecolor='#008B8B', markeredgewidth=2,
                                            label='Cleavage Site'))
        
        ax.legend(handles=legend_elements, loc='upper left', 
                 bbox_to_anchor=(0.02, 0.98), frameon=True, 
                 fancybox=True, shadow=True, fontsize=12)
        
        # 添加统计信息
        stats_text = f'Nodes: {len(G.nodes())} | Edges: {len(G.edges())}'
        if prediction_edges:
            stats_text += f'\nPrediction edges: {len(prediction_edges)}'
        if ppi_edges:
            stats_text += f'\nPPI edges: {len(ppi_edges)}'
        
        ax.text(0.02, 0.02, stats_text, transform=ax.transAxes, 
               fontsize=11, fontfamily='Arial', color='#666666',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='#F8F9FA', 
                        edgecolor='#CCCCCC', alpha=0.8))
        
        ax.set_title('Interactive Network Plot - Use mouse to zoom and pan', 
                    fontsize=14, fontfamily='Arial', color='#2C3E50', pad=20)
        ax.axis('off')
        
        # 启用交互功能
        plt.tight_layout()
        
        # 显示交互式窗口
        plt.show()
        
        self.textBrowser_status.setText("\nInteractive plot window opened. Use mouse to zoom and pan.")
        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def save_network_plot(self):
        """Save the current network plot to file"""
        # 检查控件是否存在
        if not hasattr(self, 'lineEdit_threshold') or self.lineEdit_threshold is None:
            self.textBrowser_status.setText("\nError: Plot controls not initialized. Please load data first.")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            return
        
        try:
            # 获取当前阈值
            threshold = float(self.lineEdit_threshold.text())
        except ValueError:
            threshold = 0.5
            if self.lineEdit_threshold is not None:
                self.lineEdit_threshold.setText("0.5")
        
        # 检查是否有数据
        if not hasattr(self, 'data_with_preds') or self.data_with_preds.empty:
            self.textBrowser_status.setText("\nError: No prediction data available. Please run prediction first.")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            return
        
        try:
            # 打开文件保存对话框
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save Network Plot",
                f"network_plot_threshold_{threshold}.png",
                "PNG Files (*.png);;JPEG Files (*.jpg);;PDF Files (*.pdf);;SVG Files (*.svg);;All Files (*)"
            )
            
            if file_path:
                # 获取当前筛选的数据用于绘图
                plot_data = self.get_current_filtered_data()
                
                # 创建网络图
                G = nx.Graph()
                
                # 加载数据
                merops_to_uniprot = self.load_merops_uniprot_mapping()
                ppi_matrix = self.load_protease_ppi()
                
                # 添加节点和边
                self.add_nodes_and_edges(G, plot_data, threshold, merops_to_uniprot, ppi_matrix)
                
                if len(G.nodes()) == 0:
                    self.textBrowser_status.setText("\nNo nodes to save.")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    return
                
                # 创建高质量图形
                self.create_high_quality_plot(G, threshold, file_path)
                
                self.textBrowser_status.setText(f"\nNetwork plot saved successfully to: {file_path}")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                
        except Exception as e:
            self.textBrowser_status.setText(f"\nError saving plot: {str(e)}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def create_high_quality_plot(self, G, threshold, file_path):
        """Create high-quality plot for saving"""
        # 设置matplotlib参数
        plt.rcParams['font.family'] = 'Arial'
        plt.rcParams['font.size'] = 14
        
        # 创建图形
        fig, ax = plt.subplots(figsize=(20, 16))
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        
        # 使用spring布局
        pos = nx.spring_layout(G, k=2, iterations=100, seed=42)
        
        # 分离不同类型的节点和边
        protease_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'protease']
        position_nodes = [n for n, d in G.nodes(data=True) if d.get('node_type') == 'protein_position']
        prediction_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('edge_type') == 'prediction']
        ppi_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get('edge_type') == 'ppi']
        
        # 绘制边
        if prediction_edges:
            nx.draw_networkx_edges(G, pos, edgelist=prediction_edges, 
                                 edge_color='#FF4444', alpha=0.7, width=3, 
                                 style='-', connectionstyle="arc3,rad=0.1", ax=ax)
        
        if ppi_edges:
            nx.draw_networkx_edges(G, pos, edgelist=ppi_edges, 
                                 edge_color='#4444FF', alpha=0.6, width=2.5, 
                                 style='--', connectionstyle="arc3,rad=0.2", ax=ax)
        
        # 绘制节点
        if protease_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=protease_nodes, 
                                 node_color='#FF6B6B', node_size=1000, 
                                 alpha=0.9, edgecolors='#CC0000', linewidths=3, ax=ax)
        
        if position_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=position_nodes, 
                                 node_color='#4ECDC4', node_size=600, 
                                 alpha=0.9, edgecolors='#008B8B', linewidths=3, ax=ax)
        
        # 添加标签
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', 
                               font_family='Arial', font_color='#2C3E50', ax=ax)
        
        # 为预测边添加Pre_Score标签
        if prediction_edges:
            edge_labels = {}
            for u, v, d in G.edges(data=True):
                if d.get('edge_type') == 'prediction':
                    score = d.get('weight', 0)
                    edge_labels[(u, v)] = f'{score:.3f}'
            
            nx.draw_networkx_edge_labels(G, pos, edge_labels, 
                                       font_size=10, font_family='Arial', 
                                       font_color='#8B0000', font_weight='bold',
                                       bbox=dict(boxstyle="round,pad=0.3", 
                                               facecolor='white', 
                                               edgecolor='#FF4444', 
                                               alpha=0.9, linewidth=1), ax=ax)
        
        # 创建图例
        legend_elements = []
        if prediction_edges:
            legend_elements.append(plt.Line2D([0], [0], color='#FF4444', lw=3, 
                                            label=f'Prediction (>{threshold})'))
        if ppi_edges:
            legend_elements.append(plt.Line2D([0], [0], color='#4444FF', lw=2.5, 
                                            linestyle='--', label='PPI Interaction'))
        if protease_nodes:
            legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', 
                                            markerfacecolor='#FF6B6B', markersize=18,
                                            markeredgecolor='#CC0000', markeredgewidth=3,
                                            label='Protease'))
        if position_nodes:
            legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', 
                                            markerfacecolor='#4ECDC4', markersize=15,
                                            markeredgecolor='#008B8B', markeredgewidth=3,
                                            label='Cleavage Site'))
        
        legend = ax.legend(handles=legend_elements, loc='upper left', 
                          bbox_to_anchor=(0.02, 0.98), frameon=True, 
                          fancybox=True, shadow=True, fontsize=14)
        legend.get_frame().set_facecolor('#F8F9FA')
        
        # 添加统计信息
        stats_text = f'Nodes: {len(G.nodes())} | Edges: {len(G.edges())}'
        if prediction_edges:
            stats_text += f'\nPrediction edges: {len(prediction_edges)}'
        if ppi_edges:
            stats_text += f'\nPPI edges: {len(ppi_edges)}'
        
        ax.text(0.02, 0.02, stats_text, transform=ax.transAxes, 
               fontsize=12, fontfamily='Arial', color='#666666',
               bbox=dict(boxstyle="round,pad=0.4", facecolor='#F8F9FA', 
                        edgecolor='#CCCCCC', alpha=0.9))
        
        # 设置标题
        ax.set_title(f'Protease-Cleavage Site Interaction Network\n(Threshold: {threshold})', 
                    fontsize=18, fontweight='bold', fontfamily='Arial', 
                    color='#2C3E50', pad=30)
        
        ax.axis('off')
        plt.tight_layout()
        
        # 保存文件
        plt.savefig(file_path, dpi=300, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        
        # 清理
        plt.close()
    
    def save_table_data(self):
        """Save current table data to file"""
        # 检查是否有数据
        if not hasattr(self, 'data_with_preds') or self.data_with_preds.empty:
            self.textBrowser_status.setText("\nError: No prediction data available. Please run prediction first.")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            return
        
        try:
            # 获取当前筛选的数据
            filtered_data = self.get_current_filtered_data()
            
            if filtered_data.empty:
                self.textBrowser_status.setText("\nNo data to save after filtering.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return
            
            # 打开文件保存对话框
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save Table Data",
                "prediction_results.csv",
                "CSV Files (*.csv);;Excel Files (*.xlsx);;TSV Files (*.tsv);;All Files (*)"
            )
            
            if file_path:
                # 根据文件扩展名选择保存格式
                if file_path.lower().endswith('.xlsx'):
                    # 保存为Excel格式
                    filtered_data.to_excel(file_path, index=False, engine='openpyxl')
                    self.textBrowser_status.setText(f"\nTable data saved successfully to Excel file: {file_path}")
                elif file_path.lower().endswith('.tsv'):
                    # 保存为TSV格式
                    filtered_data.to_csv(file_path, sep='\t', index=False)
                    self.textBrowser_status.setText(f"\nTable data saved successfully to TSV file: {file_path}")
                else:
                    # 默认保存为CSV格式
                    filtered_data.to_csv(file_path, index=False)
                    self.textBrowser_status.setText(f"\nTable data saved successfully to CSV file: {file_path}")
                
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                
        except Exception as e:
            self.textBrowser_status.setText(f"\nError saving table data: {str(e)}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def on_tab_changed(self, index):
        """Handle tab change events"""
        if index == 1:  # Plot tab (index 1)
            # 当切换到Plot页面时，自动绘制网络图
            if hasattr(self, 'data_with_preds') and self.data_with_preds is not None and not self.data_with_preds.empty:
                if hasattr(self, 'lineEdit_threshold') and self.lineEdit_threshold is not None:
                    self.textBrowser_status.setText("\nAuto-updating network plot...")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    self.update_network_plot()
                else:
                    self.textBrowser_status.setText("\nPlot controls not initialized. Please load data first.")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def visualize_with_3dmol(self):
        """Visualize selected residue and its neighborhood using 3Dmol.js"""
        try:
            # 检查是否有数据
            if not hasattr(self, 'data_with_preds') or self.data_with_preds is None or self.data_with_preds.empty:
                self.textBrowser_status.setText("\nError: No prediction data available. Please run prediction or load result file first.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return
            
            # 检查PDB文件是否存在
            if not hasattr(self, 'pdb_path') or not self.pdb_path or not os.path.exists(self.pdb_path):
                # 如果没有PDB文件，让用户选择
                from PyQt5.QtWidgets import QFileDialog
                pdb_file, _ = QFileDialog.getOpenFileName(
                    self, 
                    "Select PDB File for 3D Visualization", 
                    "", 
                    "PDB files (*.pdb);;All files (*)"
                )
                if not pdb_file:
                    self.textBrowser_status.setText("\nError: PDB file is required for 3D visualization. Please select a PDB file.")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    return
                self.pdb_path = pdb_file
            
            # 获取当前筛选的数据
            plot_data = self.get_current_filtered_data()
            if plot_data.empty:
                self.textBrowser_status.setText("\nError: No data to visualize. Please adjust filter settings.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return
            
            # 检查是否有Position列
            if 'Position' not in plot_data.columns:
                self.textBrowser_status.setText("\nError: Position column not found in data.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return
            
            # 获取唯一的残基位置
            positions = plot_data['Position'].unique()
            if len(positions) == 0:
                self.textBrowser_status.setText("\nError: No valid positions found in data.")
                self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                return
            
            # 让用户选择要可视化的残基位置
            from PyQt5.QtWidgets import QInputDialog
            position, ok = QInputDialog.getItem(
                self, 
                "Select Residue Position", 
                "Choose a residue position to visualize:",
                [str(pos) for pos in sorted(positions, key=lambda x: int(x) if x.isdigit() else 0)],
                0, 
                False
            )
            
            if not ok or not position:
                return
            
            # 获取链ID
            chain_id = self.LineEdit_chain.text().strip() if hasattr(self, 'LineEdit_chain') else 'A'
            if not chain_id:
                chain_id = 'A'
            
            # 创建3Dmol.js可视化对话框
            self.create_3dmol_visualization_dialog(self.pdb_path, chain_id, position)
            
        except Exception as e:
            self.textBrowser_status.setText(f"\nError in 3Dmol visualization: {str(e)}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def create_3dmol_visualization_dialog(self, pdb_path, chain_id, position):
        """Create 3Dmol.js visualization and open in browser"""
        try:
            # 创建简单的参数设置对话框
            dialog = QDialog(self)
            dialog.setWindowTitle(f"3Dmol.js Visualization - Position {position}")
            dialog.setModal(True)
            dialog.resize(400, 150)
            
            layout = QVBoxLayout()
            
            # 添加控制面板
            control_layout = QHBoxLayout()
            
            # 距离阈值控制
            threshold_label = QLabel("Distance Threshold (Å):")
            threshold_spinbox = QSpinBox()
            threshold_spinbox.setRange(1, 50)
            threshold_spinbox.setValue(10)
            threshold_spinbox.setSuffix(" Å")
            
            control_layout.addWidget(threshold_label)
            control_layout.addWidget(threshold_spinbox)
            control_layout.addStretch()
            
            layout.addLayout(control_layout)
            
            # 添加按钮
            button_layout = QHBoxLayout()
            
            # 在浏览器中打开按钮
            open_browser_button = QPushButton("Open in Browser")
            open_browser_button.setStyleSheet("""
                QPushButton {
                    background-color: #007bff;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
                QPushButton:pressed {
                    background-color: #004085;
                }
            """)
            
            # 保存按钮
            save_button = QPushButton("Save HTML")
            save_button.setStyleSheet("""
                QPushButton {
                    background-color: #28a745;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #218838;
                }
                QPushButton:pressed {
                    background-color: #1e7e34;
                }
            """)
            
            # 取消按钮
            cancel_button = QPushButton("Cancel")
            cancel_button.setStyleSheet("""
                QPushButton {
                    background-color: #6c757d;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #5a6268;
                }
                QPushButton:pressed {
                    background-color: #545b62;
                }
            """)
            
            button_layout.addWidget(open_browser_button)
            button_layout.addWidget(save_button)
            button_layout.addWidget(cancel_button)
            
            layout.addLayout(button_layout)
            
            # 连接信号
            def open_in_browser():
                try:
                    import os
                    import webbrowser
                    
                    # 添加调试信息
                    self.textBrowser_status.setText(f"\nDebug: open_in_browser function called")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    
                    # 使用self.pdb_path而不是参数pdb_path
                    current_pdb_path = self.pdb_path
                    
                    # 添加调试信息
                    self.textBrowser_status.setText(f"\nDebug: Using PDB file: {current_pdb_path}")
                    self.textBrowser_status.setText(f"\nDebug: PDB file exists: {os.path.exists(current_pdb_path) if current_pdb_path else False}")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    
                    # 检查PDB文件是否存在
                    if not os.path.exists(current_pdb_path):
                        self.textBrowser_status.setText(f"\nError: PDB file not found: {current_pdb_path}")
                        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                        return
                    
                    # 生成HTML内容
                    html_content = self.generate_3dmol_html(current_pdb_path, chain_id, position, threshold_spinbox.value())
                    
                    # 保存HTML文件并在浏览器中打开
                    
                    # 获取GUI文件夹路径
                    gui_dir = os.path.dirname(os.path.abspath(__file__))
                    res_dir = os.path.join(gui_dir, "res")
                    
                    # 确保res文件夹存在
                    if not os.path.exists(res_dir):
                        os.makedirs(res_dir)
                    
                    # 使用固定HTML文件名
                    html_filename = "3dmol_visualization.html"
                    html_file = os.path.join(res_dir, html_filename)
                    
                    # 写入HTML文件（覆盖之前的文件）
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    # 打开浏览器
                    # webbrowser.open(f'file://{temp_file}')
                    webbrowser.open(f'file://{html_file}')
                    # 更新状态
                    self.textBrowser_status.setText(f"\nOpening 3Dmol visualization in browser...")
                    # self.textBrowser_status.setText(f"\nTemporary file: {temp_file}")
                    self.textBrowser_status.setText(f"\nFile: {html_file}")
                    self.textBrowser_status.setText(f"\nTarget: Chain {chain_id}, Position {position}")
                    self.textBrowser_status.setText(f"\nDistance threshold: {threshold_spinbox.value()} Å")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                    
                    # 关闭对话框
                    dialog.accept()
                    
                except Exception as e:
                    self.textBrowser_status.setText(f"\nError opening browser: {str(e)}")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            
            def save_html():
                try:
                    import os
                    
                    # 使用self.pdb_path而不是参数pdb_path
                    current_pdb_path = self.pdb_path
                    
                    # 检查PDB文件是否存在
                    if not os.path.exists(current_pdb_path):
                        self.textBrowser_status.setText(f"\nError: PDB file not found: {current_pdb_path}")
                        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                        return
                    
                    # 生成HTML内容
                    html_content = self.generate_3dmol_html(current_pdb_path, chain_id, position, threshold_spinbox.value())
                    
                    # 打开文件保存对话框
                    file_path, _ = QFileDialog.getSaveFileName(
                        dialog, 
                        "Save HTML File", 
                        f"3dmol_visualization_position_{position}_threshold_{threshold_spinbox.value()}.html",
                        "HTML files (*.html)"
                    )
                    if file_path:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(html_content)
                        self.textBrowser_status.setText(f"\n3Dmol.js visualization saved to: {file_path}")
                        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                        
                        # 询问是否在浏览器中打开
                        from PyQt5.QtWidgets import QMessageBox
                        reply = QMessageBox.question(
                            dialog, 
                            'Open in Browser', 
                            f'HTML file saved successfully!\n\nDo you want to open it in your browser now?',
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.Yes
                        )
                        
                        if reply == QMessageBox.Yes:
                            import webbrowser
                            webbrowser.open(f'file://{file_path}')
                            self.textBrowser_status.setText(f"\nOpening saved file in browser...")
                            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
                        
                        dialog.accept()
                        
                except Exception as e:
                    self.textBrowser_status.setText(f"\nError saving HTML: {str(e)}")
                    self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            
            def cancel_dialog():
                dialog.reject()
            
            open_browser_button.clicked.connect(open_in_browser)
            save_button.clicked.connect(save_html)
            cancel_button.clicked.connect(cancel_dialog)
            
            dialog.setLayout(layout)
            dialog.exec_()
            
        except Exception as e:
            self.textBrowser_status.setText(f"\nError creating 3Dmol dialog: {str(e)}")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def generate_3dmol_html(self, pdb_path, chain_id, position, threshold):
        """Generate HTML content with 3Dmol.js visualization - 只显示局部残基"""
        # 读取PDB文件内容
        try:
            with open(pdb_path, 'r') as f:
                pdb_content = f.read()
            print(f"Successfully loaded PDB file: {pdb_path} ({len(pdb_content)} characters)")
        except Exception as e:
            print(f"Failed to load PDB file {pdb_path}: {e}")
            # 使用默认示例PDB内容作为后备
            pdb_content = "ATOM      1  N   ALA A   1      20.154  16.967  23.862  1.00 11.18           N  \nATOM      2  CA  ALA A   1      19.030  16.053  23.456  1.00 10.53           C  \n"
        
        # 获取当前脚本目录，用于构建本地文件路径
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        local_3dmol_path = os.path.join(script_dir, 'static', 'js', '3Dmol-min.js')
        
        # 尝试读取本地3Dmol.js文件内容
        local_3dmol_content = ""
        try:
            with open(local_3dmol_path, 'r', encoding='utf-8') as f:
                local_3dmol_content = f.read()
            print(f"Successfully loaded local 3Dmol.js ({len(local_3dmol_content)} characters)")
        except Exception as e:
            print(f"Failed to load local 3Dmol.js: {e}")
            local_3dmol_content = ""
        
        # 如果有本地3Dmol.js文件，直接嵌入；否则使用CDN
        if local_3dmol_content:
            script_tag = f'<script>{local_3dmol_content}</script>'
            load_script = '''
// 直接使用内嵌的3Dmol.js
window.onload = function() {
    document.getElementById('loading').innerHTML = '3Dmol.js loaded successfully.';
    
    // 等待3Dmol.js完全初始化
    let waitCount = 0;
    const maxWaitCount = 100; // 最多等待5秒 (100 * 50ms)
    
    function waitFor3Dmol() {
        if (typeof $3Dmol !== 'undefined' && $3Dmol.createViewer) {
            console.log('3Dmol.js is ready');
            init();
        } else if (waitCount < maxWaitCount) {
            waitCount++;
            console.log('Waiting for 3Dmol.js to initialize... (' + waitCount + '/' + maxWaitCount + ')');
            setTimeout(waitFor3Dmol, 50);
        } else {
            console.error('3Dmol.js failed to initialize after maximum wait time');
            document.getElementById('loading').innerHTML = 'Error: 3Dmol.js failed to initialize properly.';
        }
    }
    
    // 延迟启动，确保3Dmol.js完全加载
    setTimeout(waitFor3Dmol, 200);
};
            '''
        else:
            script_tag = '<script src="https://3Dmol.org/build/3Dmol-min.js" onerror="loadBackup3Dmol()"></script>'
            load_script = '''
        // 检查网络连接
        function checkNetworkConnection() {
            return new Promise((resolve) => {
                const img = new Image();
                img.onload = () => resolve(true);
                img.onerror = () => resolve(false);
                img.src = 'https://3Dmol.org/favicon.ico?t=' + Date.now();
                setTimeout(() => resolve(false), 3000);
            });
        }
        
        // 尝试多个CDN源加载3Dmol.js
        async function load3Dmol() {
            // 首先检查网络连接
            const hasNetwork = await checkNetworkConnection();
            if (!hasNetwork) {
                document.getElementById('loading').innerHTML = 'No internet connection detected. Using fallback mode.';
                tryLocalFallback();
                return;
            }
            
            const cdnSources = [
                'https://3Dmol.org/build/3Dmol-min.js',
                'https://cdn.jsdelivr.net/npm/3dmol@2.1.0/build/3Dmol-min.js',
                'https://unpkg.com/3dmol@2.1.0/build/3Dmol-min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.1.0/3Dmol-min.js'
            ];
            
            let currentIndex = 0;
            
            function tryNextCDN() {
                if (currentIndex >= cdnSources.length) {
                    // 尝试使用本地备用方案
                    tryLocalFallback();
                    return;
                }
                
                const script = document.createElement('script');
                script.src = cdnSources[currentIndex];
                script.onload = function() {
                    console.log('3Dmol.js loaded successfully from:', cdnSources[currentIndex]);
                    
                    // 等待3Dmol.js完全初始化
                    let waitCount = 0;
                    const maxWaitCount = 100; // 最多等待5秒 (100 * 50ms)
                    
                    function waitFor3Dmol() {
                        if (typeof $3Dmol !== 'undefined' && $3Dmol.createViewer) {
                            console.log('3Dmol.js is ready');
                            document.getElementById('loading').innerHTML = '3Dmol.js loaded successfully.';
                            init();
                        } else if (waitCount < maxWaitCount) {
                            waitCount++;
                            console.log('Waiting for 3Dmol.js to initialize... (' + waitCount + '/' + maxWaitCount + ')');
                            setTimeout(waitFor3Dmol, 50);
                        } else {
                            console.error('3Dmol.js failed to initialize after maximum wait time');
                            document.getElementById('loading').innerHTML = 'Error: 3Dmol.js failed to initialize properly.';
                        }
                    }
                    
                    // 延迟启动，确保3Dmol.js完全加载
                    setTimeout(waitFor3Dmol, 200);
                };
                script.onerror = function() {
                    console.log('Failed to load from:', cdnSources[currentIndex]);
                    currentIndex++;
                    tryNextCDN();
                };
                document.head.appendChild(script);
            }
            
            tryNextCDN();
        }
        
        function tryLocalFallback() {
            console.log('Trying local 3Dmol.js...');
            
            // 尝试加载本地3Dmol.js文件
            const script = document.createElement('script');
            script.src = './static/js/3Dmol-min.js';
            script.onload = function() {
                console.log('Local 3Dmol.js loaded successfully');
                document.getElementById('loading').innerHTML = 'Local 3Dmol.js loaded successfully.';
                
                // 等待3Dmol.js完全初始化
                let waitCount = 0;
                const maxWaitCount = 100; // 最多等待5秒 (100 * 50ms)
                
                function waitFor3Dmol() {
                    if (typeof $3Dmol !== 'undefined' && $3Dmol.createViewer) {
                        console.log('Local 3Dmol.js is ready');
                        init();
                    } else if (waitCount < maxWaitCount) {
                        waitCount++;
                        console.log('Waiting for local 3Dmol.js to initialize... (' + waitCount + '/' + maxWaitCount + ')');
                        setTimeout(waitFor3Dmol, 50);
                    } else {
                        console.error('Local 3Dmol.js failed to initialize after maximum wait time');
                        document.getElementById('loading').innerHTML = 'Error: Local 3Dmol.js failed to initialize properly.';
                    }
                }
                
                // 延迟启动，确保3Dmol.js完全加载
                setTimeout(waitFor3Dmol, 200);
            };
            script.onerror = function() {
                console.log('Local 3Dmol.js not found, using simplified fallback');
                trySimplifiedFallback();
            };
            document.head.appendChild(script);
        }
        
        function trySimplifiedFallback() {
            // 创建一个简化的3Dmol.js替代方案
            console.log('Using simplified fallback...');
            
            // 创建一个简化的3Dmol对象
            window.$3Dmol = {
                createViewer: function(element, options) {
                    return {
                        addModel: function(data, format) {
                            console.log('Fallback: addModel called');
                        },
                        setStyle: function(selection, style) {
                            console.log('Fallback: setStyle called');
                        },
                        render: function() {
                            console.log('Fallback: render called');
                        },
                        zoomTo: function(selection) {
                            console.log('Fallback: zoomTo called');
                        },
                        getModel: function() {
                            return {
                                selectedAtoms: function(criteria) {
                                    return [];
                                }
                            };
                        },
                        addSurface: function(type, options, selection) {
                            console.log('Fallback: addSurface called');
                        },
                        removeAllSurfaces: function() {
                            console.log('Fallback: removeAllSurfaces called');
                        },
                        addLabel: function(text, options) {
                            console.log('Fallback: addLabel called');
                        },
                        removeAllLabels: function() {
                            console.log('Fallback: removeAllLabels called');
                        }
                    };
                },
                SurfaceType: {
                    VDW: 'VDW'
                },
                rasmolElementColors: {}
            };
            
            // 显示备用模式信息
            document.getElementById('loading').innerHTML = 'Using simplified fallback mode - 3Dmol.js not available. Some features may be limited.';
            
            // 延迟初始化
            setTimeout(function() {
                init();
            }, 500);
        }
        
        // 页面加载后开始加载3Dmol.js
        window.onload = function() {
            load3Dmol();
        };
            '''
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>3Dmol Local Residue Visualization - Chain {chain_id}, Position {position}</title>
    {script_tag}
    <script>
        {load_script}
    </script>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            margin: 0 0 10px 0;
            font-size: 24px;
        }}
        .header p {{
            margin: 5px 0;
            opacity: 0.9;
        }}
        #viewer {{
            width: 100%;
            height: 700px;
            border: 2px solid #dee2e6;
            border-radius: 10px;
            position: relative;
            overflow: hidden;
            background: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .controls {{
            margin: 15px 0;
            padding: 15px;
            background: white;
            border-radius: 10px;
            border: 1px solid #dee2e6;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            align-items: center;
        }}
        .controls button {{
            margin: 2px;
            padding: 10px 16px;
            background: linear-gradient(135deg, #007bff, #0056b3);
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .controls button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
        .controls button:active {{
            transform: translateY(0);
        }}
        .info {{
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 4px solid #28a745;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .stats {{
            background: linear-gradient(135deg, #e3f2fd, #bbdefb);
            padding: 15px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 4px solid #2196F3;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .loading {{
            text-align: center;
            padding: 40px;
            color: #666;
            font-size: 16px;
        }}
        .instructions {{
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 4px solid #ffc107;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .instructions ul {{
            margin: 10px 0;
            padding-left: 20px;
        }}
        .instructions li {{
            margin: 5px 0;
        }}
        .sequence-panel {{
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border: 1px solid #dee2e6;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .sequence-panel h3 {{
            margin: 0 0 15px 0;
            color: #2C3E50;
            font-size: 18px;
            font-weight: bold;
        }}
        .sequence-container {{
            width: 100%;
        }}
        .sequence-info {{
            display: flex;
            gap: 20px;
            margin-bottom: 15px;
            font-size: 14px;
            color: #666;
        }}
        .sequence-info span {{
            display: flex;
            align-items: center;
        }}
        .sequence-display {{
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 15px;
            overflow-x: auto;
        }}
        .sequence-text {{
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.8;
            white-space: pre-wrap;
            user-select: text;
            letter-spacing: 1px;
            word-break: break-all;
        }}
        .residue {{
            display: inline-block;
            padding: 3px 6px;
            margin: 1px;
            border-radius: 4px;
            font-weight: bold;
            min-width: 24px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 14px;
            line-height: 1.2;
        }}
        .residue:hover {{
            transform: scale(1.1);
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }}
        .residue.target {{
            background-color: #dc3545;
            color: white;
            border: 2px solid #c82333;
        }}
        .residue.local {{
            background-color: #ffc107;
            color: #212529;
            border: 1px solid #e0a800;
        }}
        .residue.other {{
            background-color: #e9ecef;
            color: #6c757d;
            border: 1px solid #ced4da;
        }}
        .sequence-legend {{
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 12px;
        }}
        .legend-color {{
            width: 16px;
            height: 16px;
            border-radius: 3px;
            border: 1px solid #ccc;
        }}
        .legend-color.target {{
            background-color: #dc3545;
        }}
        .legend-color.local {{
            background-color: #ffc107;
        }}
        .legend-color.other {{
            background-color: #e9ecef;
        }}
        .line-number {{
            color: #6c757d;
            font-size: 12px;
            margin-right: 10px;
            font-weight: normal;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>3D Protein Structure Visualization</h1>
        <p><strong>Target Residue:</strong> Chain {chain_id}, Position {position}</p>
        <p><strong>Distance Threshold:</strong> {threshold} Å (based on Ca distance)</p>
        <p><strong>PDB File:</strong> {os.path.basename(pdb_path)}</p>
    </div>
    
    <div class="controls">
        <button onclick="resetView()">Reset View</button>
        <button onclick="toggleSurface()">Toggle Surface</button>
        <button onclick="toggleLabels()">Toggle Labels</button>
        <button onclick="centerOnTarget()">Center on Target</button>
        <button onclick="showAllChains()">Show All Chains</button>
        <button onclick="showLocalOnly()">Show Local Only</button>
        <button onclick="toggleDisplayMode()">Toggle Display Mode</button>
    </div>
    
    <div id="viewer">
        <div class="loading" id="loading">Loading 3Dmol.js...</div>
    </div>
    
    <div class="stats" id="stats">
        <strong>Statistics:</strong><br>
        <span id="residueCount">Calculating...</span>
    </div>
    
    <div class="sequence-panel">
        <h3>Protein Sequence</h3>
        <div class="sequence-container">
            <div class="sequence-info">
                <span>Chain: <strong id="chainInfo">{chain_id}</strong></span>
                <span>Total Residues: <strong id="totalResidues">Calculating...</strong></span>
                <span>Local Residues: <strong id="localResidues">Calculating...</strong></span>
            </div>
            <div class="sequence-display" id="sequenceDisplay">
                <div class="sequence-text" id="sequenceText">Loading sequence...</div>
            </div>
            <div class="sequence-legend">
                <div class="legend-item">
                    <span class="legend-color target"></span>
                    <span>Target Residue</span>
                </div>
                <div class="legend-item">
                    <span class="legend-color local"></span>
                    <span>Local Residues</span>
                </div>
                <div class="legend-item">
                    <span class="legend-color other"></span>
                    <span>Other Residues</span>
                </div>
            </div>
        </div>
    </div>
    
    <div class="instructions">
        <strong>Instructions:</strong>
        <ul>
            <li><strong>Mouse Controls:</strong> Left click + drag to rotate, right click + drag to pan, scroll to zoom</li>
            <li><strong>Target Residue:</strong> Slightly thicker sticks/spheres (Position {position})</li>
            <li><strong>Local Residues:</strong> Medium sticks/spheres within {threshold}Å</li>
            <li><strong>CPK Colorscheme:</strong> Carbon (Cyan), Nitrogen (Blue), Oxygen (Red), Sulfur (Yellow), Hydrogen (White)</li>
            <li><strong>Display Modes:</strong> Switch between stick, sphere, and cartoon representations</li>
        </ul>
    </div>

    <script>
        let viewer;
        let surfaceVisible = false;
        let labelsVisible = true;
        let showAllChainsMode = false;
        let displayMode = 'stick'; // 'stick', 'sphere', 'cartoon'
        let localResidues = new Set();
        let targetResidue = {int(position)};
        let chainId = '{chain_id}';
        let threshold = {float(threshold)};
        
        function init() {{
            try {{
                // 检查3Dmol.js是否加载成功
                if (typeof $3Dmol === 'undefined') {{
                    document.getElementById('loading').innerHTML = 'Error: 3Dmol.js failed to load. Please check your internet connection.';
                    return;
                }}
                
                // 隐藏加载提示
                const loadingDiv = document.getElementById('loading');
                if (loadingDiv) {{
                    loadingDiv.style.display = 'none';
                }}
                
                // 创建viewer，确保不会影响其他元素
                const viewerElement = document.getElementById('viewer');
                viewer = $3Dmol.createViewer(viewerElement, {{
                    defaultcolors: $3Dmol.rasmolElementColors
                }});
            
            // Load PDB data
            const pdbData = `{pdb_content}`;
            viewer.addModel(pdbData, "pdb");
            
                // 计算局部残基
                calculateLocalResidues();
                
                // 设置初始显示模式
                showLocalOnly();
                
                // 添加标签
                addLabels();
                
                // 更新统计信息
                updateStats();
                
                // 生成蛋白质序列
                generateProteinSequence();
                
                // 居中显示
                centerOnTarget();
                
                console.log('3Dmol.js visualization initialized successfully');
                
                // 确保按钮区域可见
                const controlsDiv = document.querySelector('.controls');
                if (controlsDiv) {{
                    controlsDiv.style.display = 'block';
                    controlsDiv.style.visibility = 'visible';
                    controlsDiv.style.position = 'relative';
                    controlsDiv.style.zIndex = '1000';
                    console.log('Controls div is visible');
                }} else {{
                    console.error('Controls div not found!');
                }}
                
                // 设置定时器，定期检查按钮可见性
                setInterval(function() {{
                    ensureControlsVisible();
                }}, 1000);
                
            }} catch (error) {{
                console.error('Error initializing 3Dmol.js:', error);
                const loadingDiv = document.getElementById('loading');
                if (loadingDiv) {{
                    loadingDiv.innerHTML = 'Error initializing visualization: ' + error.message;
                }}
            }}
        }}
        
        function calculateLocalResidues() {{
            // 获取目标残基的α碳原子坐标
            const targetAtoms = viewer.getModel().selectedAtoms({{chain: chainId, resi: targetResidue, atom: 'CA'}});
            if (targetAtoms.length === 0) {{
                console.log('Target residue α-carbon not found');
                return;
            }}
            
            const targetPos = targetAtoms[0];
            localResidues.clear();
            localResidues.add(targetResidue); // 添加目标残基
            
            // 遍历所有残基，计算与目标残基的距离
            const allAtoms = viewer.getModel().selectedAtoms({{chain: chainId, atom: 'CA'}});
            
            allAtoms.forEach(atom => {{
                if (atom.resi !== targetResidue) {{
                    const distance = Math.sqrt(
                        Math.pow(atom.x - targetPos.x, 2) +
                        Math.pow(atom.y - targetPos.y, 2) +
                        Math.pow(atom.z - targetPos.z, 2)
                    );
                    
                    if (distance <= threshold) {{
                        localResidues.add(atom.resi);
                    }}
                }}
            }});
            
            console.log(`Found ${{localResidues.size}} local residues:`, Array.from(localResidues).sort((a, b) => a - b));
        }}
        
        function showLocalOnly() {{
            showAllChainsMode = false;
            
            // 隐藏所有残基
            viewer.setStyle({{}}, {{}});
            
            // 只显示局部残基
            const localResidueList = Array.from(localResidues);
            
            // 根据显示模式设置样式
            let baseStyle = {{}};
            let targetStyle = {{}};
            let nearbyStyle = {{}};
            
            if (displayMode === 'stick') {{
                // Stick模式 - 使用CPK颜色方案，碳原子为青色
                baseStyle = {{
                    stick: {{
                        radius: 0.3,
                        colorscheme: 'CPK',
                        opacity: 0.8
                    }}
                }};
                // 目标残基使用更粗的stick，保持CPK颜色
                targetStyle = {{
                    stick: {{
                        radius: 0.5,
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                // 范围内残基使用中等粗细的stick，保持CPK颜色
                nearbyStyle = {{
                    stick: {{
                        radius: 0.4,
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }} else if (displayMode === 'sphere') {{
                // Sphere模式 - 使用CPK颜色方案，碳原子为青色
                baseStyle = {{
                    sphere: {{
                        radius: 0.4,
                        colorscheme: 'CPK',
                        opacity: 0.8
                    }}
                }};
                // 目标残基使用更大的sphere，保持CPK颜色
                targetStyle = {{
                    sphere: {{
                        radius: 0.6,
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                // 范围内残基使用中等大小的sphere，保持CPK颜色
                nearbyStyle = {{
                    sphere: {{
                        radius: 0.5,
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }} else if (displayMode === 'cartoon') {{
                // Cartoon模式 - 使用CPK颜色方案
                baseStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 0.8
                    }}
                }};
                targetStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                nearbyStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }}
            
            // 应用基础样式
            viewer.setStyle({{chain: chainId, resi: localResidueList}}, baseStyle);
            
            // 高亮目标残基
            viewer.setStyle({{chain: chainId, resi: targetResidue}}, targetStyle);
            
            // 高亮范围内的其他残基
            const nearbyResidues = localResidueList.filter(resi => resi !== targetResidue);
            if (nearbyResidues.length > 0) {{
                viewer.setStyle({{chain: chainId, resi: nearbyResidues}}, nearbyStyle);
            }}
            
            // α碳原子使用标准CPK颜色方案，不再额外设置颜色
            
            viewer.render();
            // 确保按钮在渲染后仍然可见
            ensureControlsVisible();
            
            // 更新序列显示
            generateProteinSequence();
        }}
        
        function showAllChains() {{
            showAllChainsMode = true;
            
            // 显示所有链 - 使用cartoon形式作为背景
            viewer.setStyle({{}}, {{cartoon: {{color: 'spectrum', opacity: 0.3}}}});
            
            // 根据显示模式设置目标链样式
            let chainStyle = {{}};
            let targetStyle = {{}};
            let nearbyStyle = {{}};
            
            if (displayMode === 'stick') {{
                // Stick模式 - 使用CPK颜色方案，碳原子为青色
                chainStyle = {{
                    stick: {{
                        radius: 0.2,
                        colorscheme: 'CPK',
                        opacity: 0.6
                    }}
                }};
                // 目标残基使用更粗的stick，保持CPK颜色
                targetStyle = {{
                    stick: {{
                        radius: 0.5,
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                // 范围内残基使用中等粗细的stick，保持CPK颜色
                nearbyStyle = {{
                    stick: {{
                        radius: 0.4,
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }} else if (displayMode === 'sphere') {{
                // Sphere模式 - 使用CPK颜色方案，碳原子为青色
                chainStyle = {{
                    sphere: {{
                        radius: 0.3,
                        colorscheme: 'CPK',
                        opacity: 0.6
                    }}
                }};
                // 目标残基使用更大的sphere，保持CPK颜色
                targetStyle = {{
                    sphere: {{
                        radius: 0.6,
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                // 范围内残基使用中等大小的sphere，保持CPK颜色
                nearbyStyle = {{
                    sphere: {{
                        radius: 0.5,
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }} else if (displayMode === 'cartoon') {{
                // Cartoon模式 - 使用CPK颜色方案
                chainStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 0.6
                    }}
                }};
                targetStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 1.0
                    }}
                }};
                nearbyStyle = {{
                    cartoon: {{
                        colorscheme: 'CPK',
                        opacity: 0.9
                    }}
                }};
            }}
            
            // 高亮目标链
            viewer.setStyle({{chain: chainId}}, chainStyle);
            
            // 高亮目标残基
            viewer.setStyle({{chain: chainId, resi: targetResidue}}, targetStyle);
            
            // 高亮范围内的残基
            const nearbyResidues = Array.from(localResidues).filter(resi => resi !== targetResidue);
            if (nearbyResidues.length > 0) {{
                viewer.setStyle({{chain: chainId, resi: nearbyResidues}}, nearbyStyle);
            }}
            
            // α碳原子使用标准CPK颜色方案，不再额外设置颜色
            
            viewer.render();
            // 确保按钮在渲染后仍然可见
            ensureControlsVisible();
            
            // 更新序列显示
            generateProteinSequence();
        }}
        
        function addLabels() {{
            try {{
                // 先移除所有标签
                viewer.removeAllLabels();
                
            if (labelsVisible) {{
                    console.log('Adding labels...');
                    console.log('localResidues size:', localResidues.size);
                    console.log('targetResidue:', targetResidue);
                    console.log('chainId:', chainId);
                    
                    // 确保localResidues不为空
                    if (localResidues.size === 0) {{
                        console.log('localResidues is empty, recalculating...');
                        calculateLocalResidues();
                    }}
                    
                    // 获取残基的氨基酸字母
                    function getResidueName(residueNumber) {{
                        try {{
                            const atoms = viewer.getModel().selectedAtoms({{chain: chainId, resi: residueNumber}});
                            if (atoms.length > 0) {{
                                return atoms[0].resn; // 获取残基名称
                            }}
                        }} catch (error) {{
                            console.error('Error getting residue name for', residueNumber, ':', error);
                        }}
                        return 'UNK'; // 如果无法获取，返回未知
                    }}
                    
                    // 方法1: 尝试使用addResLabels (3Dmol.js内置方法)
                    try {{
                        console.log('Trying addResLabels method...');
                        viewer.addResLabels({{chain: chainId, resi: Array.from(localResidues)}}, {{
                            backgroundColor: 'yellow',
                            backgroundOpacity: 0.7,
                            fontColor: 'black',
                            fontSize: 12
                        }});
                        console.log('addResLabels method successful');
                    }} catch (error) {{
                        console.log('addResLabels failed, trying individual labels:', error);
                        
                        // 方法2: 使用addLabel为每个残基添加标签
                        const targetResidueName = getResidueName(targetResidue);
                        console.log('Adding target residue label:', targetResidueName + targetResidue);
                        
                        viewer.addLabel(`${{targetResidueName}}${{targetResidue}}`, {{
                            position: {{chain: chainId, resi: targetResidue}}, 
                            backgroundColor: 'red', 
                            backgroundOpacity: 0.8, 
                            fontColor: 'white',
                            fontSize: 14
                        }});
                        
                        // 为范围内的其他残基添加标签
                        const nearbyResidues = Array.from(localResidues).filter(resi => resi !== targetResidue);
                        console.log('nearbyResidues:', nearbyResidues);
                        
                        nearbyResidues.forEach(resi => {{
                            const residueName = getResidueName(resi);
                            console.log('Adding nearby residue label:', residueName + resi);
                            
                            viewer.addLabel(`${{residueName}}${{resi}}`, {{
                                position: {{chain: chainId, resi: resi}}, 
                                backgroundColor: 'yellow', 
                                backgroundOpacity: 0.7, 
                                fontColor: 'black',
                                fontSize: 12
                            }});
                        }});
                    }}
                    
                    console.log('Labels added successfully');
                }} else {{
                    console.log('Labels hidden');
                }}
            }} catch (error) {{
                console.error('Error in addLabels:', error);
            }}
        }}
        
        function updateStats() {{
            const totalResidues = localResidues.size;
            const nearbyResidues = totalResidues - 1; // 减去目标残基
            
            document.getElementById('residueCount').innerHTML = `
                Total Local Residues: ${{totalResidues}}<br>
                Target Residue: ${{targetResidue}}<br>
                Nearby Residues: ${{nearbyResidues}}<br>
                Distance Threshold: ${{threshold}} Å
            `;
        }}
        
        function generateProteinSequence() {{
            try {{
                console.log('Generating protein sequence...');
                
                // 获取所有残基信息
                const allAtoms = viewer.getModel().selectedAtoms({{chain: chainId}});
                const residues = new Map();
                
                // 按残基编号分组
                allAtoms.forEach(atom => {{
                    if (!residues.has(atom.resi)) {{
                        residues.set(atom.resi, {{
                            resi: atom.resi,
                            resn: atom.resn,
                            chain: atom.chain
                        }});
                    }}
                }});
                
                // 转换为数组并排序
                const sortedResidues = Array.from(residues.values()).sort((a, b) => a.resi - b.resi);
                console.log('Found', sortedResidues.length, 'residues');
                
                // 更新统计信息
                document.getElementById('totalResidues').textContent = sortedResidues.length;
                document.getElementById('localResidues').textContent = localResidues.size;
                
                // 生成序列HTML - 使用单字母形式
                let sequenceHTML = '';
                const residuesPerLine = 60; // 每行显示60个残基
                
                sortedResidues.forEach((residue, index) => {{
                    let cssClass = 'other';
                    if (residue.resi === targetResidue) {{
                        cssClass = 'target';
                    }} else if (localResidues.has(residue.resi)) {{
                        cssClass = 'local';
                    }}
                    
                    // 将三字母氨基酸代码转换为单字母
                    const singleLetter = getSingleLetterCode(residue.resn);
                    sequenceHTML += `<span class="residue ${{cssClass}}" data-resi="${{residue.resi}}" title="Residue ${{residue.resn}}${{residue.resi}} (${{singleLetter}})">${{singleLetter}}</span>`;
                    
                    // 每60个残基换行，并添加行号
                    if ((index + 1) % residuesPerLine === 0) {{
                        const lineNumber = Math.floor((index + 1) / residuesPerLine);
                        sequenceHTML += `<br><span class="line-number">${{lineNumber * residuesPerLine + 1}}</span>`;
                    }}
                }});
                
                // 更新序列显示
                document.getElementById('sequenceText').innerHTML = sequenceHTML;
                
                // 添加点击事件
                document.querySelectorAll('.residue').forEach(element => {{
                    element.addEventListener('click', function() {{
                        const resi = parseInt(this.dataset.resi);
                        console.log('Clicked on residue:', resi);
                        // 可以在这里添加点击残基时的操作
                        centerOnResidue(resi);
                    }});
                }});
                
                console.log('Protein sequence generated successfully');
                
            }} catch (error) {{
                console.error('Error generating protein sequence:', error);
                document.getElementById('sequenceText').innerHTML = 'Error loading sequence';
            }}
        }}
        
        function getSingleLetterCode(threeLetterCode) {{
            const aminoAcidMap = {{
                'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C',
                'GLN': 'Q', 'GLU': 'E', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I',
                'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F', 'PRO': 'P',
                'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V',
                'ASX': 'B', 'GLX': 'Z', 'XAA': 'X', 'UNK': 'X'
            }};
            return aminoAcidMap[threeLetterCode.toUpperCase()] || 'X';
        }}
        
        function centerOnResidue(resi) {{
            try {{
                viewer.zoomTo({{chain: chainId, resi: resi}});
            viewer.render();
                console.log('Centered on residue:', resi);
            }} catch (error) {{
                console.error('Error centering on residue:', error);
            }}
        }}
        
        function resetView() {{
            try {{
                if (showAllChainsMode) {{
                    showAllChains();
                }} else {{
                    showLocalOnly();
                }}
            viewer.zoomTo();
            }} catch (error) {{
                console.error('Error in resetView:', error);
            }}
        }}
        
        function toggleSurface() {{
            try {{
            if (surfaceVisible) {{
                viewer.removeAllSurfaces();
                surfaceVisible = false;
            }} else {{
                    // 为局部残基添加VDW表面
                    const localResidueList = Array.from(localResidues);
                    viewer.addSurface($3Dmol.SurfaceType.VDW, {{
                        opacity: 0.4, 
                        color: 'lightblue'
                    }}, {{chain: chainId, resi: localResidueList}});
                surfaceVisible = true;
            }}
            viewer.render();
            }} catch (error) {{
                console.error('Error in toggleSurface:', error);
            }}
        }}
        
        function toggleLabels() {{
            try {{
                console.log('toggleLabels called, current labelsVisible:', labelsVisible);
            labelsVisible = !labelsVisible;
                console.log('toggleLabels called, new labelsVisible:', labelsVisible);
                addLabels();
            viewer.render();
                console.log('toggleLabels completed');
            }} catch (error) {{
                console.error('Error in toggleLabels:', error);
            }}
        }}
        
        function centerOnTarget() {{
            try {{
                viewer.zoomTo({{chain: chainId, resi: targetResidue}});
            viewer.render();
            }} catch (error) {{
                console.error('Error in centerOnTarget:', error);
            }}
        }}
        
        function toggleDisplayMode() {{
            try {{
                // 循环切换显示模式: stick -> sphere -> cartoon -> stick
                if (displayMode === 'stick') {{
                    displayMode = 'sphere';
                }} else if (displayMode === 'sphere') {{
                    displayMode = 'cartoon';
                }} else {{
                    displayMode = 'stick';
                }}
                
                // 重新应用显示模式
                if (showAllChainsMode) {{
                    showAllChains();
                }} else {{
                    showLocalOnly();
                }}
                
                console.log('Display mode changed to:', displayMode);
            }} catch (error) {{
                console.error('Error in toggleDisplayMode:', error);
            }}
        }}
        
        function ensureControlsVisible() {{
            // 强制确保按钮区域可见
            const controlsDiv = document.querySelector('.controls');
            if (controlsDiv) {{
                controlsDiv.style.display = 'block';
                controlsDiv.style.visibility = 'visible';
                controlsDiv.style.position = 'relative';
                controlsDiv.style.zIndex = '1000';
            }}
        }}
        
        // 初始化函数现在由load3Dmol()调用
    </script>
</body>
</html>
"""
        return html_content
    
    def get_current_filtered_data(self):
        """Get currently filtered data based on user selections"""
        if not hasattr(self, 'data_with_preds') or self.data_with_preds is None or self.data_with_preds.empty:
            return pd.DataFrame()
        
        # 检查筛选控件是否存在
        if not hasattr(self, 'comboBox_proteases') or self.comboBox_proteases is None:
            return self.data_with_preds
        if not hasattr(self, 'comboBox_protein_pos') or self.comboBox_protein_pos is None:
            return self.data_with_preds
        
        try:
            # 获取选择的筛选条件
            selected_protease = self.comboBox_proteases.currentText()
            selected_protein_pos = self.comboBox_protein_pos.currentText()
        except RuntimeError:
            # 如果控件已被删除，返回原始数据
            return self.data_with_preds
        
        # 筛选数据
        filtered_data = self.data_with_preds.copy()
        
        if selected_protease != "All":
            filtered_data = filtered_data[filtered_data['Proteases'] == selected_protease]
        
        if selected_protein_pos != "All":
            filtered_data = filtered_data[filtered_data['Protein|position'] == selected_protein_pos]
        
        # 处理数据：创建Position列（与display_data_in_table方法保持一致）
        if 'Protein|position' in filtered_data.columns:
            # 分割Protein|position列
            protein_pos_split = filtered_data['Protein|position'].str.split('|', expand=True)
            if protein_pos_split.shape[1] >= 2:
                filtered_data['Protein'] = protein_pos_split[0]
                filtered_data['Position'] = protein_pos_split[1]
        
        return filtered_data
    
    

                                                                                                
from qt_material import apply_stylesheet
import qdarkstyle
from qdarkstyle.light.palette import LightPalette

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    # apply_stylesheet(app, theme='light_blue.xml')
    # apply_stylesheet(app, theme='dark_teal.xml')
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
    main_ui = MyDesigner()
    main_ui.show()
    # main_ui.showMaximized()
    app.exec_()
