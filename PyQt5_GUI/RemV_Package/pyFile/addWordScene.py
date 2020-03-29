# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addWordScene.ui'
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
        self.label.setGeometry(QtCore.QRect(40, 50, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.wordEnter = QtWidgets.QLineEdit(Dialog)
        self.wordEnter.setGeometry(QtCore.QRect(40, 120, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.wordEnter.setFont(font)
        self.wordEnter.setObjectName("wordEnter")
        self.doneBtn = QtWidgets.QPushButton(Dialog)
        self.doneBtn.setGeometry(QtCore.QRect(80, 200, 231, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.doneBtn.setFont(font)
        self.doneBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.doneBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.doneBtn.setStyleSheet("border:solid;\n"
"border-width: 2px;\n"
"border-radius:20px;\n"
"border-color: rgb(254, 129, 5);\n"
"background-color:rgb(255, 255, 222)")
        self.doneBtn.setObjectName("doneBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "输入想添加的单词："))
        self.doneBtn.setText(_translate("Dialog", "完成录入，关闭窗口"))
