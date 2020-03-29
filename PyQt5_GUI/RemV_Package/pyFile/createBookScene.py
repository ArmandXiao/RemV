# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createBookScene.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.createBookBtn = QtWidgets.QPushButton(Dialog)
        self.createBookBtn.setGeometry(QtCore.QRect(80, 190, 231, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.createBookBtn.setFont(font)
        self.createBookBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createBookBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createBookBtn.setStyleSheet("border:solid;\n"
"border-width: 2px;\n"
"border-radius:20px;\n"
"border-color: rgb(254, 129, 5);\n"
"background-color:rgb(255, 255, 222)")
        self.createBookBtn.setObjectName("createBookBtn")
        self.enterNameEdit = QtWidgets.QLineEdit(Dialog)
        self.enterNameEdit.setGeometry(QtCore.QRect(40, 110, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.enterNameEdit.setFont(font)
        self.enterNameEdit.setObjectName("enterNameEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "输入创建的书籍的名称："))
        self.createBookBtn.setText(_translate("Dialog", "Create"))
