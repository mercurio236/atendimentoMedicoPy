# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaprincipalmedico.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from Enfermeiro.telaevolucaomedica import Ui_EvolucaoMedica
from Enfermeiro.telacirurgia import Ui_TelaCirurgia
from medico.telaprincipalmedicamento import Ui_TelaPrincipalMedicamento
from medico.telamedico import Ui_TelaMedico

class Ui_TelaPrincipalMedico(object):
    def setupUi(self, TelaPrincipalMedico):
        TelaPrincipalMedico.setObjectName("TelaPrincipalMedico")
        TelaPrincipalMedico.setFixedSize(681, 532)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/medico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaPrincipalMedico.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TelaPrincipalMedico)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 661, 161))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 240, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 47, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(50, 240, 291, 16))
        self.lblNome.setText("")
        self.lblNome.setObjectName("lblNome")
        self.lblLeito = QtWidgets.QLabel(self.centralwidget)
        self.lblLeito.setGeometry(QtCore.QRect(40, 260, 61, 16))
        self.lblLeito.setText("")
        self.lblLeito.setObjectName("lblLeito")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 340, 661, 111))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 309, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.camBuscar = QtWidgets.QLineEdit(self.centralwidget)
        self.camBuscar.setGeometry(QtCore.QRect(10, 30, 311, 21))
        self.camBuscar.setObjectName("camBuscar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(330, 22, 131, 31))
        self.btnBuscar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon1)
        self.btnBuscar.setObjectName("btnBuscar")
        TelaPrincipalMedico.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaPrincipalMedico)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 21))
        self.menubar.setObjectName("menubar")
        self.menuMedico = QtWidgets.QMenu(self.menubar)
        self.menuMedico.setObjectName("menuMedico")
        self.menuMedicamentos = QtWidgets.QMenu(self.menubar)
        self.menuMedicamentos.setObjectName("menuMedicamentos")
        TelaPrincipalMedico.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaPrincipalMedico)
        self.statusbar.setObjectName("statusbar")
        TelaPrincipalMedico.setStatusBar(self.statusbar)
        self.actionAtendimentoMed = QtWidgets.QAction(TelaPrincipalMedico)
        self.actionAtendimentoMed.setObjectName("actionAtendimentoMed")
        self.actionEvolu_o = QtWidgets.QAction(TelaPrincipalMedico)
        self.actionEvolu_o.setObjectName("actionEvolu_o")
        self.actionCirurgia = QtWidgets.QAction(TelaPrincipalMedico)
        self.actionCirurgia.setObjectName("actionCirurgia")
        self.actionSair = QtWidgets.QAction(TelaPrincipalMedico)
        self.actionSair.setObjectName("actionSair")
        self.actionMedica_o = QtWidgets.QAction(TelaPrincipalMedico)
        self.actionMedica_o.setObjectName("actionMedica_o")
        self.actionSAir = QtWidgets.QAction(TelaPrincipalMedico)
        self.actionSAir.setObjectName("actionSAir")
        self.menuMedico.addAction(self.actionEvolu_o)
        self.menuMedico.addAction(self.actionCirurgia)
        self.menuMedico.addAction(self.actionAtendimentoMed)
        self.menuMedico.addSeparator()
        self.menuMedico.addAction(self.actionSAir)
        self.menuMedicamentos.addAction(self.actionMedica_o)
        self.menubar.addAction(self.menuMedico.menuAction())
        self.menubar.addAction(self.menuMedicamentos.menuAction())

        self.retranslateUi(TelaPrincipalMedico)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipalMedico)

        #Botões para actions
        self.actionSAir.triggered.connect(TelaPrincipalMedico.close)
        self.actionEvolu_o.triggered.connect(self.Evolucao)
        self.actionCirurgia.triggered.connect(self.Cirurgia)
        self.actionMedica_o.triggered.connect(self.Medicamento)
        self.actionAtendimentoMed.triggered.connect(self.Atendimento)
        self.btnBuscar.clicked.connect(self.Nova)


    #Função para Actons

    def Evolucao(self):
        EvolucaoMedica = QtWidgets.QDialog()
        ui = Ui_EvolucaoMedica()
        ui.setupUi(EvolucaoMedica)
        EvolucaoMedica.show()
        EvolucaoMedica.exec_()

    def Cirurgia(self):
        TelaCirurgia = QtWidgets.QDialog()
        ui = Ui_TelaCirurgia()
        ui.setupUi(TelaCirurgia)
        TelaCirurgia.show()
        TelaCirurgia.exec_()

    def Medicamento(self):
        TelaPrincipalMedicamento = QtWidgets.QDialog()
        ui = Ui_TelaPrincipalMedicamento()
        ui.setupUi(TelaPrincipalMedicamento)
        TelaPrincipalMedicamento.show()
        TelaPrincipalMedicamento.exec_()

    def Atendimento(self):
        TelaMedico = QtWidgets.QDialog()
        ui = Ui_TelaMedico()
        ui.setupUi(TelaMedico)
        TelaMedico.show()
        TelaMedico.exec_()

    def Nova(self):
            connection = sqlite3.connect('Paciente.db')
            query = "SELECT idInter, nome, leito FROM internacao"
            result = connection.execute(query)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    self.textEdit.setText(str(row_data[2]))



            connection.close()


    def retranslateUi(self, TelaPrincipalMedico):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipalMedico.setWindowTitle(_translate("TelaPrincipalMedico", "Medico"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TelaPrincipalMedico", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TelaPrincipalMedico", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TelaPrincipalMedico", "Leito"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TelaPrincipalMedico", "Observação Medica"))
        self.label.setText(_translate("TelaPrincipalMedico", "Nome:"))
        self.label_2.setText(_translate("TelaPrincipalMedico", "Leito:"))
        self.label_3.setText(_translate("TelaPrincipalMedico", "Observações"))
        self.label_4.setText(_translate("TelaPrincipalMedico", "Buscar Paciente"))
        self.btnBuscar.setText(_translate("TelaPrincipalMedico", "Buscar"))
        self.menuMedico.setTitle(_translate("TelaPrincipalMedico", "Medico"))
        self.menuMedicamentos.setTitle(_translate("TelaPrincipalMedico", "Medicamentos"))
        self.actionAtendimentoMed.setText(_translate("TelaPrincipalMedico", "Atendimento Medico"))
        self.actionEvolu_o.setText(_translate("TelaPrincipalMedico", "Evolução"))
        self.actionCirurgia.setText(_translate("TelaPrincipalMedico", "Cirurgia"))
        self.actionSair.setText(_translate("TelaPrincipalMedico", "Sair"))
        self.actionMedica_o.setText(_translate("TelaPrincipalMedico", "Medicação"))
        self.actionSAir.setText(_translate("TelaPrincipalMedico", "Sair"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipalMedico = QtWidgets.QMainWindow()
    ui = Ui_TelaPrincipalMedico()
    ui.setupUi(TelaPrincipalMedico)
    TelaPrincipalMedico.show()
    sys.exit(app.exec_())
