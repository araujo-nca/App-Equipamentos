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


        self.combobox_Secao.activated.connect(self.dados_tabela)
        self.combobox_ArranjoInstalacao.activated.connect(self.dados_tabela)
        self.combobox_MaterialIsolante.activated.connect(self.dados_tabela)
        self.combobox_TipoCondutor.activated.connect(self.dados_tabela)



    # Retorna os dados da tabela
    # ------------------------------------------------------------------------------------------
    @pyqtSlot()
    def dados_tabela(self):

        # Variáveis

        material_isolante = str(self.combobox_MaterialIsolante.currentText())
        tipo_de_condutor = str(self.combobox_TipoCondutor.currentText())
        arranjo_instalacao = str(self.combobox_ArranjoInstalacao.currentText())
        nivel_de_tensao = str(self.combobox_NivelTensao.currentText())
        secao_condutor = float(self.combobox_Secao.currentText())
        unipolar = bool(self.radioButton_Unipolar.isChecked())
        tripolar = bool(self.radioButton_Tripolar.isChecked())
        
        
        if(unipolar and material_isolante == 'PVC' and tipo_de_condutor == 'Cobre'):

            tabela = Planilha("Tabelas", "4.23.uni")

        elif(tripolar and material_isolante == 'PVC' and tipo_de_condutor == 'Cobre'):

            tabela = Planilha("Tabelas", "4.23.tri")

            self.del_item_in_combo("1.5")
            self.del_item_in_combo("2.5")
            self.del_item_in_combo("4")
            self.del_item_in_combo("6")

        elif(unipolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '0.6/1.0'):

            tabela = Planilha("Tabelas", "4.24.uni.0,6-1")


        elif(tripolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '0.6/1.0'):

            tabela = Planilha("Tabelas", "4.24.tri.0,6-1")

        elif(unipolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '8.7/15'):

            tabela = Planilha("Tabelas", "4.24.uni.8,7-15")

        elif(tripolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '8.7/15'):

            tabela = Planilha("Tabelas", "4.24.tri.8,7-15")

        elif(unipolar and material_isolante == 'EPR' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '0.6/1.0'):

            tabela = Planilha("Tabelas", "4.25.uni.0,6-1")

        elif(unipolar and material_isolante == 'EPR' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '8.7/15'):

            tabela = Planilha("Tabelas", "4.25.uni.8,7-15")

        elif(tripolar and material_isolante == 'EPR' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '0.6/1.0'):

            tabela = Planilha("Tabelas", "4.25.tri.0,6-1")

        elif(tripolar and material_isolante == 'EPR' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '8.7/15'):

            tabela = Planilha("Tabelas", "4.25.tri.8,7-15")

        elif(unipolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Alumínio' and nivel_de_tensao == '8.7/15'):

            tabela = Planilha("Tabelas", "4.26.uni.8,7-15")

        elif(unipolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Alumínio' and nivel_de_tensao == '20/35'):

            tabela = Planilha("Tabelas", "4.26.uni.20-35")

        elif(unipolar and material_isolante == 'EPR' and tipo_de_condutor == 'Alumínio' and nivel_de_tensao == '8.7/15'):

            tabela = Planilha("Tabelas", "4.27.uni.8,7-15")

        elif(unipolar and material_isolante == 'EPR' and tipo_de_condutor == 'Alumínio' and nivel_de_tensao == '20/35'):

            tabela = Planilha("Tabelas", "4.27.uni.20-35")

        else:
            pass
        
        secao = tabela.set_index("Seção condutor")

        corrente_nominal = secao.loc[[secao_condutor],[arranjo_instalacao]].values[0][0]
        rp = secao.loc[[secao_condutor],["Rp"]].values[0][0]
        rz = secao.loc[[secao_condutor],["Rz"]].values[0][0]
        xp = secao.loc[[secao_condutor],["Xp"]].values[0][0]
        xz = secao.loc[[secao_condutor],["Xz"]].values[0][0]

        self.lineEdit_CorrenteNominal.setText(str(corrente_nominal))
        self.lineEdit_RP.setText(str(rp))
        self.lineEdit_RZ.setText(str(rz))
        self.lineEdit_XP.setText(str(xp))
        self.lineEdit_XZ.setText(str(xz))
        


    # ------------------------------------------------------------------------------------------

    def del_item_in_combo(self, text):
        # currentTextChanged signal will pass selected text to slot
        index = self.combobox_Secao.findText(text)  # find the index of text
        self.combobox_Secao.removeItem(index)

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