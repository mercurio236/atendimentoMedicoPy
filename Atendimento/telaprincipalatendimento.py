# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaprincipalatendimento.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Atendimento.telaconsulta import Ui_TelaConsulta
from Atendimento.telaatendimento import Ui_TelaAtendimento


class Ui_TelaPrincipalAtendimento(object):
    def setupUi(self, TelaPrincipalAtendimento):
        TelaPrincipalAtendimento.setObjectName("TelaPrincipalAtendimento")
        TelaPrincipalAtendimento.resize(517, 421)
        TelaPrincipalAtendimento.setMouseTracking(False)
        TelaPrincipalAtendimento.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/atendimento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaPrincipalAtendimento.setWindowIcon(icon)
        TelaPrincipalAtendimento.setAutoFillBackground(False)
        TelaPrincipalAtendimento.setStyleSheet("QDialog{\n"
"    background: white;\n"
"}")
        self.line = QtWidgets.QFrame(TelaPrincipalAtendimento)
        self.line.setGeometry(QtCore.QRect(240, 0, 20, 191))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(TelaPrincipalAtendimento)
        self.label.setGeometry(QtCore.QRect(310, 20, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(TelaPrincipalAtendimento)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(TelaPrincipalAtendimento)
        self.pushButton.setGeometry(QtCore.QRect(84, 82, 81, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background: green;\n"
"    color: white;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(TelaPrincipalAtendimento)
        self.pushButton_2.setGeometry(QtCore.QRect(334, 82, 81, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background: green;\n"
"    color: white;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(TelaPrincipalAtendimento)
        self.label_3.setGeometry(QtCore.QRect(170, 220, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(TelaPrincipalAtendimento)
        self.listWidget.setGeometry(QtCore.QRect(5, 251, 501, 151))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(TelaPrincipalAtendimento)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipalAtendimento)

        self.pushButton_2.clicked.connect(self.Cadastro)
        self.pushButton.clicked.connect(self.Consulta)

    def Cadastro(self):
        TelaConsulta = QtWidgets.QDialog()
        ui = Ui_TelaConsulta()
        ui.setupUi(TelaConsulta)
        TelaConsulta.show()
        TelaConsulta.exec_()

    def Consulta(self):
        TelaAtendimento = QtWidgets.QDialog()
        ui = Ui_TelaAtendimento()
        ui.setupUi(TelaAtendimento)
        TelaAtendimento.show()
        TelaAtendimento.exec_()

    def retranslateUi(self, TelaPrincipalAtendimento):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipalAtendimento.setWindowTitle(_translate("TelaPrincipalAtendimento", "Tela Principal"))
        self.label.setText(_translate("TelaPrincipalAtendimento", "Consultar ficha"))
        self.label_2.setText(_translate("TelaPrincipalAtendimento", "Abrir ficha"))
        self.pushButton.setText(_translate("TelaPrincipalAtendimento", "Abrir"))
        self.pushButton_2.setText(_translate("TelaPrincipalAtendimento", "Consultar"))
        self.label_3.setText(_translate("TelaPrincipalAtendimento", "Historicos de fichas"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipalAtendimento = QtWidgets.QDialog()
    ui = Ui_TelaPrincipalAtendimento()
    ui.setupUi(TelaPrincipalAtendimento)
    TelaPrincipalAtendimento.show()
    sys.exit(app.exec_())
