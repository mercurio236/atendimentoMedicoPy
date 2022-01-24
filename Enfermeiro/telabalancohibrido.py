# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telabalancohibrido.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_TelaBalancoHibrido(object):
    def setupUi(self, TelaBalancoHibrido):
        TelaBalancoHibrido.setObjectName("TelaBalancoHibrido")
        TelaBalancoHibrido.setFixedSize(542, 620)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/atendimento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaBalancoHibrido.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(TelaBalancoHibrido)
        self.label.setGeometry(QtCore.QRect(20, 200, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        TelaBalancoHibrido.setModal(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.camDiurese = QtWidgets.QLineEdit(TelaBalancoHibrido)
        self.camDiurese.setGeometry(QtCore.QRect(20, 220, 151, 20))
        self.camDiurese.setObjectName("camDiurese")
        self.label_2 = QtWidgets.QLabel(TelaBalancoHibrido)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.camFezes = QtWidgets.QLineEdit(TelaBalancoHibrido)
        self.camFezes.setGeometry(QtCore.QRect(20, 270, 151, 20))
        self.camFezes.setObjectName("camFezes")
        self.label_3 = QtWidgets.QLabel(TelaBalancoHibrido)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.camMedic = QtWidgets.QLineEdit(TelaBalancoHibrido)
        self.camMedic.setGeometry(QtCore.QRect(20, 320, 151, 20))
        self.camMedic.setObjectName("camMedic")
        self.label_4 = QtWidgets.QLabel(TelaBalancoHibrido)
        self.label_4.setGeometry(QtCore.QRect(20, 350, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.camAgua = QtWidgets.QLineEdit(TelaBalancoHibrido)
        self.camAgua.setGeometry(QtCore.QRect(20, 370, 151, 20))
        self.camAgua.setObjectName("camAgua")
        self.label_5 = QtWidgets.QLabel(TelaBalancoHibrido)
        self.label_5.setGeometry(QtCore.QRect(20, 400, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.camAliment = QtWidgets.QLineEdit(TelaBalancoHibrido)
        self.camAliment.setGeometry(QtCore.QRect(20, 420, 151, 20))
        self.camAliment.setObjectName("camAliment")
        self.label_6 = QtWidgets.QLabel(TelaBalancoHibrido)
        self.label_6.setGeometry(QtCore.QRect(20, 460, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.camSalina = QtWidgets.QLineEdit(TelaBalancoHibrido)
        self.camSalina.setGeometry(QtCore.QRect(20, 480, 151, 20))
        self.camSalina.setObjectName("camSalina")
        self.label_7 = QtWidgets.QLabel(TelaBalancoHibrido)
        self.label_7.setGeometry(QtCore.QRect(20, 520, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.camRepo = QtWidgets.QLineEdit(TelaBalancoHibrido)
        self.camRepo.setGeometry(QtCore.QRect(20, 540, 151, 20))
        self.camRepo.setObjectName("camRepo")
        self.groupPeriDiu = QtWidgets.QGroupBox(TelaBalancoHibrido)
        self.groupPeriDiu.setGeometry(QtCore.QRect(190, 200, 301, 56))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupPeriDiu.setFont(font)
        self.groupPeriDiu.setObjectName("groupPeriDiu")
        self.gridLayout = QtWidgets.QGridLayout(self.groupPeriDiu)
        self.gridLayout.setObjectName("gridLayout")
        self.radioM1 = QtWidgets.QRadioButton(self.groupPeriDiu)
        self.radioM1.setObjectName("radioM1")
        self.gridLayout.addWidget(self.radioM1, 0, 0, 1, 1)
        self.radioT1 = QtWidgets.QRadioButton(self.groupPeriDiu)
        self.radioT1.setObjectName("radioT1")
        self.gridLayout.addWidget(self.radioT1, 0, 1, 1, 1)
        self.radioN1 = QtWidgets.QRadioButton(self.groupPeriDiu)
        self.radioN1.setObjectName("radioN1")
        self.gridLayout.addWidget(self.radioN1, 0, 2, 1, 1)
        self.groupPeriFezes = QtWidgets.QGroupBox(TelaBalancoHibrido)
        self.groupPeriFezes.setGeometry(QtCore.QRect(190, 250, 301, 56))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupPeriFezes.setFont(font)
        self.groupPeriFezes.setObjectName("groupPeriFezes")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupPeriFezes)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioM2 = QtWidgets.QRadioButton(self.groupPeriFezes)
        self.radioM2.setObjectName("radioM2")
        self.gridLayout_2.addWidget(self.radioM2, 0, 0, 1, 1)
        self.radioT2 = QtWidgets.QRadioButton(self.groupPeriFezes)
        self.radioT2.setObjectName("radioT2")
        self.gridLayout_2.addWidget(self.radioT2, 0, 1, 1, 1)
        self.radioN2 = QtWidgets.QRadioButton(self.groupPeriFezes)
        self.radioN2.setObjectName("radioN2")
        self.gridLayout_2.addWidget(self.radioN2, 0, 2, 1, 1)
        self.groupPeriMedic = QtWidgets.QGroupBox(TelaBalancoHibrido)
        self.groupPeriMedic.setGeometry(QtCore.QRect(190, 300, 301, 56))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupPeriMedic.setFont(font)
        self.groupPeriMedic.setObjectName("groupPeriMedic")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupPeriMedic)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioM3 = QtWidgets.QRadioButton(self.groupPeriMedic)
        self.radioM3.setObjectName("radioM3")
        self.gridLayout_3.addWidget(self.radioM3, 0, 0, 1, 1)
        self.radioT3 = QtWidgets.QRadioButton(self.groupPeriMedic)
        self.radioT3.setObjectName("radioT3")
        self.gridLayout_3.addWidget(self.radioT3, 0, 1, 1, 1)
        self.radioN3 = QtWidgets.QRadioButton(self.groupPeriMedic)
        self.radioN3.setObjectName("radioN3")
        self.gridLayout_3.addWidget(self.radioN3, 0, 2, 1, 1)
        self.groupPeriAgua = QtWidgets.QGroupBox(TelaBalancoHibrido)
        self.groupPeriAgua.setGeometry(QtCore.QRect(190, 350, 301, 56))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupPeriAgua.setFont(font)
        self.groupPeriAgua.setObjectName("groupPeriAgua")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupPeriAgua)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radioM4 = QtWidgets.QRadioButton(self.groupPeriAgua)
        self.radioM4.setObjectName("radioM4")
        self.gridLayout_4.addWidget(self.radioM4, 0, 0, 1, 1)
        self.radioT4 = QtWidgets.QRadioButton(self.groupPeriAgua)
        self.radioT4.setObjectName("radioT4")
        self.gridLayout_4.addWidget(self.radioT4, 0, 1, 1, 1)
        self.radioN4 = QtWidgets.QRadioButton(self.groupPeriAgua)
        self.radioN4.setObjectName("radioN4")
        self.gridLayout_4.addWidget(self.radioN4, 0, 2, 1, 1)
        self.groupPeriAliment = QtWidgets.QGroupBox(TelaBalancoHibrido)
        self.groupPeriAliment.setGeometry(QtCore.QRect(190, 400, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupPeriAliment.setFont(font)
        self.groupPeriAliment.setObjectName("groupPeriAliment")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupPeriAliment)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioM5 = QtWidgets.QRadioButton(self.groupPeriAliment)
        self.radioM5.setObjectName("radioM5")
        self.gridLayout_5.addWidget(self.radioM5, 0, 0, 1, 1)
        self.radioT5 = QtWidgets.QRadioButton(self.groupPeriAliment)
        self.radioT5.setObjectName("radioT5")
        self.gridLayout_5.addWidget(self.radioT5, 0, 1, 1, 1)
        self.radioN5 = QtWidgets.QRadioButton(self.groupPeriAliment)
        self.radioN5.setObjectName("radioN5")
        self.gridLayout_5.addWidget(self.radioN5, 0, 2, 1, 1)
        self.groupPeriSalina = QtWidgets.QGroupBox(TelaBalancoHibrido)
        self.groupPeriSalina.setGeometry(QtCore.QRect(190, 450, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupPeriSalina.setFont(font)
        self.groupPeriSalina.setObjectName("groupPeriSalina")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupPeriSalina)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.radioM6 = QtWidgets.QRadioButton(self.groupPeriSalina)
        self.radioM6.setObjectName("radioM6")
        self.gridLayout_6.addWidget(self.radioM6, 0, 0, 1, 1)
        self.radioT6 = QtWidgets.QRadioButton(self.groupPeriSalina)
        self.radioT6.setObjectName("radioT6")
        self.gridLayout_6.addWidget(self.radioT6, 0, 1, 1, 1)
        self.radioN6 = QtWidgets.QRadioButton(self.groupPeriSalina)
        self.radioN6.setObjectName("radioN6")
        self.gridLayout_6.addWidget(self.radioN6, 0, 2, 1, 1)
        self.groupPeriRepo = QtWidgets.QGroupBox(TelaBalancoHibrido)
        self.groupPeriRepo.setGeometry(QtCore.QRect(190, 510, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupPeriRepo.setFont(font)
        self.groupPeriRepo.setObjectName("groupPeriRepo")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupPeriRepo)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.radioM7 = QtWidgets.QRadioButton(self.groupPeriRepo)
        self.radioM7.setObjectName("radioM7")
        self.gridLayout_7.addWidget(self.radioM7, 0, 0, 1, 1)
        self.radioT7 = QtWidgets.QRadioButton(self.groupPeriRepo)
        self.radioT7.setObjectName("radioT7")
        self.gridLayout_7.addWidget(self.radioT7, 0, 1, 1, 1)
        self.radioN7 = QtWidgets.QRadioButton(self.groupPeriRepo)
        self.radioN7.setObjectName("radioN7")
        self.gridLayout_7.addWidget(self.radioN7, 0, 2, 1, 1)
        self.btnSalvar = QtWidgets.QPushButton(TelaBalancoHibrido)
        self.btnSalvar.setGeometry(QtCore.QRect(410, 580, 81, 31))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setObjectName("btnSalvar")
        self.lineEdit = QtWidgets.QLineEdit(TelaBalancoHibrido)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 311, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(TelaBalancoHibrido)
        self.label_8.setGeometry(QtCore.QRect(20, 5, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(TelaBalancoHibrido)
        self.pushButton.setGeometry(QtCore.QRect(340, 22, 111, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(TelaBalancoHibrido)
        self.tableWidget.setGeometry(QtCore.QRect(15, 60, 511, 131))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(1)
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

        self.retranslateUi(TelaBalancoHibrido)
        QtCore.QMetaObject.connectSlotsByName(TelaBalancoHibrido)

        #Botões
        self.pushButton.clicked.connect(self.Atualizar)
        self.btnSalvar.clicked.connect(self.Salvar)



        #Functions

    def Atualizar(self):
        self.connection = sqlite3.connect('Paciente.db')
        self.query = "SELECT * FROM internacao"
        self.result = self.connection.execute(self.query)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.camDiurese.setText(str(row_data[3]))
                self.camFezes.setText(str(row_data[4]))
                self.camMedic.setText(str(row_data[5]))
                self.camAgua.setText(str(row_data[6]))
                self.camAliment.setText(str(row_data[7]))
                self.camSalina.setText(str(row_data[9]))
                self.camRepo.setText(str(row_data[10]))
        self.connection.close()


        pesquisa = ""
        pesquisa = self.lineEdit.text()

        try:

            self.conn = sqlite3.connect("Paciente.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT nome FROM internacao"+str(pesquisa))
            row = result.fetchone()
            resultado = "Nome: "+str(row[1])
            QMessageBox.Information(QMessageBox(), 'Sucesso', resultado)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Error')

    def Salvar(self):
        try:
            QMessageBox.information(QMessageBox(), 'Sucesso', 'Salvo com sucesso')
            TelaBalancoHibrido.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Erro', 'Erro ao salvar')











    def retranslateUi(self, TelaBalancoHibrido):
        _translate = QtCore.QCoreApplication.translate
        TelaBalancoHibrido.setWindowTitle(_translate("TelaBalancoHibrido", "Balanço Híbrido"))
        self.label.setText(_translate("TelaBalancoHibrido", "Diurése"))
        self.label_2.setText(_translate("TelaBalancoHibrido", "Fezes"))
        self.label_3.setText(_translate("TelaBalancoHibrido", "Medicação"))
        self.label_4.setText(_translate("TelaBalancoHibrido", "Água"))
        self.label_5.setText(_translate("TelaBalancoHibrido", "Alimentação"))
        self.label_6.setText(_translate("TelaBalancoHibrido", "Salina"))
        self.label_7.setText(_translate("TelaBalancoHibrido", "Reposição"))
        self.groupPeriDiu.setTitle(_translate("TelaBalancoHibrido", "Periodo"))
        self.radioM1.setText(_translate("TelaBalancoHibrido", "Manhã"))
        self.radioT1.setText(_translate("TelaBalancoHibrido", "Tarde"))
        self.radioN1.setText(_translate("TelaBalancoHibrido", "Noite"))
        self.groupPeriFezes.setTitle(_translate("TelaBalancoHibrido", "Periodo"))
        self.radioM2.setText(_translate("TelaBalancoHibrido", "Manhã"))
        self.radioT2.setText(_translate("TelaBalancoHibrido", "Tarde"))
        self.radioN2.setText(_translate("TelaBalancoHibrido", "Noite"))
        self.groupPeriMedic.setTitle(_translate("TelaBalancoHibrido", "Periodo"))
        self.radioM3.setText(_translate("TelaBalancoHibrido", "Manhã"))
        self.radioT3.setText(_translate("TelaBalancoHibrido", "Tarde"))
        self.radioN3.setText(_translate("TelaBalancoHibrido", "Noite"))
        self.groupPeriAgua.setTitle(_translate("TelaBalancoHibrido", "Periodo"))
        self.radioM4.setText(_translate("TelaBalancoHibrido", "Manhã"))
        self.radioT4.setText(_translate("TelaBalancoHibrido", "Tarde"))
        self.radioN4.setText(_translate("TelaBalancoHibrido", "Noite"))
        self.groupPeriAliment.setTitle(_translate("TelaBalancoHibrido", "Periodo"))
        self.radioM5.setText(_translate("TelaBalancoHibrido", "Manhã"))
        self.radioT5.setText(_translate("TelaBalancoHibrido", "Tarde"))
        self.radioN5.setText(_translate("TelaBalancoHibrido", "Noite"))
        self.groupPeriSalina.setTitle(_translate("TelaBalancoHibrido", "Periodo"))
        self.radioM6.setText(_translate("TelaBalancoHibrido", "Manhã"))
        self.radioT6.setText(_translate("TelaBalancoHibrido", "Tarde"))
        self.radioN6.setText(_translate("TelaBalancoHibrido", "Noite"))
        self.groupPeriRepo.setTitle(_translate("TelaBalancoHibrido", "Periodo"))
        self.radioM7.setText(_translate("TelaBalancoHibrido", "Manhã"))
        self.radioT7.setText(_translate("TelaBalancoHibrido", "Tarde"))
        self.radioN7.setText(_translate("TelaBalancoHibrido", "Noite"))
        self.btnSalvar.setText(_translate("TelaBalancoHibrido", "Salvar"))
        self.label_8.setText(_translate("TelaBalancoHibrido", "Buscar Paciente:"))
        self.pushButton.setText(_translate("TelaBalancoHibrido", "Buscar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TelaBalancoHibrido", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TelaBalancoHibrido", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TelaBalancoHibrido", "Leito"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TelaBalancoHibrido", "Diurese"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("TelaBalancoHibrido", "Fezes"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("TelaBalancoHibrido", "Medicacao"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("TelaBalancoHibrido", "agua"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("TelaBalancoHibrido", "aliementacao"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("TelaBalancoHibrido", "salina"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("TelaBalancoHibrido", "reposicao"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("TelaBalancoHibrido", "Periodo"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaBalancoHibrido = QtWidgets.QDialog()
    ui = Ui_TelaBalancoHibrido()
    ui.setupUi(TelaBalancoHibrido)
    TelaBalancoHibrido.show()
    sys.exit(app.exec_())
