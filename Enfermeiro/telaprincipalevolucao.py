# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaprincipalevolucao.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaPrincipalEvolucao(object):
    def setupUi(self, TelaPrincipalEvolucao):
        TelaPrincipalEvolucao.setObjectName("TelaPrincipalEvolucao")
        TelaPrincipalEvolucao.setFixedSize(756, 360)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/enfermeira.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaPrincipalEvolucao.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(TelaPrincipalEvolucao)
        self.label.setGeometry(QtCore.QRect(20, 0, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pacienteInternado = QtWidgets.QTableWidget(TelaPrincipalEvolucao)
        self.pacienteInternado.setGeometry(QtCore.QRect(10, 40, 731, 192))
        self.pacienteInternado.setObjectName("pacienteInternado")
        self.pacienteInternado.setColumnCount(0)
        self.pacienteInternado.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(TelaPrincipalEvolucao)
        self.label_2.setGeometry(QtCore.QRect(10, 245, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(TelaPrincipalEvolucao)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(TelaPrincipalEvolucao)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.camNomePac = QtWidgets.QLabel(TelaPrincipalEvolucao)
        self.camNomePac.setGeometry(QtCore.QRect(140, 245, 291, 21))
        self.camNomePac.setText("")
        self.camNomePac.setObjectName("camNomePac")
        self.camDtaPac = QtWidgets.QLabel(TelaPrincipalEvolucao)
        self.camDtaPac.setGeometry(QtCore.QRect(130, 265, 111, 31))
        self.camDtaPac.setText("")
        self.camDtaPac.setObjectName("camDtaPac")
        self.camLtPac = QtWidgets.QLabel(TelaPrincipalEvolucao)
        self.camLtPac.setGeometry(QtCore.QRect(50, 285, 91, 31))
        self.camLtPac.setText("")
        self.camLtPac.setObjectName("camLtPac")
        self.scrollArea = QtWidgets.QScrollArea(TelaPrincipalEvolucao)
        self.scrollArea.setGeometry(QtCore.QRect(410, 300, 331, 51))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 49))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.btnConsulta = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConsulta.setIcon(icon1)
        self.btnConsulta.setObjectName("btnConsulta")
        self.gridLayout.addWidget(self.btnConsulta, 0, 0, 1, 1)
        self.btnEvoluir = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnEvoluir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagens/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEvoluir.setIcon(icon2)
        self.btnEvoluir.setObjectName("btnEvoluir")
        self.gridLayout.addWidget(self.btnEvoluir, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(TelaPrincipalEvolucao)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipalEvolucao)

    def retranslateUi(self, TelaPrincipalEvolucao):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipalEvolucao.setWindowTitle(_translate("TelaPrincipalEvolucao", "Tela Principal"))
        self.label.setText(_translate("TelaPrincipalEvolucao", "Pacientes Internados"))
        self.label_2.setText(_translate("TelaPrincipalEvolucao", "Nome do Paciente:"))
        self.label_3.setText(_translate("TelaPrincipalEvolucao", "Data de entrada:"))
        self.label_4.setText(_translate("TelaPrincipalEvolucao", "Leito:"))
        self.btnConsulta.setText(_translate("TelaPrincipalEvolucao", "Consuta Paciente"))
        self.btnEvoluir.setText(_translate("TelaPrincipalEvolucao", "Evoluir"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipalEvolucao = QtWidgets.QDialog()
    ui = Ui_TelaPrincipalEvolucao()
    ui.setupUi(TelaPrincipalEvolucao)
    TelaPrincipalEvolucao.show()
    sys.exit(app.exec_())
