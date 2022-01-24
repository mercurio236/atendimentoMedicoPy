# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telafralda.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaFralda(object):
    def setupUi(self, TelaFralda):
        TelaFralda.setObjectName("TelaFralda")
        TelaFralda.resize(461, 196)
        self.label = QtWidgets.QLabel(TelaFralda)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        TelaFralda.setModal(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.camPacienteFralda = QtWidgets.QLineEdit(TelaFralda)
        self.camPacienteFralda.setGeometry(QtCore.QRect(20, 40, 271, 21))
        self.camPacienteFralda.setObjectName("camPacienteFralda")
        self.btnPesquisarFralda = QtWidgets.QPushButton(TelaFralda)
        self.btnPesquisarFralda.setGeometry(QtCore.QRect(300, 32, 91, 31))
        self.btnPesquisarFralda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPesquisarFralda.setObjectName("btnPesquisarFralda")
        self.pesquisaPacienteFralda = QtWidgets.QTableWidget(TelaFralda)
        self.pesquisaPacienteFralda.setGeometry(QtCore.QRect(20, 80, 421, 91))
        self.pesquisaPacienteFralda.setObjectName("pesquisaPacienteFralda")
        self.pesquisaPacienteFralda.setColumnCount(4)
        self.pesquisaPacienteFralda.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.pesquisaPacienteFralda.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pesquisaPacienteFralda.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pesquisaPacienteFralda.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pesquisaPacienteFralda.setHorizontalHeaderItem(3, item)

        self.retranslateUi(TelaFralda)
        QtCore.QMetaObject.connectSlotsByName(TelaFralda)
        self.btnPesquisarFralda.clicked.connect(self.Buscar)

    def Buscar(self):
        self.connection = sqlite3.connect('Paciente.db')
        self.query = "SELECT idInter, nome, leito, ok FROM internacao"
        self.result = self.connection.execute(self.query)
        self.pesquisaPacienteFralda.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.pesquisaPacienteFralda.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.pesquisaPacienteFralda.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.connection.close()

    def retranslateUi(self, TelaFralda):
        _translate = QtCore.QCoreApplication.translate
        TelaFralda.setWindowTitle(_translate("TelaFralda", "Troca de Fralda"))
        self.label.setText(_translate("TelaFralda", "Pesquisar Paciente"))
        self.btnPesquisarFralda.setText(_translate("TelaFralda", "Pesquisar"))
        item = self.pesquisaPacienteFralda.horizontalHeaderItem(0)
        item.setText(_translate("TelaFralda", "ID"))
        item = self.pesquisaPacienteFralda.horizontalHeaderItem(1)
        item.setText(_translate("TelaFralda", "Nome"))
        item = self.pesquisaPacienteFralda.horizontalHeaderItem(2)
        item.setText(_translate("TelaFralda", "Leito"))
        item = self.pesquisaPacienteFralda.horizontalHeaderItem(3)
        item.setText(_translate("TelaFralda", "Check"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaFralda = QtWidgets.QDialog()
    ui = Ui_TelaFralda()
    ui.setupUi(TelaFralda)
    TelaFralda.show()
    sys.exit(app.exec_())
