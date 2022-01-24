# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaevolucao.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Enfermeiro.telabalancohibrido import Ui_TelaBalancoHibrido
from Enfermeiro.telasinaisvitais import Ui_SinaisVitais
from Enfermeiro.telachecagem import Ui_TelaChecagem
from Enfermeiro.telacirurgia import Ui_TelaCirurgia
from Enfermeiro.telaevolucaomedica import Ui_EvolucaoMedica
from medico.telaprincipalmedicamento import Ui_TelaPrincipalMedicamento

class Ui_TelaEvolucao(object):
    def setupUi(self, TelaEvolucao):
        TelaEvolucao.setObjectName("TelaEvolucao")
        TelaEvolucao.setFixedSize(531, 353)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/atendimento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaEvolucao.setWindowIcon(icon)
        TelaEvolucao.setModal(True)
        self.label = QtWidgets.QLabel(TelaEvolucao)
        self.label.setGeometry(QtCore.QRect(10, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(TelaEvolucao)
        self.label_2.setGeometry(QtCore.QRect(10, 25, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(TelaEvolucao)
        self.label_3.setGeometry(QtCore.QRect(250, 26, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(TelaEvolucao)
        self.label_4.setGeometry(QtCore.QRect(420, 25, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(TelaEvolucao)
        self.line.setGeometry(QtCore.QRect(-10, 50, 551, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(TelaEvolucao)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnFinalizar = QtWidgets.QPushButton(TelaEvolucao)
        self.btnFinalizar.setGeometry(QtCore.QRect(390, 310, 121, 31))
        self.btnFinalizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFinalizar.setIcon(icon1)
        self.btnFinalizar.setObjectName("btnFinalizar")
        self.widget = QtWidgets.QWidget(TelaEvolucao)
        self.widget.setGeometry(QtCore.QRect(10, 100, 291, 161))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnHibrido = QtWidgets.QPushButton(self.widget)
        self.btnHibrido.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHibrido.setObjectName("btnHibrido")
        self.gridLayout.addWidget(self.btnHibrido, 0, 0, 1, 1)
        self.btnMedicamentos = QtWidgets.QPushButton(self.widget)
        self.btnMedicamentos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMedicamentos.setObjectName("btnMedicamentos")
        self.gridLayout.addWidget(self.btnMedicamentos, 0, 1, 1, 1)
        self.btnVitais = QtWidgets.QPushButton(self.widget)
        self.btnVitais.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVitais.setObjectName("btnVitais")
        self.gridLayout.addWidget(self.btnVitais, 1, 0, 1, 1)
        self.btnCirurgias = QtWidgets.QPushButton(self.widget)
        self.btnCirurgias.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCirurgias.setObjectName("btnCirurgias")
        self.gridLayout.addWidget(self.btnCirurgias, 1, 1, 1, 1)
        self.btnChecagem = QtWidgets.QPushButton(self.widget)
        self.btnChecagem.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnChecagem.setObjectName("btnChecagem")
        self.gridLayout.addWidget(self.btnChecagem, 2, 0, 1, 1)
        self.btnEvolucos = QtWidgets.QPushButton(self.widget)
        self.btnEvolucos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEvolucos.setObjectName("btnEvolucos")
        self.gridLayout.addWidget(self.btnEvolucos, 2, 1, 1, 1)

        self.retranslateUi(TelaEvolucao)
        QtCore.QMetaObject.connectSlotsByName(TelaEvolucao)

        #Botões
        self.btnHibrido.clicked.connect(self.hibrido)
        self.btnVitais.clicked.connect(self.Vitais)
        self.btnChecagem.clicked.connect(self.Check)
        self.btnCirurgias.clicked.connect(self.Cirurgia)
        self.btnEvolucos.clicked.connect(self.Evolucao)
        self.btnMedicamentos.clicked.connect(self.Medicamentos)
        self.btnFinalizar.clicked.connect(TelaEvolucao.close)

    #Funções dos botões

    def Vitais(self):
        SinaisVitais = QtWidgets.QDialog()
        ui = Ui_SinaisVitais()
        ui.setupUi(SinaisVitais)
        SinaisVitais.show()
        SinaisVitais.exec_()


    def hibrido(self):
        TelaBalancoHibrido = QtWidgets.QDialog()
        ui = Ui_TelaBalancoHibrido()
        ui.setupUi(TelaBalancoHibrido)
        TelaBalancoHibrido.show()
        TelaBalancoHibrido.exec_()

    def Check(self):
        TelaChecagem = QtWidgets.QDialog()
        ui = Ui_TelaChecagem()
        ui.setupUi(TelaChecagem)
        TelaChecagem.show()
        TelaChecagem.exec_()

    def Cirurgia(self):
        TelaCirurgia = QtWidgets.QDialog()
        ui = Ui_TelaCirurgia()
        ui.setupUi(TelaCirurgia)
        TelaCirurgia.show()
        TelaCirurgia.exec_()

    def Evolucao(self):
        EvolucaoMedica = QtWidgets.QDialog()
        ui = Ui_EvolucaoMedica()
        ui.setupUi(EvolucaoMedica)
        EvolucaoMedica.show()
        EvolucaoMedica.exec_()

    def Medicamentos(self):
        TelaPrincipalMedicamento = QtWidgets.QDialog()
        ui = Ui_TelaPrincipalMedicamento()
        ui.setupUi(TelaPrincipalMedicamento)
        TelaPrincipalMedicamento.show()
        TelaPrincipalMedicamento.exec_()


    def retranslateUi(self, TelaEvolucao):
        _translate = QtCore.QCoreApplication.translate
        TelaEvolucao.setWindowTitle(_translate("TelaEvolucao", "Evolução"))
        self.label.setText(_translate("TelaEvolucao", "Nome do Paciente:"))
        self.label_2.setText(_translate("TelaEvolucao", "Data de Entrada:"))
        self.label_3.setText(_translate("TelaEvolucao", "Leito:"))
        self.label_4.setText(_translate("TelaEvolucao", "Status:"))
        self.label_5.setText(_translate("TelaEvolucao", "Evoluções:"))
        self.btnFinalizar.setText(_translate("TelaEvolucao", "Finalizar"))
        self.btnHibrido.setText(_translate("TelaEvolucao", "Balanço hídrico"))
        self.btnMedicamentos.setText(_translate("TelaEvolucao", "Medicamentos"))
        self.btnVitais.setText(_translate("TelaEvolucao", "Sinais Vitais"))
        self.btnCirurgias.setText(_translate("TelaEvolucao", "Cirurgias"))
        self.btnChecagem.setText(_translate("TelaEvolucao", "Checagem"))
        self.btnEvolucos.setText(_translate("TelaEvolucao", "Evoluções Medicas"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaEvolucao = QtWidgets.QDialog()
    ui = Ui_TelaEvolucao()
    ui.setupUi(TelaEvolucao)
    TelaEvolucao.show()
    sys.exit(app.exec_())
