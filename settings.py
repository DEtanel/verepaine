# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUiDialog(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 50, 61, 41))
        self.label.setObjectName("label")
        self.lineEdit_city = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_city.setGeometry(QtCore.QRect(190, 60, 113, 20))
        self.lineEdit_city.setObjectName("lineEdit")
        # self.label_2 = QtWidgets.QLabel(Dialog)
        # self.label_2.setGeometry(QtCore.QRect(30, 130, 121, 31))
        # self.label_2.setObjectName("label_2")
        # self.lineEdit_reduceday = QtWidgets.QLineEdit(Dialog)
        # self.lineEdit_reduceday.setGeometry(QtCore.QRect(190, 130, 111, 21))
        # self.lineEdit_reduceday.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Asetukset"))
        self.label.setText(_translate("Dialog", "Kaupunki"))
        self.lineEdit_city.setText(_translate("Dialog", "Helsinki"))
        # self.label_2.setText(_translate("Dialog", "Päivän siirton ( - 1/2 pv)"))
    
