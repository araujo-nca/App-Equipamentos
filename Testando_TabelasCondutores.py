from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
import sys



# Cria uma Classe para Tabela Condutores
class TabelaCondutores(QtWidgets.QMainWindow):
    def __init__(self):
        super(TabelaCondutores, self).__init__()
        uic.loadUi('Condutores TESTE23.ui', self)

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
    window = TabelaCondutores()
    app.exec_()

# Roda a Main
if __name__ == "__main__":
    main()