# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaloginmedico.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from medico.telaprincipalmedico import Ui_TelaPrincipalMedico


class Ui_TelaLoginMedico(object):
    def setupUi(self, TelaLoginMedico):
        TelaLoginMedico.setObjectName("TelaLoginMedico")
        TelaLoginMedico.setFixedSize(355, 208)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/medico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaLoginMedico.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(TelaLoginMedico)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 30, 201, 92))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.CamCRM = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.CamCRM.setObjectName("CamCRM")
        self.verticalLayout.addWidget(self.CamCRM)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.senhaMedico = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.senhaMedico.setObjectName("senhaMedico")
        self.verticalLayout.addWidget(self.senhaMedico)
        self.btnLogarMedico = QtWidgets.QPushButton(TelaLoginMedico)
        self.btnLogarMedico.setGeometry(QtCore.QRect(240, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogarMedico.setFont(font)
        self.btnLogarMedico.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogarMedico.setIcon(icon1)
        self.btnLogarMedico.setObjectName("btnLogarMedico")

        self.retranslateUi(TelaLoginMedico)
        QtCore.QMetaObject.connectSlotsByName(TelaLoginMedico)

        #Mudando texto para senha
        self.senhaMedico.setEchoMode(QtWidgets.QLineEdit.Password)

        #Botao para cessar
        self.btnLogarMedico.clicked.connect(self.LogarMedico)



    #Função para logar
    def LogarMedico(self):
        if (self.CamCRM.text() == "arley" and self.senhaMedico.text() == "arley"):
            QMessageBox.information(QMessageBox(), 'Login', 'Login Efetuado com sucesso')
            telaprincipalenfermeiro = QtWidgets.QMainWindow()
            ui = Ui_TelaPrincipalMedico()
            ui.setupUi(telaprincipalenfermeiro)
            telaprincipalenfermeiro.show()
            TelaLoginMedico.exec_()
        else:
            QMessageBox.warning(QMessageBox(), 'Erro', 'Login ou senha incorreto')

    def retranslateUi(self, TelaLoginMedico):
        _translate = QtCore.QCoreApplication.translate
        TelaLoginMedico.setWindowTitle(_translate("TelaLoginMedico", "Login Medico"))
        self.label.setText(_translate("TelaLoginMedico", "CRM"))
        self.label_2.setText(_translate("TelaLoginMedico", "Senha"))
        self.btnLogarMedico.setText(_translate("TelaLoginMedico", "Logar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaLoginMedico = QtWidgets.QDialog()
    ui = Ui_TelaLoginMedico()
    ui.setupUi(TelaLoginMedico)
    TelaLoginMedico.show()
    sys.exit(app.exec_())
