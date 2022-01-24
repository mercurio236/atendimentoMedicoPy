# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaevolucaomedica.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_EvolucaoMedica(object):
    def setupUi(self, EvolucaoMedica):
        EvolucaoMedica.setObjectName("EvolucaoMedica")
        EvolucaoMedica.setFixedSize(606, 410)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/atendimento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EvolucaoMedica.setWindowIcon(icon)
        self.lblLeito = QtWidgets.QLabel(EvolucaoMedica)
        self.lblLeito.setGeometry(QtCore.QRect(56, 200, 71, 21))
        self.lblLeito.setText("")
        self.lblLeito.setObjectName("lblLeito")
        self.btnCancelar = QtWidgets.QPushButton(EvolucaoMedica)
        self.btnCancelar.setGeometry(QtCore.QRect(350, 360, 111, 31))
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon1)
        self.btnCancelar.setObjectName("btnCancelar")
        self.label = QtWidgets.QLabel(EvolucaoMedica)
        self.label.setGeometry(QtCore.QRect(16, 0, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(EvolucaoMedica)
        self.label_3.setGeometry(QtCore.QRect(16, 200, 47, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(EvolucaoMedica)
        self.tableWidget.setGeometry(QtCore.QRect(16, 50, 571, 111))
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
        self.editCirurgia = QtWidgets.QTextEdit(EvolucaoMedica)
        self.editCirurgia.setGeometry(QtCore.QRect(16, 230, 571, 111))
        self.editCirurgia.setObjectName("editCirurgia")
        self.label_2 = QtWidgets.QLabel(EvolucaoMedica)
        self.label_2.setGeometry(QtCore.QRect(16, 180, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        EvolucaoMedica.setModal(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblNome = QtWidgets.QLabel(EvolucaoMedica)
        self.lblNome.setGeometry(QtCore.QRect(66, 180, 241, 21))
        self.lblNome.setText("")
        self.lblNome.setObjectName("lblNome")
        self.pushButton = QtWidgets.QPushButton(EvolucaoMedica)
        self.pushButton.setGeometry(QtCore.QRect(346, 12, 101, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(EvolucaoMedica)
        self.lineEdit.setGeometry(QtCore.QRect(16, 20, 321, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.btnSalvar = QtWidgets.QPushButton(EvolucaoMedica)
        self.btnSalvar.setGeometry(QtCore.QRect(480, 360, 101, 31))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../imagens/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon3)
        self.btnSalvar.setObjectName("btnSalvar")

        self.retranslateUi(EvolucaoMedica)
        QtCore.QMetaObject.connectSlotsByName(EvolucaoMedica)
        self.btnCancelar.clicked.connect(EvolucaoMedica.close)

        self.pushButton.clicked.connect(self.Buscar)
        self.btnSalvar.clicked.connect(self.Editar)


    def Buscar(self):
        self.connection = sqlite3.connect('Paciente.db')
        self.query = "SELECT idInter, nome, leito, evo FROM internacao"
        self.result = self.connection.execute(self.query)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.lblNome.setText(str(row_data[1]))
                self.lblLeito.setText(str(row_data[2]))
                self.editCirurgia.setText(str(row_data[3]))

        self.connection.close()

    def Editar(self):
        evolucao = ""

        evolucao = self.editCirurgia.toPlainText()

        try:
            self.conn = sqlite3.connect("Paciente.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE internacao SET evo = ? ", (evolucao))
            self.conn.commit()
            self.c.close()
            self.conn.close()

            QMessageBox.information(QMessageBox(), 'Salvo com sucesso', 'Obs salvo com sucesso')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Erro ao salvar', 'Confira todos os campos')

    def retranslateUi(self, EvolucaoMedica):
        _translate = QtCore.QCoreApplication.translate
        EvolucaoMedica.setWindowTitle(_translate("EvolucaoMedica", "Evolução"))
        self.btnCancelar.setText(_translate("EvolucaoMedica", "Cancerlar"))
        self.label.setText(_translate("EvolucaoMedica", "Busca Paciente"))
        self.label_3.setText(_translate("EvolucaoMedica", "Leito:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("EvolucaoMedica", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("EvolucaoMedica", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("EvolucaoMedica", "Leito"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("EvolucaoMedica", "Evolução"))
        self.label_2.setText(_translate("EvolucaoMedica", "Nome:"))
        self.pushButton.setText(_translate("EvolucaoMedica", "Buscar"))
        self.btnSalvar.setText(_translate("EvolucaoMedica", "Salvar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvolucaoMedica = QtWidgets.QDialog()
    ui = Ui_EvolucaoMedica()
    ui.setupUi(EvolucaoMedica)
    EvolucaoMedica.show()
    sys.exit(app.exec_())
