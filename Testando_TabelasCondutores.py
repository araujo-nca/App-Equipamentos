import numpy as np
from planilhas import Planilha
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
import sys
import resources


# Cria uma Classe para Tabela Condutores
class TabelaCondutores(QtWidgets.QMainWindow):
    def __init__(self):
        super(TabelaCondutores, self).__init__()
        uic.loadUi('Condutores TESTE23.ui', self)

        self.show()


        # Radio Buttons
        # ----------------------------------------------------------------------------------------------

        # Define o Radio Button para a configuração unipolar
        self.radioButton_Unipolar = self.findChild(QtWidgets.QRadioButton, 'radioButton_Unipolar')

        # Define o Radio Button para a configuração tripolar
        self.radioButton_Tripolar = self.findChild(QtWidgets.QRadioButton, 'radioButton_Tripolar')

        # Labels
        # ----------------------------------------------------------------------------------------------

        # Define a label para alterar a imagem da configuração 
        self.label_ImagemCondutor = self.findChild(QtWidgets.QLabel, 'label_ImagemCondutor')

        # Combo Boxs
        # ----------------------------------------------------------------------------------------------

        # Define a Combo Box para o Material isolante
        self.combobox_MaterialIsolante = self.findChild(QtWidgets.QComboBox, 'comboBox_MaterialIsolante')

        # Define a Combo Box para o Tipo de condutor
        self.combobox_TipoCondutor = self.findChild(QtWidgets.QComboBox, 'comboBox_TipoCondutor')

        # Define a Combo Box para o Arranjo da instalação
        self.combobox_ArranjoInstalacao = self.findChild(QtWidgets.QComboBox, 'comboBox_ArranjoInstalacao')

        # Define a Combo Box para o Nível de tensão
        self.combobox_NivelTensao = self.findChild(QtWidgets.QComboBox, 'comboBox_NivelTensao')

        # Define a Combo Box para a seção do condutor
        self.combobox_Secao = self.findChild(QtWidgets.QComboBox, 'comboBox_Secao')


        # Line Edit
        # ----------------------------------------------------------------------------------------------

        # Define o Line Edit para a variável Rp
        self.lineEdit_RP = self.findChild(QtWidgets.QLineEdit, "lineEdit_RP")
        
        # Define o Line Edit para a variável Rz
        self.lineEdit_RZ = self.findChild(QtWidgets.QLineEdit, "lineEdit_RZ")
        
        # Define o Line Edit para a variável Xp
        self.lineEdit_XP = self.findChild(QtWidgets.QLineEdit, "lineEdit_XP")
        
        # Define o Line Edit para a variável Xz
        self.lineEdit_XZ = self.findChild(QtWidgets.QLineEdit, "lineEdit_XZ")
        
        # Define o Line Edit para a variável Xc
        self.lineEdit_XC = self.findChild(QtWidgets.QLineEdit, "lineEdit_XC")

        # Define o Line Edit para a variável Corrente nominal
        self.lineEdit_CorrenteNominal = self.findChild(QtWidgets.QLineEdit, "lineEdit_CorrenteNominal")
        
        
        # Define a ação ao clicar no radio button unipolar
        self.radioButton_Unipolar.clicked.connect(self.imagem_unipolar)

        # Define a ação ao clicar no radio button tripolar
        self.radioButton_Tripolar.clicked.connect(self.imagem_tripolar)


        self.combobox_Secao.activated.connect(self.teste)
        self.combobox_ArranjoInstalacao.activated.connect(self.teste)



    # Teste
    # ------------------------------------------------------------------------------------------
    @pyqtSlot()
    def teste(self):
        if(self.radioButton_Unipolar.pressed):

            tabela = Planilha("Tabelas", "4.23.uni")
            secao = tabela.set_index("Seção condutor")

            corrente_nominal = secao.loc[[float(self.combobox_Secao.currentText())],[str(self.combobox_ArranjoInstalacao.currentText())]]
            rp = secao.loc[[float(self.combobox_Secao.currentText())],["Rp"]]
            rz = secao.loc[[float(self.combobox_Secao.currentText())],["Rz"]]
            xp = secao.loc[[float(self.combobox_Secao.currentText())],["Xp"]]
            xz = secao.loc[[float(self.combobox_Secao.currentText())],["Xz"]]

            self.lineEdit_CorrenteNominal.setText(str(corrente_nominal))
            self.lineEdit_RP.setText(str(rp))
            self.lineEdit_RZ.setText(str(rz))
            self.lineEdit_XP.setText(str(xp))
            self.lineEdit_XZ.setText(str(xz))



    # ------------------------------------------------------------------------------------------



    @pyqtSlot()
    def imagem_unipolar(self):
        imagem = QPixmap('Imagens/Cabo Unipolar.png')
        self.label_ImagemCondutor.setPixmap(imagem)

    @pyqtSlot()
    def imagem_tripolar(self):
        imagem = QPixmap('Imagens/Cabo Tripolar.png')
        self.label_ImagemCondutor.setPixmap(imagem)

    @pyqtSlot()
    def CorrenteNominal(self):
        pass

    @pyqtSlot()
    def CorrenteNominal(self):
        pass
    
    @pyqtSlot()
    def CorrenteNominal(self):
        pass

# Função Main
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TabelaCondutores()
    app.exec_()

# Roda a Main
if __name__ == "__main__":
    main()