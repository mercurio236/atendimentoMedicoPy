# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telatriagem.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox, QLabel


class Ui_TelaTriagem(object):
    def setupUi(self, TelaTriagem):
        TelaTriagem.setObjectName("TelaTriagem")
        TelaTriagem.resize(651, 634)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/enfermeira.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaTriagem.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(TelaTriagem)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        TelaTriagem.setModal(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.ListaPaciente = QtWidgets.QTableWidget(TelaTriagem)
        self.ListaPaciente.setObjectName("ListaPaciente")
        self.ListaPaciente.setColumnCount(5)
        self.ListaPaciente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ListaPaciente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListaPaciente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListaPaciente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListaPaciente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListaPaciente.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.ListaPaciente, 1, 0, 1, 7)
        self.btnProxTriagem = QtWidgets.QPushButton(TelaTriagem)
        self.btnProxTriagem.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/entrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProxTriagem.setIcon(icon1)
        self.btnProxTriagem.setObjectName("btnProxTriagem")
        self.gridLayout.addWidget(self.btnProxTriagem, 2, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.NomePaciente = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NomePaciente.setFont(font)
        self.NomePaciente.setText("")
        self.NomePaciente.setObjectName("NomePaciente")
        self.gridLayout.addWidget(self.NomePaciente, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 1)
        self.dtaPaciente = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dtaPaciente.setFont(font)
        self.dtaPaciente.setText("")
        self.dtaPaciente.setObjectName("dtaPaciente")
        self.gridLayout.addWidget(self.dtaPaciente, 3, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 2)
        self.ObsPaciente = QtWidgets.QTextEdit(TelaTriagem)
        self.ObsPaciente.setObjectName("ObsPaciente")
        self.gridLayout.addWidget(self.ObsPaciente, 5, 0, 1, 7)
        self.label_7 = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 2)
        self.ObsEnfermeiro = QtWidgets.QTextEdit(TelaTriagem)
        self.ObsEnfermeiro.setObjectName("ObsEnfermeiro")
        self.gridLayout.addWidget(self.ObsEnfermeiro, 7, 0, 1, 7)
        self.label_8 = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 3, 1, 1)
        self.ComboMedico = QtWidgets.QComboBox(TelaTriagem)
        self.ComboMedico.setObjectName("ComboMedico")
        self.gridLayout.addWidget(self.ComboMedico, 9, 0, 1, 1)
        self.dtaSaida = QtWidgets.QLabel(TelaTriagem)
        self.dtaSaida.setText("")
        self.dtaSaida.setObjectName("dtaSaida")
        self.gridLayout.addWidget(self.dtaSaida, 9, 2, 1, 1)
        self.hrSaida = QtWidgets.QLabel(TelaTriagem)
        self.hrSaida.setText("")
        self.hrSaida.setObjectName("hrSaida")
        self.gridLayout.addWidget(self.hrSaida, 9, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(TelaTriagem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)
        self.ComboStatus = QtWidgets.QComboBox(TelaTriagem)
        self.ComboStatus.setObjectName("ComboStatus")
        self.gridLayout.addWidget(self.ComboStatus, 11, 0, 1, 1)
        self.btnCancelar = QtWidgets.QPushButton(TelaTriagem)
        self.btnCancelar.setObjectName("btnCancelar")
        self.gridLayout.addWidget(self.btnCancelar, 11, 3, 1, 1)
        self.btnAusente = QtWidgets.QPushButton(TelaTriagem)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagens/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAusente.setIcon(icon2)
        self.btnAusente.setObjectName("btnAusente")
        self.gridLayout.addWidget(self.btnAusente, 11, 5, 1, 1)
        self.btnEncaminhar = QtWidgets.QPushButton(TelaTriagem)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../imagens/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEncaminhar.setIcon(icon3)
        self.btnEncaminhar.setObjectName("btnEncaminhar")
        self.gridLayout.addWidget(self.btnEncaminhar, 11, 6, 1, 1)

        self.retranslateUi(TelaTriagem)
        QtCore.QMetaObject.connectSlotsByName(TelaTriagem)

        #Botoes

        self.btnCancelar.clicked.connect(TelaTriagem.close)
        self.btnEncaminhar.clicked.connect(self.salvarOBS)

        #Especialista

        self.ComboMedico.addItem("Cardiologia")
        self.ComboMedico.addItem("Cardiologia Pediatrica")
        self.ComboMedico.addItem("Dermatovenereologia")
        self.ComboMedico.addItem("Doenças Infercciosas")
        self.ComboMedico.addItem("Endocrionologia")
        self.ComboMedico.addItem("Ginecologia")
        self.ComboMedico.addItem("Ginecologia/Obstetrica")
        self.ComboMedico.addItem("Imunoalergologia")
        self.ComboMedico.addItem("Hematologia")
        self.ComboMedico.addItem("Medico Geral")
        self.ComboMedico.addItem("Neurologia")
        self.ComboMedico.addItem("Oncologia")
        self.ComboMedico.addItem("Otorrinolaringologia")
        self.ComboMedico.addItem("Patologia")
        self.ComboMedico.addItem("Pediatria")
        self.ComboMedico.addItem("Pneumologia")
        self.ComboMedico.addItem("Psiquiatria")
        self.ComboMedico.addItem("Radiologia")
        self.ComboMedico.addItem("Urulogia")


        #estatus
        self.ComboStatus.addItem("Baixo")
        self.ComboStatus.addItem("Médio")
        self.ComboStatus.addItem("Alto")
        self.ComboStatus.addItem("Internação")
        self.ComboStatus.addItem("Urgência")

        self.btnProxTriagem.clicked.connect(self.Nova)

        #Deixa campo Observação Paciente desabilitado
        desabilitado = False if self.ObsPaciente.isEnabled() else True
        self.ObsPaciente.setEnabled(desabilitado)

















    def salvarOBS(self):
        obs = ""
        encaminhar = ""
        status = ""

        obs = self.ObsEnfermeiro.toPlainText()
        encaminhar = self.ComboMedico.itemText(self.ComboMedico.currentIndex())
        status = self.ComboStatus.itemText(self.ComboStatus.currentIndex())


        try:
            self.conn = sqlite3.connect("Paciente.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO enfermeiro (obsTri, encaminhar, status) VALUES (?,?,?)", (obs,encaminhar,status))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Salvo com sucesso', 'Obs salvo com sucesso')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Erro ao salvar', 'Confira todos os campos')

    def Nova(self):
            self.connection = sqlite3.connect('Paciente.db')
            self.query = "SELECT id, nome, data, hora, obsCliente FROM paciente"
            self.result = self.connection.execute(self.query)
            self.ListaPaciente.setRowCount(0)
            for row_number, row_data in enumerate(self.result):
                self.ListaPaciente.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ListaPaciente.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.ObsPaciente.setText(str(data))
                    self.NomePaciente.setText(str(row_data[1]))
                    self.dtaPaciente.setText(str(row_data[2]))

            self.connection.close()













    def retranslateUi(self, TelaTriagem):
        _translate = QtCore.QCoreApplication.translate
        TelaTriagem.setWindowTitle(_translate("TelaTriagem", "Triagem"))
        self.label.setText(_translate("TelaTriagem", "Fila de Pacientes"))
        item = self.ListaPaciente.horizontalHeaderItem(0)
        item.setText(_translate("TelaTriagem", "Id"))
        item = self.ListaPaciente.horizontalHeaderItem(1)
        item.setText(_translate("TelaTriagem", "Nome"))
        item = self.ListaPaciente.horizontalHeaderItem(2)
        item.setText(_translate("TelaTriagem", "Data"))
        item = self.ListaPaciente.horizontalHeaderItem(3)
        item.setText(_translate("TelaTriagem", "Hora"))
        item = self.ListaPaciente.horizontalHeaderItem(4)
        item.setText(_translate("TelaTriagem", "Observação"))

        self.btnProxTriagem.setText(_translate("TelaTriagem", "Proxímo"))
        self.label_2.setText(_translate("TelaTriagem", "Nome:"))
        self.label_4.setText(_translate("TelaTriagem", "Data:"))
        self.label_6.setText(_translate("TelaTriagem", "Observação do Paciente:"))
        self.label_7.setText(_translate("TelaTriagem", "Observação do enfermeiro:"))
        self.label_8.setText(_translate("TelaTriagem", "Encaminhar para:"))
        self.label_9.setText(_translate("TelaTriagem", "Data:"))
        self.label_11.setText(_translate("TelaTriagem", "Hora:"))
        self.label_13.setText(_translate("TelaTriagem", "Status:"))
        self.btnCancelar.setText(_translate("TelaTriagem", "Cancelar"))
        self.btnAusente.setText(_translate("TelaTriagem", "Ausente"))
        self.btnEncaminhar.setText(_translate("TelaTriagem", "Encaminhar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaTriagem = QtWidgets.QDialog()
    ui = Ui_TelaTriagem()
    ui.setupUi(TelaTriagem)
    TelaTriagem.show()
    sys.exit(app.exec_())
