# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadScene.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(848, 599)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(493, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.list_1 = QtWidgets.QListWidget(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.list_1.setFont(font)
        self.list_1.setStyleSheet("")
        self.list_1.setAlternatingRowColors(True)
        self.list_1.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_1.setMovement(QtWidgets.QListView.Static)
        self.list_1.setObjectName("list_1")
        self.gridLayout_3.addWidget(self.list_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.list_2 = QtWidgets.QListWidget(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.list_2.setFont(font)
        self.list_2.setAlternatingRowColors(True)
        self.list_2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_2.setObjectName("list_2")
        self.gridLayout_4.addWidget(self.list_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.list_3 = QtWidgets.QListWidget(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.list_3.setFont(font)
        self.list_3.setAlternatingRowColors(True)
        self.list_3.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_3.setObjectName("list_3")
        self.gridLayout_5.addWidget(self.list_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.list_4 = QtWidgets.QListWidget(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.list_4.setFont(font)
        self.list_4.setAlternatingRowColors(True)
        self.list_4.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_4.setObjectName("list_4")
        self.gridLayout_6.addWidget(self.list_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.list_5 = QtWidgets.QListWidget(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.list_5.setFont(font)
        self.list_5.setAlternatingRowColors(True)
        self.list_5.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_5.setObjectName("list_5")
        self.gridLayout_7.addWidget(self.list_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.list_6 = QtWidgets.QListWidget(self.tab_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.list_6.setFont(font)
        self.list_6.setAlternatingRowColors(True)
        self.list_6.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_6.setObjectName("list_6")
        self.gridLayout_2.addWidget(self.list_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout_9.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(280, 250))
        self.textEdit.setStyleSheet("background-color:transparent;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.downloadBtn = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.downloadBtn.setFont(font)
        self.downloadBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.downloadBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.downloadBtn.setStyleSheet("border:solid;\n"
"border-width: 2px;\n"
"border-radius:20px;\n"
"border-color: rgb(254, 129, 5);\n"
"background-color:rgb(255, 255, 222)")
        self.downloadBtn.setObjectName("downloadBtn")
        self.verticalLayout.addWidget(self.downloadBtn)
        self.groupBox = QtWidgets.QGroupBox(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.finishedList = QtWidgets.QListWidget(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.finishedList.setFont(font)
        self.finishedList.setAlternatingRowColors(True)
        self.finishedList.setProperty("isWrapping", False)
        self.finishedList.setWordWrap(True)
        self.finishedList.setObjectName("finishedList")
        self.gridLayout_8.addWidget(self.finishedList, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout_9.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.confirmLabel = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmLabel.sizePolicy().hasHeightForWidth())
        self.confirmLabel.setSizePolicy(sizePolicy)
        self.confirmLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.confirmLabel.setFont(font)
        self.confirmLabel.setObjectName("confirmLabel")
        self.gridLayout_10.addWidget(self.confirmLabel, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.backBtn_DS = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn_DS.sizePolicy().hasHeightForWidth())
        self.backBtn_DS.setSizePolicy(sizePolicy)
        self.backBtn_DS.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.backBtn_DS.setFont(font)
        self.backBtn_DS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backBtn_DS.setStyleSheet("border:solid;\n"
"border-width: 2px;\n"
"border-radius:20px;\n"
"border-color: rgb(254, 129, 5);\n"
"background-color:rgb(255, 255, 222)")
        self.backBtn_DS.setObjectName("backBtn_DS")
        self.horizontalLayout_2.addWidget(self.backBtn_DS)
        self.confirmBtn = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmBtn.sizePolicy().hasHeightForWidth())
        self.confirmBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.confirmBtn.setFont(font)
        self.confirmBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confirmBtn.setStyleSheet("color:red;\n"
"border:solid;\n"
"border-width: 2px;\n"
"border-radius:20px;\n"
"border-color: rgb(254, 129, 5);\n"
"background-color:rgb(255, 255, 222)")
        self.confirmBtn.setObjectName("confirmBtn")
        self.horizontalLayout_2.addWidget(self.confirmBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.confirmList = QtWidgets.QListWidget(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.confirmList.setFont(font)
        self.confirmList.setAlternatingRowColors(True)
        self.confirmList.setObjectName("confirmList")
        self.horizontalLayout.addWidget(self.confirmList)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_10.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setEnabled(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_11.addWidget(self.label, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 40))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_11.addWidget(self.progressBar, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "小学"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "初中"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "高中"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "大学"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "留学"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "研究生"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:600; color:#6a8759;\">本地测试结果：</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:600; color:#ff0000;\">3,589</span><span style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:600; color:#6a8759;\"> </span><span style=\" font-family:\'等线\'; font-size:14pt; font-weight:600; color:#6a8759;\">个词</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:14pt; font-weight:600; color:#6a8759;\">共 约 </span><span style=\" font-family:\'等线\'; font-size:14pt; color:#ff0000;\">12 </span><span style=\" font-family:\'等线\'; font-size:14pt; font-weight:600; color:#6a8759;\">秒</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'等线\'; font-size:14pt; font-weight:600; color:#6a8759;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:14pt; font-weight:600; color:#6a8759;\">当时网速：</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:14pt; font-weight:600; color:#6a8759;\">下载</span><span style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:600; color:#6a8759;\">  5.85Mbps</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'等线\'; font-size:14pt; font-weight:600; color:#6a8759;\">上传</span><span style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:600; color:#6a8759;\">  1.47Mbps</span></p></body></html>"))
        self.downloadBtn.setText(_translate("Form", "下载离线书本"))
        self.groupBox.setTitle(_translate("Form", "已完成下载"))
        self.confirmLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\">共选择 4 本书， 预计 时间</p></body></html>"))
        self.backBtn_DS.setText(_translate("Form", "返回"))
        self.confirmBtn.setText(_translate("Form", "确认下载"))
        self.label.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic;\">Time is a river and let it gently on the slip through your fingers.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:28pt; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">时间是一条金河，莫让他轻轻地在你指尖溜过</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))