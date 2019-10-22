from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
import sys

# Cria uma Classe para o App principal
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('mainwindow MVP.ui', self)


        # Botão para os condutores
        self.btm_condutores = self.findChild(QtWidgets.QPushButton, 'pushButton_Condutores')

        # Botão para o Transformador de Potencial
        self.btm_tp = self.findChild(QtWidgets.QPushButton, 'pushButton_Tp')

        # Botão para o Transformador de Corrente
        self.btm_tc = self.findChild(QtWidgets.QPushButton, 'pushButton_Tc')

        # Mostra a Janle Principal
        self.show()

        # Cria um Objeto Condutores
        self.condutores = Condutores()
        # Define uma ação par ao botão
        self.btm_condutores.clicked.connect(self.open_Condutores)

        # Cria um objeto Transformador de Potencial
        self.tp = Transformador_de_Potencial()
        # Define uma ação para o botão Transformador de Potencial
        self.btm_tp.clicked.connect(self.open_TP)

        # Cria um objeto para o botão Transformador de Corrente
        self.tc = Transformador_de_Corrente()
        # Define uma ação para o botão transformador de Corrente
        self.btm_tc.clicked.connect(self.open_TC)


    # Abre Condutores
    @pyqtSlot()
    def open_Condutores(self):
        if self.condutores.isHidden():
            self.condutores.show()
        else:
            self.condutores.hide()

   # Abre TP 
    @pyqtSlot()
    def open_TP(self):
        if self.tp.isHidden():
            self.tp.show()
        else:
            self.tp.hide()

    # Abre Tc
    @pyqtSlot()
    def open_TC(self):
        if self.tc.isHidden():
            self.tc.show()
        else:
            self.tc.hide()


    
# Cria uma Classe para condutores
class Condutores(QtWidgets.QMainWindow):
    def __init__(self):
        super(Condutores, self).__init__()
        uic.loadUi('Condutores MVP.ui', self)


# Cria uma Classe para Transformador de Potencial
class Transformador_de_Potencial(QtWidgets.QMainWindow):
    def __init__(self):
        super(Transformador_de_Potencial, self).__init__()
        uic.loadUi('Transformador de Potencial MVP.ui', self)

# Cria uma Classe para Transformador de Corrente
class Transformador_de_Corrente(QtWidgets.QMainWindow):
    def __init__(self):
        super(Transformador_de_Corrente, self).__init__()
        uic.loadUi('Transformador de Corrente MVP.ui', self)

        # Botão para a corrente no secundário
        self.btm_CorrenteSecundario = self.findChild(QtWidgets.QPushButton, 'pushButtonCorrenteSecundario')
        # Botão para a carga nominal
        self.btm_CargaNominal = self.findChild(QtWidgets.QPushButton, 'pushButtonCargaNominal')
        # Botão para a carga do tc
        self.btm_CargaTC = self.findChild(QtWidgets.QPushButton, 'pushButtonCargaTC')
        # Botão para o fator de sobrecorrente
        self.btm_FatorSobrecorrente = self.findChild(QtWidgets.QPushButton, 'pushButtonFatorSobrecorrente')
        # Botão para a corrente de magnetização
        self.btm_CorrenteMagnetizacao = self.findChild(QtWidgets.QPushButton, 'pushButtonCorrenteMagnetizacao')
        # Botão para a tensão nominal
        self.btm_TensaoSecundario = self.findChild(QtWidgets.QPushButton, 'pushButtonTensaoSecundario')


# Cria uma Classe para Tabela Condutores
class TabelaCondutores(QtWidgets.QMainWindow):
    def __init__(self):
        super(TabelaCondutores, self).__init__()
        uic.loadUi('Condutores TESTE.ui', self)

        self.show()

        self.btm_configuracao_Unipolar = self.findChild(QtWidgets.QRadioButton, 'radioButton_Unipolar')
        self.btm_configuracao_Tripolar = self.findChild(QtWidgets.QRadioButton, 'radioButton_Tripolar')
        self.imagem_condutor = self.findChild(QtWidgets.QLabel, 'label_Imagem')


        self.btm_configuracao_Unipolar.clicked.connect(self.imagem_unipolar)
        self.btm_configuracao_Tripolar.clicked.connect(self.imagem_tripolar)



    @pyqtSlot()
    def imagem_unipolar(self):
        imagem = QPixmap('Imagens/Cabo Unipolar.png')
        self.imagem_condutor.setPixmap(imagem)

    @pyqtSlot()
    def imagem_tripolar(self):
        imagem = QPixmap('Imagens/Cabo Tripolar.png')
        self.imagem_condutor.setPixmap(imagem)

    


# Função Main
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    app.exec_()

# Roda a Main
if __name__ == "__main__":
    main()

