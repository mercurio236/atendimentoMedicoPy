# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telademedicamento.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_TelaDeMedicamento(object):
    def setupUi(self, TelaDeMedicamento):
        TelaDeMedicamento.setObjectName("TelaDeMedicamento")
        TelaDeMedicamento.setFixedSize(796, 332)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/medicamento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaDeMedicamento.setWindowIcon(icon)
        TelaDeMedicamento.setStyleSheet("QDialog{\n"
"    background-color: #d3d3d3;\n"
"}")
        self.label = QtWidgets.QLabel(TelaDeMedicamento)
        self.label.setGeometry(QtCore.QRect(20, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        TelaDeMedicamento.setModal(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(TelaDeMedicamento)
        self.label_2.setGeometry(QtCore.QRect(20, 25, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(TelaDeMedicamento)
        self.line.setGeometry(QtCore.QRect(0, 70, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(TelaDeMedicamento)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.radioSim = QtWidgets.QRadioButton(self.groupBox)
        self.radioSim.setGeometry(QtCore.QRect(10, 30, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioSim.setFont(font)
        self.radioSim.setObjectName("radioSim")
        self.radioNao = QtWidgets.QRadioButton(self.groupBox)
        self.radioNao.setGeometry(QtCore.QRect(80, 30, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioNao.setFont(font)
        self.radioNao.setObjectName("radioNao")
        self.label_3 = QtWidgets.QLabel(TelaDeMedicamento)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtMedica = QtWidgets.QTextEdit(TelaDeMedicamento)
        self.txtMedica.setGeometry(QtCore.QRect(20, 180, 751, 81))
        self.txtMedica.setObjectName("txtMedica")
        self.btnSalvar = QtWidgets.QPushButton(TelaDeMedicamento)
        self.btnSalvar.setGeometry(QtCore.QRect(690, 270, 81, 31))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../imagens/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnEditar = QtWidgets.QPushButton(TelaDeMedicamento)
        self.btnEditar.setGeometry(QtCore.QRect(590, 270, 81, 31))
        self.btnEditar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../imagens/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditar.setIcon(icon2)
        self.btnEditar.setObjectName("btnEditar")
        self.checkMedico = QtWidgets.QCheckBox(TelaDeMedicamento)
        self.checkMedico.setGeometry(QtCore.QRect(20, 270, 151, 21))
        self.checkMedico.setObjectName("checkMedico")
        self.nomePaciente = QtWidgets.QLabel(TelaDeMedicamento)
        self.nomePaciente.setGeometry(QtCore.QRect(150, 15, 381, 21))
        self.nomePaciente.setText("")
        self.nomePaciente.setObjectName("nomePaciente")
        self.dtaAtendiemento = QtWidgets.QLabel(TelaDeMedicamento)
        self.dtaAtendiemento.setGeometry(QtCore.QRect(70, 35, 151, 21))
        self.dtaAtendiemento.setText("")
        self.dtaAtendiemento.setObjectName("dtaAtendiemento")
        self.label_6 = QtWidgets.QLabel(TelaDeMedicamento)
        self.label_6.setGeometry(QtCore.QRect(20, 45, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.nDaFicha = QtWidgets.QLabel(TelaDeMedicamento)
        self.nDaFicha.setGeometry(QtCore.QRect(100, 50, 161, 21))
        self.nDaFicha.setText("")
        self.nDaFicha.setObjectName("nDaFicha")

        self.retranslateUi(TelaDeMedicamento)
        QtCore.QMetaObject.connectSlotsByName(TelaDeMedicamento)

        #Botoes
        #self.btnEditar.clicked.connect(self.Editar)


    def retranslateUi(self, TelaDeMedicamento):
        _translate = QtCore.QCoreApplication.translate
        TelaDeMedicamento.setWindowTitle(_translate("TelaDeMedicamento", "Medicamento "))
        self.label.setText(_translate("TelaDeMedicamento", "Nome do Paciente:"))
        self.label_2.setText(_translate("TelaDeMedicamento", "Data:"))
        self.groupBox.setTitle(_translate("TelaDeMedicamento", "Paciente está com dor?"))
        self.radioSim.setText(_translate("TelaDeMedicamento", "Sim"))
        self.radioNao.setText(_translate("TelaDeMedicamento", "Não"))
        self.label_3.setText(_translate("TelaDeMedicamento", "Tipo de medicação ministrada"))
        self.btnSalvar.setText(_translate("TelaDeMedicamento", "Salvar"))
        self.btnEditar.setText(_translate("TelaDeMedicamento", "Editar"))
        self.checkMedico.setText(_translate("TelaDeMedicamento", "Retorno ao médico"))
        self.label_6.setText(_translate("TelaDeMedicamento", "N° da Ficha:"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaDeMedicamento = QtWidgets.QDialog()
    ui = Ui_TelaDeMedicamento()
    ui.setupUi(TelaDeMedicamento)
    TelaDeMedicamento.show()
    sys.exit(app.exec_())
