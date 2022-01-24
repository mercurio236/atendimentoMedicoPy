# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaprincipalmedicamento.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from Enfermeiro.telademedicamento import Ui_TelaDeMedicamento


class Ui_TelaPrincipalMedicamento(object):
    def setupUi(self, TelaPrincipalMedicamento):
        TelaPrincipalMedicamento.setObjectName("TelaPrincipalMedicamento")
        TelaPrincipalMedicamento.setFixedSize(791, 435)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/medicamento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaPrincipalMedicamento.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(TelaPrincipalMedicamento)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        TelaPrincipalMedicamento.setModal(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(TelaPrincipalMedicamento)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnSair = QtWidgets.QPushButton(TelaPrincipalMedicamento)
        self.btnSair.setGeometry(QtCore.QRect(710, 10, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSair.setFont(font)
        self.btnSair.setStyleSheet("QPushButton{\n"
"    background-color: red;\n"
"    color: white;\n"
"}")
        self.btnSair.setObjectName("btnSair")
        self.line = QtWidgets.QFrame(TelaPrincipalMedicamento)
        self.line.setGeometry(QtCore.QRect(0, 60, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(TelaPrincipalMedicamento)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(TelaPrincipalMedicamento)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 771, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        self.label_4 = QtWidgets.QLabel(TelaPrincipalMedicamento)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.nomeUsu = QtWidgets.QLabel(TelaPrincipalMedicamento)
        self.nomeUsu.setGeometry(QtCore.QRect(140, 10, 351, 31))
        self.nomeUsu.setStyleSheet("QLabel{\n"
"    color:blue;\n"
"}")
        self.nomeUsu.setText("")
        self.nomeUsu.setObjectName("nomeUsu")
        self.matUsua = QtWidgets.QLabel(TelaPrincipalMedicamento)
        self.matUsua.setGeometry(QtCore.QRect(90, 30, 161, 31))
        self.matUsua.setText("")
        self.matUsua.setObjectName("matUsua")
        self.nomePaciente = QtWidgets.QLabel(TelaPrincipalMedicamento)
        self.nomePaciente.setGeometry(QtCore.QRect(140, 320, 381, 31))
        self.nomePaciente.setText("")
        self.nomePaciente.setObjectName("nomePaciente")
        self.scrollArea = QtWidgets.QScrollArea(TelaPrincipalMedicamento)
        self.scrollArea.setGeometry(QtCore.QRect(420, 370, 361, 61))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 59))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.btnEditar = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnEditar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditar.setIcon(icon1)
        self.btnEditar.setObjectName("btnEditar")
        self.gridLayout.addWidget(self.btnEditar, 0, 0, 1, 1)
        self.btnAnterior = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnAnterior.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAnterior.setStyleSheet("QPushButton{\n"
"    background-color: #FF603B;\n"
"    color: white;\n"
"}")
        self.btnAnterior.setObjectName("btnAnterior")
        self.gridLayout.addWidget(self.btnAnterior, 0, 1, 1, 1)
        self.btnProximo = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnProximo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProximo.setStyleSheet("QPushButton{\n"
"    background-color: #2DBD3B;\n"
"    color: white;\n"
"}")
        self.btnProximo.setObjectName("btnProximo")
        self.gridLayout.addWidget(self.btnProximo, 0, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(TelaPrincipalMedicamento)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipalMedicamento)

        #Botoes
        self.btnEditar.clicked.connect(self.Editar)
        self.btnSair.clicked.connect(self.Atualizar)

    def Editar(self):
        TelaDeMedicamento = QtWidgets.QDialog()
        ui = Ui_TelaDeMedicamento()
        ui.setupUi(TelaDeMedicamento)
        TelaDeMedicamento.show()
        TelaDeMedicamento.exec_()


    def Atualizar(self):
        self.connection = sqlite3.connect('Paciente.db')
        self.query = "SELECT nome, data, idade, cpf, rg, uf, email, celular, passaport, end, cep, numeroCasa, bairro, uf1  FROM paciente"
        self.result = self.connection.execute(self.query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(self.result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        self.connection.close()

    def retranslateUi(self, TelaPrincipalMedicamento):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipalMedicamento.setWindowTitle(_translate("TelaPrincipalMedicamento", "Tela Principal de Medicamento"))
        self.label.setText(_translate("TelaPrincipalMedicamento", "Nome do Usuário:"))
        self.label_2.setText(_translate("TelaPrincipalMedicamento", "Matrícula:"))
        self.btnSair.setText(_translate("TelaPrincipalMedicamento", "Atualizar"))
        self.label_3.setText(_translate("TelaPrincipalMedicamento", "Fila"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("TelaPrincipalMedicamento", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TelaPrincipalMedicamento", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TelaPrincipalMedicamento", "Nascimento"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TelaPrincipalMedicamento", "Idade"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TelaPrincipalMedicamento", "CPF"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("TelaPrincipalMedicamento", "RG"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("TelaPrincipalMedicamento", "UF"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("TelaPrincipalMedicamento", "E-mail"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("TelaPrincipalMedicamento", "Celular"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("TelaPrincipalMedicamento", "Passaporte"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("TelaPrincipalMedicamento", "Endereco"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("TelaPrincipalMedicamento", "CEP"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("TelaPrincipalMedicamento", "N"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("TelaPrincipalMedicamento", "Bairro"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("TelaPrincipalMedicamento", "Estado"))
        self.label_4.setText(_translate("TelaPrincipalMedicamento", "Nome do Paciente:"))
        self.btnEditar.setText(_translate("TelaPrincipalMedicamento", "Editar"))
        self.btnAnterior.setText(_translate("TelaPrincipalMedicamento", "Anterior"))
        self.btnProximo.setText(_translate("TelaPrincipalMedicamento", "Proxímo"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipalMedicamento = QtWidgets.QDialog()
    ui = Ui_TelaPrincipalMedicamento()
    ui.setupUi(TelaPrincipalMedicamento)
    TelaPrincipalMedicamento.show()
    sys.exit(app.exec_())
