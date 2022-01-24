# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telachecagem.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_TelaChecagem(object):
    def setupUi(self, TelaChecagem):
        TelaChecagem.setObjectName("TelaChecagem")
        TelaChecagem.resize(637, 435)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/atendimento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaChecagem.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(TelaChecagem)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        TelaChecagem.setModal(True)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.camBuscarPacCheck = QtWidgets.QLineEdit(TelaChecagem)
        self.camBuscarPacCheck.setGeometry(QtCore.QRect(10, 30, 271, 21))
        self.camBuscarPacCheck.setObjectName("camBuscarPacCheck")
        self.btnBuscarPacCheck = QtWidgets.QPushButton(TelaChecagem)
        self.btnBuscarPacCheck.setGeometry(QtCore.QRect(290, 22, 101, 31))
        self.btnBuscarPacCheck.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarPacCheck.setIcon(icon1)
        self.btnBuscarPacCheck.setObjectName("btnBuscarPacCheck")
        self.tableWidgetCons = QtWidgets.QTableWidget(TelaChecagem)
        self.tableWidgetCons.setGeometry(QtCore.QRect(10, 70, 611, 91))
        self.tableWidgetCons.setObjectName("tableWidgetCons")
        self.tableWidgetCons.setColumnCount(6)
        self.tableWidgetCons.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCons.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCons.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCons.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCons.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCons.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCons.setHorizontalHeaderItem(5, item)
        self.editEvolucao = QtWidgets.QTextEdit(TelaChecagem)
        self.editEvolucao.setGeometry(QtCore.QRect(10, 250, 611, 121))
        self.editEvolucao.setObjectName("editEvolucao")
        self.label_2 = QtWidgets.QLabel(TelaChecagem)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(TelaChecagem)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lblNomePaciente = QtWidgets.QLabel(TelaChecagem)
        self.lblNomePaciente.setGeometry(QtCore.QRect(110, 180, 301, 21))
        self.lblNomePaciente.setText("")
        self.lblNomePaciente.setObjectName("lblNomePaciente")
        self.lblLeito = QtWidgets.QLabel(TelaChecagem)
        self.lblLeito.setGeometry(QtCore.QRect(50, 200, 51, 16))
        self.lblLeito.setText("")
        self.lblLeito.setObjectName("lblLeito")
        self.label_4 = QtWidgets.QLabel(TelaChecagem)
        self.label_4.setGeometry(QtCore.QRect(10, 225, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnSalvar = QtWidgets.QPushButton(TelaChecagem)
        self.btnSalvar.setGeometry(QtCore.QRect(504, 380, 111, 31))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagens/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon2)
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnCancerlar = QtWidgets.QPushButton(TelaChecagem)
        self.btnCancerlar.setGeometry(QtCore.QRect(374, 382, 111, 31))
        self.btnCancerlar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../imagens/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancerlar.setIcon(icon3)
        self.btnCancerlar.setObjectName("btnCancerlar")

        self.retranslateUi(TelaChecagem)
        QtCore.QMetaObject.connectSlotsByName(TelaChecagem)
        self.btnCancerlar.clicked.connect(TelaChecagem.close)

        self.btnBuscarPacCheck.clicked.connect(self.Buscar)
        self.btnSalvar.clicked.connect(self.Salvar)


    def Buscar(self):
        self.connection = sqlite3.connect('Paciente.db')
        self.query = "SELECT idInter, nome, leito, ok, medicamento, evo FROM internacao"
        self.result = self.connection.execute(self.query)
        self.tableWidgetCons.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.tableWidgetCons.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetCons.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.lblNomePaciente.setText(str(row_data[1]))
                self.lblLeito.setText(str(row_data[2]))
                self.editEvolucao.setText(str(row_data[5]))
        self.connection.close()

    def Salvar(self):
        evolucao = ""

        evolucao = self.editEvolucao.toPlainText()





        try:
            self.conn = sqlite3.connect("Paciente.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE internacao SET evo = ? ",(evolucao))
            self.conn.commit()
            self.c.close()
            self.conn.close()

            QMessageBox.information(QMessageBox(), 'Salvo com sucesso', 'Obs salvo com sucesso')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Erro ao salvar', 'Confira todos os campos')

    def retranslateUi(self, TelaChecagem):
        _translate = QtCore.QCoreApplication.translate
        TelaChecagem.setWindowTitle(_translate("TelaChecagem", "Checagem de Paciente"))
        self.label.setText(_translate("TelaChecagem", "Buscar Paciente"))
        self.btnBuscarPacCheck.setText(_translate("TelaChecagem", "Buscar"))
        item = self.tableWidgetCons.horizontalHeaderItem(0)
        item.setText(_translate("TelaChecagem", "ID"))
        item = self.tableWidgetCons.horizontalHeaderItem(1)
        item.setText(_translate("TelaChecagem", "Nome"))
        item = self.tableWidgetCons.horizontalHeaderItem(2)
        item.setText(_translate("TelaChecagem", "Leito"))
        item = self.tableWidgetCons.horizontalHeaderItem(3)
        item.setText(_translate("TelaChecagem", "Check"))
        item = self.tableWidgetCons.horizontalHeaderItem(4)
        item.setText(_translate("TelaChecagem", "Medicação"))
        item = self.tableWidgetCons.horizontalHeaderItem(5)
        item.setText(_translate("TelaChecagem", "Quadro de Evolução"))
        self.label_2.setText(_translate("TelaChecagem", "Nome Paciente:"))
        self.label_3.setText(_translate("TelaChecagem", "Leito:"))
        self.label_4.setText(_translate("TelaChecagem", "Evolução"))
        self.btnSalvar.setText(_translate("TelaChecagem", "Salvar"))
        self.btnCancerlar.setText(_translate("TelaChecagem", "Cancelar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaChecagem = QtWidgets.QDialog()
    ui = Ui_TelaChecagem()
    ui.setupUi(TelaChecagem)
    TelaChecagem.show()
    sys.exit(app.exec_())
