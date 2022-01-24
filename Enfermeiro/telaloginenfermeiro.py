# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaloginenfermeiro.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Enfermeiro.telaprincipalenfermeiro import Ui_telaprincipalenfermeiro

class Ui_TelaLoginEnfermeiro(object):
    def setupUi(self, TelaLoginEnfermeiro):
        TelaLoginEnfermeiro.setObjectName("TelaLoginEnfermeiro")
        TelaLoginEnfermeiro.setFixedSize(355, 209)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/enfermeira.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaLoginEnfermeiro.setWindowIcon(icon)
        TelaLoginEnfermeiro.setModal(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(TelaLoginEnfermeiro)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 30, 211, 101))
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
        self.camLoginCoren = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.camLoginCoren.setObjectName("camLoginCoren")
        self.verticalLayout.addWidget(self.camLoginCoren)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.camSenhaEnf = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.camSenhaEnf.setObjectName("camSenhaEnf")
        self.verticalLayout.addWidget(self.camSenhaEnf)
        self.btnLogarEnfermeiro = QtWidgets.QPushButton(TelaLoginEnfermeiro)
        self.btnLogarEnfermeiro.setGeometry(QtCore.QRect(230, 160, 101, 31))
        self.btnLogarEnfermeiro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogarEnfermeiro.setIcon(icon1)
        self.btnLogarEnfermeiro.setObjectName("btnLogarEnfermeiro")

        self.retranslateUi(TelaLoginEnfermeiro)
        QtCore.QMetaObject.connectSlotsByName(TelaLoginEnfermeiro)

        #Mudar o caractere para senha
        self.camSenhaEnf.setEchoMode(QtWidgets.QLineEdit.Password)
        #Botão para logar
        self.btnLogarEnfermeiro.clicked.connect(self.LoginEnf)

    #Função para logar enfermeiro
    def LoginEnf(self):
        if(self.camLoginCoren.text() == "arley" and self.camSenhaEnf.text() == "arley"):
            QMessageBox.information(QMessageBox(), 'Login', 'Login Efetuado com sucesso')
            telaprincipalenfermeiro = QtWidgets.QMainWindow()
            ui = Ui_telaprincipalenfermeiro()
            ui.setupUi(telaprincipalenfermeiro)
            telaprincipalenfermeiro.show()
            TelaLoginEnfermeiro.exec_()
        else:
            QMessageBox.warning(QMessageBox(), 'Erro', 'Login ou senha incorreto')




    def retranslateUi(self, TelaLoginEnfermeiro):
        _translate = QtCore.QCoreApplication.translate
        TelaLoginEnfermeiro.setWindowTitle(_translate("TelaLoginEnfermeiro", "Login Enfermeiro"))
        self.label.setText(_translate("TelaLoginEnfermeiro", "Entre com seu COREN"))
        self.label_2.setText(_translate("TelaLoginEnfermeiro", "Senha"))
        self.btnLogarEnfermeiro.setText(_translate("TelaLoginEnfermeiro", "Entrar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaLoginEnfermeiro = QtWidgets.QDialog()
    ui = Ui_TelaLoginEnfermeiro()
    ui.setupUi(TelaLoginEnfermeiro)
    TelaLoginEnfermeiro.show()
    sys.exit(app.exec_())
