# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaconsultaficha.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from Atendimento.telaconsultaresultado import Ui_TelaConsultaResultado


class Ui_TelaConsultaFicha(object):

    def Nova(self):
        connection = sqlite3.connect('Paciente.db')
        query = "SELECT * FROM paciente"
        result = connection.execute(query)
        self.tableWidgetConsulta.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetConsulta.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetConsulta.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def setupUi(self, TelaConsultaFicha):
        TelaConsultaFicha.setObjectName("TelaConsultaFicha")
        TelaConsultaFicha.setFixedSize(822, 624)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/atendimento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaConsultaFicha.setWindowIcon(icon)
        TelaConsultaFicha.setStyleSheet("QDialog{\n"
"    background-color: #e9e9e9;\n"
"}")
        TelaConsultaFicha.setModal(True)
        self.label = QtWidgets.QLabel(TelaConsultaFicha)
        self.label.setGeometry(QtCore.QRect(9, 9, 140, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(TelaConsultaFicha)
        self.line.setGeometry(QtCore.QRect(9, 38, 804, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidgetConsulta = QtWidgets.QTableWidget(TelaConsultaFicha)
        self.tableWidgetConsulta.setGeometry(QtCore.QRect(9, 53, 811, 501))
        self.tableWidgetConsulta.setRowCount(0) #quantidade de linhas
        self.tableWidgetConsulta.setColumnCount(24)
        self.tableWidgetConsulta.setObjectName("tableWidgetConsulta")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetConsulta.setHorizontalHeaderItem(23, item)
        self.tableWidgetConsulta.horizontalHeader().setVisible(True)
        self.tableWidgetConsulta.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetConsulta.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetConsulta.horizontalHeader().setHighlightSections(True)
        self.tableWidgetConsulta.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidgetConsulta.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetConsulta.horizontalHeader().setStretchLastSection(False)
        self.tableWidgetConsulta.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetConsulta.verticalHeader().setDefaultSectionSize(30)
        self.tableWidgetConsulta.verticalHeader().setHighlightSections(True)
        self.tableWidgetConsulta.verticalHeader().setMinimumSectionSize(30)
        self.tableWidgetConsulta.verticalHeader().setSortIndicatorShown(False)
        self.tableWidgetConsulta.verticalHeader().setStretchLastSection(False)
        self.scrollArea = QtWidgets.QScrollArea(TelaConsultaFicha)
        self.scrollArea.setGeometry(QtCore.QRect(476, 560, 331, 51))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 49))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.btnFechar = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnFechar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFechar.setIcon(icon1)
        self.btnFechar.setObjectName("btnFechar")
        self.gridLayout.addWidget(self.btnFechar, 0, 0, 1, 1)
        self.btnNovaConsulta = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnNovaConsulta.setIcon(icon)
        self.btnNovaConsulta.setObjectName("btnNovaConsulta")
        self.gridLayout.addWidget(self.btnNovaConsulta, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(TelaConsultaFicha)
        QtCore.QMetaObject.connectSlotsByName(TelaConsultaFicha)

        #Botão para sair
        self.btnFechar.clicked.connect(TelaConsultaFicha.close)
        self.btnNovaConsulta.clicked.connect(self.Nova)



    def retranslateUi(self, TelaConsultaFicha):
        _translate = QtCore.QCoreApplication.translate
        TelaConsultaFicha.setWindowTitle(_translate("TelaConsultaFicha", "Consulta Ficha"))
        self.label.setText(_translate("TelaConsultaFicha", "Consulta Ficha"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(0)
        item.setText(_translate("TelaConsultaFicha", "id"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(1)
        item.setText(_translate("TelaConsultaFicha", "Nome"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(2)
        item.setText(_translate("TelaConsultaFicha", "Nasecimento"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(3)
        item.setText(_translate("TelaConsultaFicha", "Idade"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(4)
        item.setText(_translate("TelaConsultaFicha", "CPF"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(5)
        item.setText(_translate("TelaConsultaFicha", "RG"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(6)
        item.setText(_translate("TelaConsultaFicha", "UF"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(7)
        item.setText(_translate("TelaConsultaFicha", "E-Mail"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(8)
        item.setText(_translate("TelaConsultaFicha", "Passaporte"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(9)
        item.setText(_translate("TelaConsultaFicha", "Celular"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(10)
        item.setText(_translate("TelaConsultaFicha", "Menor"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(11)
        item.setText(_translate("TelaConsultaFicha", "CEP"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(12)
        item.setText(_translate("TelaConsultaFicha", "Endereco"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(13)
        item.setText(_translate("TelaConsultaFicha", "numero"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(14)
        item.setText(_translate("TelaConsultaFicha", "Bairro"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(15)
        item.setText(_translate("TelaConsultaFicha", "Complemento"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(16)
        item.setText(_translate("TelaConsultaFicha", "Estado"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(17)
        item.setText(_translate("TelaConsultaFicha", "Atendimento"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(18)
        item.setText(_translate("TelaConsultaFicha", "data entrada"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(19)
        item.setText(_translate("TelaConsultaFicha", "hora"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(20)
        item.setText(_translate("TelaConsultaFicha", "especialista"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(21)
        item.setText(_translate("TelaConsultaFicha", "Forma de atendimento"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(22)
        item.setText(_translate("TelaConsultaFicha", "valor"))
        item = self.tableWidgetConsulta.horizontalHeaderItem(23)
        item.setText(_translate("TelaConsultaFicha", "Obs"))
        self.btnFechar.setText(_translate("TelaConsultaFicha", "Fechar"))
        self.btnNovaConsulta.setText(_translate("TelaConsultaFicha", "Nova consulta"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaConsultaFicha = QtWidgets.QDialog()
    ui = Ui_TelaConsultaFicha()
    ui.setupUi(TelaConsultaFicha)
    TelaConsultaFicha.show()
    sys.exit(app.exec_())
