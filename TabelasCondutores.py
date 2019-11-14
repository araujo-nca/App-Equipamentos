#############################################################################################
#                          EQUIPAMENTOS ELÉTRICOS                                           #
#                                                                                           #
#   CENTRO FEDERAL DE EDUCAÇÃO TECNOLÓGICA - ENGENHARIA ELÉTRICA                            #
#   Alunos: Michael Henrique, Deilson Martins, Nathan Araújo, Matheus Almeida               #
#   Professor: Marcelo Nesci                                                                #
#                                                                                           #    
#############################################################################################



import numpy as np
from planilhas import Planilha
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from condutores import Condutor
from dmg import Dmg
import sys
import resources


# Cria uma Classe para Tabela Condutores
class TabelaCondutores(QtWidgets.QMainWindow):
    def __init__(self):
        super(TabelaCondutores, self).__init__()
        uic.loadUi('Consulta-tabelas-condutores.ui', self)

        self.show()


        # Radio Buttons
        # ----------------------------------------------------------------------------------------------

        # Define o Radio Button para a configuração unipolar
        self.radioButton_3unipolar = self.findChild(QtWidgets.QRadioButton, 'radioButton_3unipolares')

        # Define o Radio Button para a configuração tripolar
        self.radioButton_1tripolar = self.findChild(QtWidgets.QRadioButton, 'radioButton_1tripolar')
        
        self.radioButton_3uni_triangulo_eq = self.findChild(QtWidgets.QRadioButton, 'radioButton_3uni_triangulo_eq')

        self.radioButton_3uni_plano = self.findChild(QtWidgets.QRadioButton, 'radioButton_3uni_plano')

        self.radioButton_3uni_assimetricos = self.findChild(QtWidgets.QRadioButton, 'radioButton_3uni_assimetricos')        

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

        # Define o Line Edit para a entrada distancia
        self.lineEdit_distanciaDMG = self.findChild(QtWidgets.QLineEdit, "lineEdit_distanciaDMG")
        
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
        
        
        # Ações
        # ------------------------------------------------------------------------------------------
        
        # Define a configuração ao clicar no radio button unipolar
        self.radioButton_3unipolar.clicked.connect(self.configuracao_tripolar)

        # Define a configuração ao clicar no radio button tripolar
        self.radioButton_1tripolar.clicked.connect(self.configuracao_tripolar)

        self.radioButton_3uni_triangulo_eq.clicked.connect(self.configuracao_triangulo_equilatero)
        
        self.radioButton_3uni_plano.clicked.connect(self.configuracao_plano)
        
        self.radioButton_3uni_assimetricos.clicked.connect(self.configuracao_espacados_assimetricamente)

        # Define a configuração ao defenir o tipo de condutor
        self.combobox_TipoCondutor.activated.connect(self.configuracao_tipo_de_condutor)

        # Define a configuração ao defenir o material de isolamento
        self.combobox_MaterialIsolante.activated.connect(self.configuracao_material_de_isolamento)


        # Atualiza os dados
        self.combobox_Secao.activated.connect(self.dados_tabela)
        self.combobox_ArranjoInstalacao.activated.connect(self.dados_tabela)
        self.combobox_MaterialIsolante.activated.connect(self.dados_tabela)
        self.combobox_TipoCondutor.activated.connect(self.dados_tabela)
        self.combobox_NivelTensao.activated.connect(self.dados_tabela)
        self.radioButton_3unipolar.clicked.connect(self.dados_tabela)
        self.radioButton_1tripolar.clicked.connect(self.dados_tabela)


    # Função para retornas os dados da tabela
    # ------------------------------------------------------------------------------------------
    @pyqtSlot()
    def dados_tabela(self):

        # Variáveis do condutor
        material_isolante = str(self.combobox_MaterialIsolante.currentText())
        tipo_de_condutor = str(self.combobox_TipoCondutor.currentText())
        arranjo_instalacao = str(self.combobox_ArranjoInstalacao.currentText())
        nivel_de_tensao = str(self.combobox_NivelTensao.currentText())
        secao_condutor = float(self.combobox_Secao.currentText())
        unipolar = bool(self.radioButton_3unipolar.isChecked())
        tripolar = bool(self.radioButton_1tripolar.isChecked())


        # Função para mostrar os dados da tela
        def dados(tabela_dos_dados):
            
            # Define a seção como o "Fator de busca"
            secao = tabela_dos_dados.set_index("Seção condutor")

            # Procura as seções na tabela, conforme o valor da seção
            corrente_nominal = secao.loc[[secao_condutor],[arranjo_instalacao]].values[0][0]
            rp = secao.loc[[secao_condutor],["Rp"]].values[0][0]
            rz = secao.loc[[secao_condutor],["Rz"]].values[0][0]
            xp = secao.loc[[secao_condutor],["Xp"]].values[0][0]
            xz = secao.loc[[secao_condutor],["Xz"]].values[0][0]
            xc = secao.loc[[secao_condutor],["Xc"]].values[0][0]

            # Adiciona na tela os valores encontrados na tabela para a configuração
            self.lineEdit_CorrenteNominal.setText(str(corrente_nominal))
            self.lineEdit_RP.setText(str(rp))
            self.lineEdit_RZ.setText(str(rz))
            self.lineEdit_XP.setText(str(xp))
            self.lineEdit_XZ.setText(str(xz))
            self.lineEdit_XC.setText(str(xc))
        
        # Pega os dados da tabela 4.23 para a configuração unipolar
        if(unipolar and material_isolante == 'PVC' and tipo_de_condutor == 'Cobre'):
            
            # Lê a tabela
            tabela = Planilha("Tabelas", "4.23.uni")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.23 para a configuração tripolar
        elif(tripolar and material_isolante == 'PVC' and tipo_de_condutor == 'Cobre'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.23.tri")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.24 para a configuração unipolar e nível de tensão de 0.6-1 kV
        elif(unipolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '0.6/1.0'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.24.uni.0,6-1")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.24 para a configuração tripolar e nível de tensão de 0.6-1 kV
        elif(tripolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '0.6/1.0'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.24.tri.0,6-1")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.24 para a configuração unipolar e nível de tensão de 8.7-15 kV
        elif(unipolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '8.7/15'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.24.uni.8,7-15")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.24 para a configuração tripolar e nível de tensão de 8.7-15 kV
        elif(tripolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '8.7/15'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.24.tri.8,7-15")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.25 para a configuração unipolar e nível de tensão de 0.6-1 kV
        elif(unipolar and material_isolante == 'EPR' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '0.6/1.0'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.25.uni.0,6-1")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.25 para a configuração unipolar e nível de tensão de 8.7-15 kV
        elif(unipolar and material_isolante == 'EPR' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '8.7/15'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.25.uni.8,7-15")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.25 para a configuração tripolar e nível de tensão de 0.6-1 kV
        elif(tripolar and material_isolante == 'EPR' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '0.6/1.0'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.25.tri.0,6-1")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.25 para a configuração tripolar e nível de tensão de 8.76-15 kV
        elif(tripolar and material_isolante == 'EPR' and tipo_de_condutor == 'Cobre' and nivel_de_tensao == '8.7/15'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.25.tri.8,7-15")
            dados(tabela)
            # Mostra os dados lidos na tela

        # Pega os dados da tabela 4.26 para a configuração unipolar e nível de tensão de 8.76-15 kV
        elif(unipolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Alumínio' and nivel_de_tensao == '8.7/15'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.26.uni.8,7-15")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.26 para a configuração unipolar e nível de tensão de 20-35 kV
        elif(unipolar and material_isolante == 'XLPE' and tipo_de_condutor == 'Alumínio' and nivel_de_tensao == '20/35'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.26.uni.20-35")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.27 para a configuração unipolar e nível de tensão de 8.76-15 kV
        elif(unipolar and material_isolante == 'EPR' and tipo_de_condutor == 'Alumínio' and nivel_de_tensao == '8.7/15'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.27.uni.8,7-15")
            # Mostra os dados lidos na tela
            dados(tabela)

        # Pega os dados da tabela 4.27 para a configuração unipolar e nível de tensão de 20-35 kV
        elif(unipolar and material_isolante == 'EPR' and tipo_de_condutor == 'Alumínio' and nivel_de_tensao == '20/35'):

            # Lê a tabela
            tabela = Planilha("Tabelas", "4.27.uni.20-35")
            # Mostra os dados lidos na tela
            dados(tabela)

        else:
            

            self.lineEdit_CorrenteNominal.setText('-')
            self.lineEdit_RP.setText('-')
            self.lineEdit_RZ.setText('-')
            self.lineEdit_XP.setText('-')
            self.lineEdit_XZ.setText('-')
            self.lineEdit_XC.setText('-')

            self.erro = Erro()
            self.erro.show()
        


        

    # ------------------------------------------------------------------------------------------


    # Função para a configuração unipolar
    @pyqtSlot()
    def configuracao_unipolar(self):

        # Mostra na tela uma imagem de um cabo unipolar
        imagem = QPixmap('Imagens/Cabo Unipolar.png')
        self.label_ImagemCondutor.setPixmap(imagem)

        # Listas com os itens para adicionar aos combo boxes
        items_secao = ['1.5','2.5','4','6','10','16','25', '35', '50', '70', '95', '120', '150', '185', '240','300','400','500']
        items_nivel_tesao = ['0.6/1.0','8.7/15']
        items_tipo_condutor = ['Cobre', 'Alumínio']

        # Adiciona os itens das listas para seus respectivos combo boxes
        self.combo_box_items(items_secao, self.combobox_Secao)
        self.combo_box_items(items_nivel_tesao, self.combobox_NivelTensao)
        self.combo_box_items(items_tipo_condutor, self.comboBox_TipoCondutor)


    # Função para a configuração tripolar
    @pyqtSlot()
    def configuracao_tripolar(self):

        # Mostra na tela uma imagem de um cabo tripolar
        imagem = QPixmap('Imagens/Cabo Tripolar.png')
        self.label_ImagemCondutor.setPixmap(imagem)

        # Listas com os itens para adicionar aos combo boxes
        items_secao = ['25', '35', '50', '70', '95', '120', '150', '185', '240']
        items_nivel_tesao = ['0.6/1.0','8.7/15' ,'20/35']
        items_tipo_condutor = ['Cobre']

        # Adiciona os itens das listas para seus respectivos combo boxes
        self.combo_box_items(items_secao, self.combobox_Secao)
        self.combo_box_items(items_nivel_tesao, self.combobox_NivelTensao)
        self.combo_box_items(items_tipo_condutor, self.comboBox_TipoCondutor)

    # Função para a configuração triangular equilatero INCLUI APENAS A IMAGEM CORRESPONDENTE
    @pyqtSlot()
    def configuracao_triangulo_equilatero(self):

        # Mostra na tela uma imagem de um cabo tripolar
        imagem = QPixmap('Imagens/Unipolar_Equilatero.png')
        self.label_ImagemCondutor.setPixmap(imagem)

        # Listas com os itens para adicionar aos combo boxes
        items_secao = ['25', '35', '50', '70', '95', '120', '150', '185', '240']
        items_nivel_tesao = ['0.6/1.0','8.7/15' ,'20/35']
        items_tipo_condutor = ['Cobre']

        # Adiciona os itens das listas para seus respectivos combo boxes
        self.combo_box_items(items_secao, self.combobox_Secao)
        self.combo_box_items(items_nivel_tesao, self.combobox_NivelTensao)
        self.combo_box_items(items_tipo_condutor, self.comboBox_TipoCondutor)

    # Função para a configuração plana INCLUI APENAS A IMAGEM CORRESPONDENTE
    @pyqtSlot()
    def configuracao_plano(self):

        # Mostra na tela uma imagem de um cabo tripolar
        imagem = QPixmap('Imagens/Unipolar_Plana.png')
        self.label_ImagemCondutor.setPixmap(imagem)

        # Listas com os itens para adicionar aos combo boxes
        items_secao = ['25', '35', '50', '70', '95', '120', '150', '185', '240']
        items_nivel_tesao = ['0.6/1.0','8.7/15' ,'20/35']
        items_tipo_condutor = ['Cobre']

        # Adiciona os itens das listas para seus respectivos combo boxes
        self.combo_box_items(items_secao, self.combobox_Secao)
        self.combo_box_items(items_nivel_tesao, self.combobox_NivelTensao)
        self.combo_box_items(items_tipo_condutor, self.comboBox_TipoCondutor)

    # Função para a configuração espaçada assimetricamente INCLUI APENAS A IMAGEM CORRESPONDENTE
    @pyqtSlot()
    def configuracao_espacados_assimetricamente(self):

        # Mostra na tela uma imagem de um cabo tripolar
        imagem = QPixmap('Imagens/Unipolar_Espaçados.png')
        self.label_ImagemCondutor.setPixmap(imagem)

        # Listas com os itens para adicionar aos combo boxes
        items_secao = ['25', '35', '50', '70', '95', '120', '150', '185', '240']
        items_nivel_tesao = ['0.6/1.0','8.7/15' ,'20/35']
        items_tipo_condutor = ['Cobre']

        # Adiciona os itens das listas para seus respectivos combo boxes
        self.combo_box_items(items_secao, self.combobox_Secao)
        self.combo_box_items(items_nivel_tesao, self.combobox_NivelTensao)
        self.combo_box_items(items_tipo_condutor, self.comboBox_TipoCondutor)

    # Função para a configuração tipo de condutor
    @pyqtSlot()
    def configuracao_tipo_de_condutor(self):
        
        # Caso condutor seja de aluminío
        if(str(self.combobox_TipoCondutor.currentText()) == 'Alumínio'):

            # Listas com os itens para adicionar aos combo boxes
            items_secao = ['25', '35', '50', '70', '95', '120', '150', '185', '240','300','400','500']
            items_material_isolante = ['XLPE', 'EPR']
            items_nivel_tesao = ['8.7/15' ,'20/35']

            # Adiciona os itens das listas para seus respectivos combo boxes
            self.combo_box_items(items_secao, self.combobox_Secao)
            self.combo_box_items(items_material_isolante, self.combobox_MaterialIsolante)
            self.combo_box_items(items_nivel_tesao, self.combobox_NivelTensao)

        # Caso condutor seja de cobre
        if(str(self.combobox_TipoCondutor.currentText()) == 'Cobre'):

            # Listas com os itens para adicionar aos combo boxes
            items_secao = ['1.5','2.5','4','6','10','16','25', '35', '50', '70', '95', '120', '150', '185', '240','300','400','500']
            items_material_isolante = ['XLPE', 'PVC','EPR']
            items_nivel_tesao = ['0.6/1.0','8.7/15']

            # Adiciona os itens das listas para seus respectivos combo boxes
            self.combo_box_items(items_secao, self.combobox_Secao)
            self.combo_box_items(items_material_isolante, self.combobox_MaterialIsolante)
            self.combo_box_items(items_nivel_tesao, self.combobox_NivelTensao)

    # Função para a configuração material de isolamento
    @pyqtSlot()
    def configuracao_material_de_isolamento(self):

        if(bool(self.radioButton_1tripolar.isChecked())):

            if(str(self.combobox_MaterialIsolante.currentText()) == 'EPR'):
                # Listas com os itens para adicionar aos combo boxes
                items_nivel_tesao = ['0.6/1.0','8.7/15']

                # Adiciona os itens das listas para seus respectivos combo boxes
                self.combo_box_items(items_nivel_tesao, self.combobox_NivelTensao)
            else:
                
                self.configuracao_tripolar()
            
        else:

            self.configuracao_unipolar()

    # funcao deilson configuracao em triangulo equilatero
    @pyqtSlot()
    def configuracao_tripolar_em_triangulo_equilatero(self):
        
        # Variáveis do condutor
        material_isolante = str(self.combobox_MaterialIsolante.currentText())
        tipo_de_condutor = str(self.combobox_TipoCondutor.currentText())
        # arranjo_instalacao = str(self.combobox_ArranjoInstalacao.currentText())
        nivel_de_tensao = str(self.combobox_NivelTensao.currentText())
        secao_condutor = float(self.combobox_Secao.currentText())
        # tri_equilatero = bool(self.radioButton_3uni_triangulo_eq.isChecked())
        distanciaDMG = float(self.lineEdit_distanciaDMG.text())

        condutor = Condutor(material_isolante, tipo_de_condutor, secao_condutor, nivel_de_tensao)
        dmg = Dmg()
        resistividade = condutor.resistividade_condutor()
        temperatura_condutor = 90
        distancia_entre_cabos = dmg.tres_cabos_unipolares_em_triangulo_equilatero(distanciaDMG)
        # distancia_entre_cabos = 1
        temperatura_blindagem = 85

        K4 = 1.1
        Ebi = 0.3
        Ebe = 0.3
        Ebm = 0.08

        if material_isolante == "XLPE":
            
            resistividade = condutor.resistividade_condutor()
            temperatura_condutor = 90

            zp = condutor.impedancia_positiva_aterrada_um_ponto(temperatura_condutor, "Três_cabos_unipolares_em_triangulo_equilatero", distancia_entre_cabos)
            rp = np.real(zp)
            xp = np.imag(zp)

            zz = condutor.impedancia_zero_blindagem_aterrada_um_ponto(resistividade, temperatura_condutor, temperatura_blindagem, K4, Ebi, Ebe, Ebm, "Três_cabos_unipolares_em_triangulo_equilatero", distancia_entre_cabos)
            rz = np.real(zz)
            xz = np.imag(zz)

        elif material_isolante == "EPR":
            
            resistividade = condutor.resistividade_condutor()
            temperatura_condutor = 90

            zp = condutor.impedancia_positiva_aterrada_um_ponto(temperatura_condutor, "Três_cabos_unipolares_em_triangulo_equilatero", distancia_entre_cabos)
            rp = np.real(zp)
            xp = np.imag(zp)
            
            zz = condutor.impedancia_zero_blindagem_aterrada_um_ponto(resistividade, temperatura_condutor, temperatura_blindagem, K4, Ebi, Ebe, Ebm, "Três_cabos_unipolares_em_triangulo_equilatero", distancia_entre_cabos)
            rz = np.real(zz)
            xz = np.imag(zz)

        elif material_isolante == "PVC":
            
            resistividade = condutor.resistividade_condutor()
            temperatura_condutor = 70
            
            zp = condutor.impedancia_positiva_aterrada_um_ponto(temperatura_condutor, "Três_cabos_unipolares_em_triangulo_equilatero", distancia_entre_cabos)
            rp = np.real(zp)
            xp = np.imag(zp)
        
            zz = condutor.impedancia_zero_blindagem_aterrada_um_ponto(resistividade, temperatura_condutor, temperatura_blindagem, K4, Ebi, Ebe, Ebm, "Três_cabos_unipolares_em_triangulo_equilatero", distancia_entre_cabos)
            rz = np.real(zz)
            xz = np.imag(zz)
        
            self.lineEdit_RP.setText(str(rp))
            self.lineEdit_RZ.setText(str(rz))
            self.lineEdit_XP.setText(str(xp))
            self.lineEdit_XZ.setText(str(xz))


    # funcao deilson configuracao espacados assimetricamente
    @pyqtSlot()
    def tres_cabos_unipolares_espacados_assimetricamente(self):

        # Variáveis do condutor
        material_isolante = str(self.combobox_MaterialIsolante.currentText())
        tipo_de_condutor = str(self.combobox_TipoCondutor.currentText())
        arranjo_instalacao = str(self.combobox_ArranjoInstalacao.currentText())
        nivel_de_tensao = str(self.combobox_NivelTensao.currentText())
        secao_condutor = float(self.combobox_Secao.currentText())
        esp_assimetricamente = bool(self.radioButton_3uni_assimetricos.isChecked())

        
        if material_isolante == "XLPE":
            
            condutor = Condutor(material_isolante, tipo_de_condutor, secao_condutor, nivel_de_tensao)
            dmg = Dmg()
            resistividade = condutor.resistividade_condutor()
            temperatura_condutor = 90
            distancia_entre_cabos = dmg.tres_cabos_unipolares_espacados_assimetricamente(esp_assimetricamente)

            temperatura_blindagem = 85
            K4 = 1.1
            Ebi = 0.3
            Ebe = 0.3
            Ebm = 0.08

            zp = condutor.impedancia_positiva_aterrada_um_ponto(temperatura_condutor, "tres_cabos_unipolares_espacados_assimetricamente", distancia_entre_cabos)
            rp = np.real(zp)
            xp = np.imag(zp)

            zz = condutor.impedancia_zero_blindagem_aterrada_um_ponto(resistividade, temperatura_condutor, temperatura_blindagem, K4, Ebi, Ebe, Ebm, "Três_cabos_unipolares_em_triangulo_equilatero", distancia_entre_cabos)
            rz = np.real(zz)
            xz = np.imag(zz)

        elif material_isolante == "EPR":
                
            resistividade = condutor.resistividade_condutor()
            temperatura_condutor = 90

            zp = condutor.impedancia_positiva_aterrada_um_ponto(temperatura_condutor, "tres_cabos_unipolares_espacados_assimetricamente", distancia_entre_cabos)
            rp = np.real(zp)
            xp = np.imag(zp)
                
            zz = condutor.impedancia_zero_blindagem_aterrada_um_ponto(resistividade, temperatura_condutor, temperatura_blindagem, K4, Ebi, Ebe, Ebm, "Três_cabos_unipolares_em_triangulo_equilatero", distancia_entre_cabos)
            rz = np.real(zz)
            xz = np.imag(zz)

        elif material_isolante == "PVC":
                
            resistividade = condutor.resistividade_condutor()
            temperatura_condutor = 70
                
            zp = condutor.impedancia_positiva_aterrada_um_ponto(temperatura_condutor, "tres_cabos_unipolares_espacados_assimetricamente", distancia_entre_cabos)
            rp = np.real(zp)
            xp = np.imag(zp)
            
            zz = condutor.impedancia_zero_blindagem_aterrada_um_ponto(resistividade, temperatura_condutor, temperatura_blindagem, K4, Ebi, Ebe, Ebm, "tres_cabos_unipolares_espacados_assimetricamente", distancia_entre_cabos)
            rz = np.real(zz)
            xz = np.imag(zz)
        
        self.lineEdit_RP.setText(str(rp))
        self.lineEdit_RZ.setText(str(rz))
        self.lineEdit_XP.setText(str(xp))
        self.lineEdit_XZ.setText(str(xz)) 



    # Função para remover todos os itens do combo box e adicionar itens de uma lista
    def combo_box_items(self, lista_de_items, combobox):
        
        # Limpa o Combo Box
        combobox.clear()
        
        # Adiciona os itens da lista
        for item in lista_de_items:
            combobox.addItem(item)

# Caixa de diálogo para indicar que a configuração não está disponível
class Erro(QtWidgets.QDialog):
    def __init__(self):
        super(Erro, self).__init__()
        uic.loadUi('Erro.ui', self)

        self.show()

# Função Main, onde o construtor da aplicação é definido e é executado
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TabelaCondutores()
    app.exec_()


# Executa a aplicação
if __name__ == "__main__":
    main()