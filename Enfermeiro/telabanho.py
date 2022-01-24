# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telabanho.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaBanho(object):
    def setupUi(self, TelaBanho):
        TelaBanho.setObjectName("TelaBanho")
        TelaBanho.resize(472, 169)
        self.label = QtWidgets.QLabel(TelaBanho)
        self.label.setGeometry(QtCore.QRect(9, 9, 117, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        TelaBanho.setModal(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.camPesquisaBanho = QtWidgets.QLineEdit(TelaBanho)
        self.camPesquisaBanho.setGeometry(QtCore.QRect(9, 31, 231, 20))
        self.camPesquisaBanho.setObjectName("camPesquisaBanho")
        self.pacienteBanho = QtWidgets.QTableWidget(TelaBanho)
        self.pacienteBanho.setGeometry(QtCore.QRect(9, 57, 454, 103))
        self.pacienteBanho.setObjectName("pacienteBanho")
        self.pacienteBanho.setColumnCount(4)
        self.pacienteBanho.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.pacienteBanho.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pacienteBanho.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pacienteBanho.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pacienteBanho.setHorizontalHeaderItem(3, item)
        self.btnPesquisarBanho = QtWidgets.QPushButton(TelaBanho)
        self.btnPesquisarBanho.setGeometry(QtCore.QRect(250, 20, 81, 31))
        self.btnPesquisarBanho.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPesquisarBanho.setObjectName("btnPesquisarBanho")

        self.retranslateUi(TelaBanho)
        QtCore.QMetaObject.connectSlotsByName(TelaBanho)

        self.btnPesquisarBanho.clicked.connect(self.Buscar)



    def Buscar(self):
        self.connection = sqlite3.connect('Paciente.db')
        self.query = "SELECT idInter, nome, leito FROM internacao"
        self.result = self.connection.execute(self.query)
        self.pacienteBanho.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.pacienteBanho.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.pacienteBanho.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.connection.close()

    def retranslateUi(self, TelaBanho):
        _translate = QtCore.QCoreApplication.translate
        TelaBanho.setWindowTitle(_translate("TelaBanho", "Banho"))
        self.label.setText(_translate("TelaBanho", "Pesquisa Paciente"))
        item = self.pacienteBanho.horizontalHeaderItem(0)
        item.setText(_translate("TelaBanho", "ID"))
        item = self.pacienteBanho.horizontalHeaderItem(1)
        item.setText(_translate("TelaBanho", "Nome"))
        item = self.pacienteBanho.horizontalHeaderItem(2)
        item.setText(_translate("TelaBanho", "Leito"))
        item = self.pacienteBanho.horizontalHeaderItem(3)
        item.setText(_translate("TelaBanho", "Check"))
        self.btnPesquisarBanho.setText(_translate("TelaBanho", "Pesquisar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaBanho = QtWidgets.QDialog()
    ui = Ui_TelaBanho()
    ui.setupUi(TelaBanho)
    TelaBanho.show()
    sys.exit(app.exec_())
