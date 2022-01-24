# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaconsulta.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaConsulta(object):
    def setupUi(self, TelaConsulta):
        TelaConsulta.setObjectName("TelaConsulta")
        TelaConsulta.setFixedSize(632, 275)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaConsulta.setWindowIcon(icon)
        TelaConsulta.setModal(True)
        self.line = QtWidgets.QFrame(TelaConsulta)
        self.line.setGeometry(QtCore.QRect(310, 10, 20, 241))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(TelaConsulta)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 50, 261, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.CamConsultaResultado = QtWidgets.QLineEdit(self.layoutWidget)
        self.CamConsultaResultado.setObjectName("CamConsultaResultado")
        self.gridLayout_2.addWidget(self.CamConsultaResultado, 1, 0, 1, 2)
        self.radioNomeCompleto = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioNomeCompleto.setObjectName("radioNomeCompleto")
        self.gridLayout_2.addWidget(self.radioNomeCompleto, 2, 0, 1, 1)
        self.radioCPF = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioCPF.setObjectName("radioCPF")
        self.gridLayout_2.addWidget(self.radioCPF, 2, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(TelaConsulta)
        self.layoutWidget1.setGeometry(QtCore.QRect(350, 50, 261, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.CamConsultaFicha = QtWidgets.QLineEdit(self.layoutWidget1)
        self.CamConsultaFicha.setObjectName("CamConsultaFicha")
        self.gridLayout.addWidget(self.CamConsultaFicha, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(TelaConsulta)
        self.scrollArea.setGeometry(QtCore.QRect(130, 140, 161, 51))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 159, 49))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnConsultaResultado = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnConsultaResultado.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConsultaResultado.setIcon(icon)
        self.btnConsultaResultado.setObjectName("btnConsultaResultado")
        self.gridLayout_3.addWidget(self.btnConsultaResultado, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(TelaConsulta)
        self.scrollArea_2.setGeometry(QtCore.QRect(450, 130, 161, 51))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 159, 49))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnConsultaResultado_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btnConsultaResultado_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConsultaResultado_2.setIcon(icon)
        self.btnConsultaResultado_2.setObjectName("btnConsultaResultado_2")
        self.gridLayout_4.addWidget(self.btnConsultaResultado_2, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(TelaConsulta)
        QtCore.QMetaObject.connectSlotsByName(TelaConsulta)




    def retranslateUi(self, TelaConsulta):
        _translate = QtCore.QCoreApplication.translate
        TelaConsulta.setWindowTitle(_translate("TelaConsulta", "Consultas"))
        self.label.setText(_translate("TelaConsulta", "Consulta de Resultados"))
        self.radioNomeCompleto.setText(_translate("TelaConsulta", "Nome Completo"))
        self.radioCPF.setText(_translate("TelaConsulta", "CPF"))
        self.label_2.setText(_translate("TelaConsulta", "Consulta de Fichas"))
        self.btnConsultaResultado.setText(_translate("TelaConsulta", "Consultar"))
        self.btnConsultaResultado_2.setText(_translate("TelaConsulta", "Consultar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaConsulta = QtWidgets.QDialog()
    ui = Ui_TelaConsulta()
    ui.setupUi(TelaConsulta)
    TelaConsulta.show()
    sys.exit(app.exec_())
