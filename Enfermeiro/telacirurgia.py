# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telacirurgia.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_TelaCirurgia(object):
    def setupUi(self, TelaCirurgia):
        TelaCirurgia.setObjectName("TelaCirurgia")
        TelaCirurgia.setWindowModality(QtCore.Qt.NonModal)
        TelaCirurgia.setFixedSize(596, 417)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/atendimento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaCirurgia.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(TelaCirurgia)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        TelaCirurgia.setModal(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(TelaCirurgia)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 321, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(TelaCirurgia)
        self.pushButton.setGeometry(QtCore.QRect(340, 22, 101, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(TelaCirurgia)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 571, 111))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label_2 = QtWidgets.QLabel(TelaCirurgia)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(TelaCirurgia)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 47, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lblNome = QtWidgets.QLabel(TelaCirurgia)
        self.lblNome.setGeometry(QtCore.QRect(60, 190, 241, 21))
        self.lblNome.setText("")
        self.lblNome.setObjectName("lblNome")
        self.lblLeito = QtWidgets.QLabel(TelaCirurgia)
        self.lblLeito.setGeometry(QtCore.QRect(50, 210, 71, 21))
        self.lblLeito.setText("")
        self.lblLeito.setObjectName("lblLeito")
        self.editCirurgia = QtWidgets.QTextEdit(TelaCirurgia)
        self.editCirurgia.setGeometry(QtCore.QRect(10, 240, 571, 111))
        self.editCirurgia.setObjectName("editCirurgia")
        self.btnSalvar = QtWidgets.QPushButton(TelaCirurgia)
        self.btnSalvar.setGeometry(QtCore.QRect(474, 370, 101, 31))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagens/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon2)
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnCancelar = QtWidgets.QPushButton(TelaCirurgia)
        self.btnCancelar.setGeometry(QtCore.QRect(344, 370, 111, 31))
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../imagens/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon3)
        self.btnCancelar.setObjectName("btnCancelar")

        self.retranslateUi(TelaCirurgia)
        QtCore.QMetaObject.connectSlotsByName(TelaCirurgia)

        self.btnCancelar.clicked.connect(TelaCirurgia.close)
        self.pushButton.clicked.connect(self.Buscar)
        self.btnSalvar.clicked.connect(self.Salvar)

    def Buscar(self):
        self.connection = sqlite3.connect('Paciente.db')
        self.query = "SELECT idInter,leito, nome, evo FROM internacao"
        self.result = self.connection.execute(self.query)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.lblNome.setText(str(row_data[2]))
                self.lblLeito.setText(str(row_data[1]))
                self.editCirurgia.setText(str(row_data[3]))
        self.connection.close()

    def Salvar(self):
        evolucao = ""

        evolucao = self.editCirurgia.toPlainText()





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

    def retranslateUi(self, TelaCirurgia):
        _translate = QtCore.QCoreApplication.translate
        TelaCirurgia.setWindowTitle(_translate("TelaCirurgia", "Cirurgia"))
        self.label.setText(_translate("TelaCirurgia", "Busca Paciente"))
        self.pushButton.setText(_translate("TelaCirurgia", "Buscar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TelaCirurgia", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TelaCirurgia", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TelaCirurgia", "Leito"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TelaCirurgia", "Evolução"))
        self.label_2.setText(_translate("TelaCirurgia", "Nome:"))
        self.label_3.setText(_translate("TelaCirurgia", "Leito:"))
        self.btnSalvar.setText(_translate("TelaCirurgia", "Salvar"))
        self.btnCancelar.setText(_translate("TelaCirurgia", "Cancerlar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaCirurgia = QtWidgets.QDialog()
    ui = Ui_TelaCirurgia()
    ui.setupUi(TelaCirurgia)
    TelaCirurgia.show()
    sys.exit(app.exec_())
