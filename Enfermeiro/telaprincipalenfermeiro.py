# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaprincipalenfermeiro.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from Enfermeiro.telaevolucao import Ui_TelaEvolucao
from Enfermeiro.telatriagem import Ui_TelaTriagem
from Enfermeiro.telabanho import Ui_TelaBanho
from Enfermeiro.telafralda import Ui_TelaFralda
from medico.telaprincipalmedicamento import Ui_TelaPrincipalMedicamento


class Ui_telaprincipalenfermeiro(object):
    def setupUi(self, telaprincipalenfermeiro):
        telaprincipalenfermeiro.setObjectName("telaprincipalenfermeiro")
        telaprincipalenfermeiro.resize(609, 570)
        self.centralwidget = QtWidgets.QWidget(telaprincipalenfermeiro)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 50, 381, 61))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 59))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.btnFralda = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnFralda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFralda.setObjectName("btnFralda")
        self.gridLayout.addWidget(self.btnFralda, 0, 0, 1, 1)
        self.btnBanho = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnBanho.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBanho.setObjectName("btnBanho")
        self.gridLayout.addWidget(self.btnBanho, 0, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 130, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabelaPacientes = QtWidgets.QTableWidget(self.centralwidget)
        self.tabelaPacientes.setGeometry(QtCore.QRect(10, 210, 581, 101))
        self.tabelaPacientes.setObjectName("tabelaPacientes")
        self.tabelaPacientes.setColumnCount(3)
        self.tabelaPacientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPacientes.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPacientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPacientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPacientes.setHorizontalHeaderItem(2, item)
        self.camPacientesAtua = QtWidgets.QLineEdit(self.centralwidget)
        self.camPacientesAtua.setGeometry(QtCore.QRect(10, 180, 231, 21))
        self.camPacientesAtua.setObjectName("camPacientesAtua")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 320, 631, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 340, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.camPrazementos = QtWidgets.QLineEdit(self.centralwidget)
        self.camPrazementos.setGeometry(QtCore.QRect(10, 370, 231, 21))
        self.camPrazementos.setObjectName("camPrazementos")
        self.tabelaPrazementos = QtWidgets.QTableWidget(self.centralwidget)
        self.tabelaPrazementos.setGeometry(QtCore.QRect(10, 400, 581, 111))
        self.tabelaPrazementos.setObjectName("tabelaPrazementos")
        self.tabelaPrazementos.setColumnCount(3)
        self.tabelaPrazementos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPrazementos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPrazementos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaPrazementos.setHorizontalHeaderItem(2, item)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 170, 131, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnBuscarPaciente = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnBuscarPaciente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarPaciente.setIcon(icon)
        self.btnBuscarPaciente.setObjectName("btnBuscarPaciente")
        self.gridLayout_2.addWidget(self.btnBuscarPaciente, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(250, 360, 121, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnPrazamentos = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnPrazamentos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPrazamentos.setIcon(icon)
        self.btnPrazamentos.setObjectName("btnPrazamentos")
        self.gridLayout_3.addWidget(self.btnPrazamentos, 0, 0, 1, 1)
        telaprincipalenfermeiro.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(telaprincipalenfermeiro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 21))
        self.menubar.setObjectName("menubar")
        self.menuAtividades = QtWidgets.QMenu(self.menubar)
        self.menuAtividades.setObjectName("menuAtividades")
        telaprincipalenfermeiro.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(telaprincipalenfermeiro)
        self.statusbar.setObjectName("statusbar")
        telaprincipalenfermeiro.setStatusBar(self.statusbar)
        self.actionEvolucao = QtWidgets.QAction(telaprincipalenfermeiro)
        self.actionEvolucao.setObjectName("actionEvolucao")
        self.actionTriagem = QtWidgets.QAction(telaprincipalenfermeiro)
        self.actionTriagem.setObjectName("actionTriagem")
        self.actionMedicamento = QtWidgets.QAction(telaprincipalenfermeiro)
        self.actionMedicamento.setObjectName("actionMedicamento")
        self.actionSair = QtWidgets.QAction(telaprincipalenfermeiro)
        self.actionSair.setObjectName("actionSair")
        self.menuAtividades.addAction(self.actionEvolucao)
        self.menuAtividades.addAction(self.actionTriagem)
        self.menuAtividades.addAction(self.actionMedicamento)
        self.menuAtividades.addSeparator()
        self.menuAtividades.addAction(self.actionSair)
        self.menubar.addAction(self.menuAtividades.menuAction())

        self.retranslateUi(telaprincipalenfermeiro)
        self.actionSair.triggered.connect(telaprincipalenfermeiro.close)

        #Menu slide parte superior
        self.actionEvolucao.triggered.connect(self.Evolucao)
        self.actionTriagem.triggered.connect(self.Triagem)
        self.actionMedicamento.triggered.connect(self.Medicamento)
        QtCore.QMetaObject.connectSlotsByName(telaprincipalenfermeiro)

        #botoes da tela
        self.btnBanho.clicked.connect(self.Banho)
        self.btnFralda.clicked.connect(self.Fralda)
        self.btnBuscarPaciente.clicked.connect(self.Buscar)
        self.btnPrazamentos.clicked.connect(self.Buscar1)



    def Evolucao(self):
        TelaEvolucao = QtWidgets.QDialog()
        ui = Ui_TelaEvolucao()
        ui.setupUi(TelaEvolucao)
        TelaEvolucao.show()
        TelaEvolucao.exec_()

    def Triagem(self):
        TelaTriagem = QtWidgets.QDialog()
        ui = Ui_TelaTriagem()
        ui.setupUi(TelaTriagem)
        TelaTriagem.show()
        TelaTriagem.exec_()

    def Banho(self):
        TelaBanho = QtWidgets.QDialog()
        ui = Ui_TelaBanho()
        ui.setupUi(TelaBanho)
        TelaBanho.show()
        TelaBanho.exec_()

    def Fralda(self):
        TelaFralda = QtWidgets.QDialog()
        ui = Ui_TelaFralda()
        ui.setupUi(TelaFralda)
        TelaFralda.show()
        TelaFralda.exec_()

    def Medicamento(self):
        TelaPrincipalMedicamento = QtWidgets.QDialog()
        ui = Ui_TelaPrincipalMedicamento()
        ui.setupUi(TelaPrincipalMedicamento)
        TelaPrincipalMedicamento.show()
        TelaPrincipalMedicamento.exec_()

    def Buscar(self):
        self.connection = sqlite3.connect('Paciente.db')
        self.query = "SELECT idInter,leito, nome FROM internacao"
        self.result = self.connection.execute(self.query)
        self.tabelaPacientes.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.tabelaPacientes.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tabelaPacientes.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.connection.close()

    def Buscar1(self):
        self.connection = sqlite3.connect('Paciente.db')
        self.query = "SELECT idInter,leito, nome FROM internacao"
        self.result = self.connection.execute(self.query)
        self.tabelaPrazementos.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.tabelaPrazementos.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tabelaPrazementos.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.connection.close()


    def retranslateUi(self, telaprincipalenfermeiro):
        _translate = QtCore.QCoreApplication.translate
        telaprincipalenfermeiro.setWindowTitle(_translate("telaprincipalenfermeiro", "Tela Principal Enfermeiro"))
        self.label.setText(_translate("telaprincipalenfermeiro", "Relatorios"))
        self.btnFralda.setText(_translate("telaprincipalenfermeiro", "Troca de fraldas"))
        self.btnBanho.setText(_translate("telaprincipalenfermeiro", "Banho"))
        self.label_2.setText(_translate("telaprincipalenfermeiro", "Pacientes atualizados"))
        item = self.tabelaPacientes.horizontalHeaderItem(0)
        item.setText(_translate("telaprincipalenfermeiro", "ID"))
        item = self.tabelaPacientes.horizontalHeaderItem(1)
        item.setText(_translate("telaprincipalenfermeiro", "Leito"))
        item = self.tabelaPacientes.horizontalHeaderItem(2)
        item.setText(_translate("telaprincipalenfermeiro", "Nome"))
        self.label_3.setText(_translate("telaprincipalenfermeiro", "Prazamentos"))
        item = self.tabelaPrazementos.horizontalHeaderItem(0)
        item.setText(_translate("telaprincipalenfermeiro", "ID"))
        item = self.tabelaPrazementos.horizontalHeaderItem(1)
        item.setText(_translate("telaprincipalenfermeiro", "Nome"))
        item = self.tabelaPrazementos.horizontalHeaderItem(2)
        item.setText(_translate("telaprincipalenfermeiro", "Leito"))
        self.btnBuscarPaciente.setText(_translate("telaprincipalenfermeiro", "Buscar"))
        self.btnPrazamentos.setText(_translate("telaprincipalenfermeiro", "Buscar"))
        self.menuAtividades.setTitle(_translate("telaprincipalenfermeiro", "Atividades"))
        self.actionEvolucao.setText(_translate("telaprincipalenfermeiro", "Evolução"))
        self.actionTriagem.setText(_translate("telaprincipalenfermeiro", "Triagem"))
        self.actionMedicamento.setText(_translate("telaprincipalenfermeiro", "Medicamento"))
        self.actionSair.setText(_translate("telaprincipalenfermeiro", "Sair"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    telaprincipalenfermeiro = QtWidgets.QMainWindow()
    ui = Ui_telaprincipalenfermeiro()
    ui.setupUi(telaprincipalenfermeiro)
    telaprincipalenfermeiro.show()
    sys.exit(app.exec_())
