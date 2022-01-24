# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaconsultaresultado.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaConsultaResultado(object):
    def setupUi(self, TelaConsultaResultado):
        TelaConsultaResultado.setObjectName("TelaConsultaResultado")
        TelaConsultaResultado.resize(647, 721)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/atendimento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaConsultaResultado.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(TelaConsultaResultado)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        TelaConsultaResultado.setModal(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(TelaConsultaResultado)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(TelaConsultaResultado)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.nFicha = QtWidgets.QLabel(TelaConsultaResultado)
        self.nFicha.setGeometry(QtCore.QRect(110, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nFicha.setFont(font)
        self.nFicha.setText("")
        self.nFicha.setObjectName("nFicha")
        self.nomePaciente = QtWidgets.QLabel(TelaConsultaResultado)
        self.nomePaciente.setGeometry(QtCore.QRect(150, 30, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nomePaciente.setFont(font)
        self.nomePaciente.setText("")
        self.nomePaciente.setObjectName("nomePaciente")
        self.DtaEntrada = QtWidgets.QLabel(TelaConsultaResultado)
        self.DtaEntrada.setGeometry(QtCore.QRect(140, 55, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DtaEntrada.setFont(font)
        self.DtaEntrada.setText("")
        self.DtaEntrada.setObjectName("DtaEntrada")
        self.line = QtWidgets.QFrame(TelaConsultaResultado)
        self.line.setGeometry(QtCore.QRect(0, 80, 651, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget = QtWidgets.QListWidget(TelaConsultaResultado)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 631, 561))
        self.listWidget.setObjectName("listWidget")
        self.scrollArea = QtWidgets.QScrollArea(TelaConsultaResultado)
        self.scrollArea.setGeometry(QtCore.QRect(330, 663, 311, 51))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 49))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.btnCancelar = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon1)
        self.btnCancelar.setObjectName("btnCancelar")
        self.gridLayout.addWidget(self.btnCancelar, 0, 0, 1, 1)
        self.btnImprimir = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnImprimir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnImprimir.setObjectName("btnImprimir")
        self.gridLayout.addWidget(self.btnImprimir, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(TelaConsultaResultado)
        QtCore.QMetaObject.connectSlotsByName(TelaConsultaResultado)
        self.btnCancelar.clicked.connect(TelaConsultaResultado.close)

    def retranslateUi(self, TelaConsultaResultado):
        _translate = QtCore.QCoreApplication.translate
        TelaConsultaResultado.setWindowTitle(_translate("TelaConsultaResultado", "Resultados"))
        self.label.setText(_translate("TelaConsultaResultado", "N° da ficha:"))
        self.label_2.setText(_translate("TelaConsultaResultado", "Nome do Paciente:"))
        self.label_3.setText(_translate("TelaConsultaResultado", "Data de entrada:"))
        self.btnCancelar.setText(_translate("TelaConsultaResultado", "Cancelar"))
        self.btnImprimir.setText(_translate("TelaConsultaResultado", "Imprimir"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaConsultaResultado = QtWidgets.QDialog()
    ui = Ui_TelaConsultaResultado()
    ui.setupUi(TelaConsultaResultado)
    TelaConsultaResultado.show()
    sys.exit(app.exec_())
