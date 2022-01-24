# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telalogin.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from Atendimento.telaprincipalatendimento import Ui_TelaPrincipalAtendimento






class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):

        TelaLogin.setObjectName("TelaLogin")
        TelaLogin.setWindowModality(QtCore.Qt.WindowModal)
        TelaLogin.setFixedSize(358, 246)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaLogin.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(TelaLogin)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 50, 211, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblLogin = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblLogin.setFont(font)
        self.lblLogin.setObjectName("lblLogin")
        self.verticalLayout.addWidget(self.lblLogin)
        self.CamLogin = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.CamLogin.setObjectName("CamLogin")
        self.verticalLayout.addWidget(self.CamLogin)
        self.lblSenha = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblSenha.setFont(font)
        self.lblSenha.setObjectName("lblSenha")
        self.verticalLayout.addWidget(self.lblSenha)
        self.CamSenha = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.CamSenha.setObjectName("CamSenha")
        self.verticalLayout.addWidget(self.CamSenha)
        self.btnAcessar = QtWidgets.QPushButton(self.centralWidget)
        self.btnAcessar.setGeometry(QtCore.QRect(230, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAcessar.setFont(font)
        self.btnAcessar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/entrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAcessar.setIcon(icon1)
        self.btnAcessar.setObjectName("btnAcessar")
        TelaLogin.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(TelaLogin)
        self.statusBar.setObjectName("statusBar")
        TelaLogin.setStatusBar(self.statusBar)

        self.btnAcessar.clicked.connect(self.login)

        self.retranslateUi(TelaLogin)
        QtCore.QMetaObject.connectSlotsByName(TelaLogin)

        self.fechar = TelaLogin
        self.fechar.close()

        self.CamSenha.setEchoMode(QtWidgets.QLineEdit.Password)




    def login(self):
        if (self.CamSenha.text() == 'arley' and self.CamLogin.text() == 'arley'):
            QMessageBox.information(QMessageBox(), 'Bem vindo', 'Login com sucesso')
            TelaPrincipalAtendimento = QtWidgets.QDialog()
            ui = Ui_TelaPrincipalAtendimento()
            ui.setupUi(TelaPrincipalAtendimento)
            TelaPrincipalAtendimento.show()
            TelaPrincipalAtendimento.exec_()
            TelaLogin.close()
        else:
            QMessageBox.warning(QMessageBox(), 'Error', 'Senha ou Login incorretas')

    def retranslateUi(self, TelaLogin):
        _translate = QtCore.QCoreApplication.translate
        TelaLogin.setWindowTitle(_translate("TelaLogin", "Login"))
        self.lblLogin.setText(_translate("TelaLogin", "Login"))
        self.lblSenha.setText(_translate("TelaLogin", "Senha"))
        self.btnAcessar.setText(_translate("TelaLogin", "Acessar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaLogin = QtWidgets.QMainWindow()
    ui = Ui_TelaLogin()
    ui.setupUi(TelaLogin)
    TelaLogin.show()
    sys.exit(app.exec_())
