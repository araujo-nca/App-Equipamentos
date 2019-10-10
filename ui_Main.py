from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
import sys

# Cria uma Classe para o App principal
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('mainwindow.ui', self)


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
        uic.loadUi('Condutores.ui', self)


# Cria uma Classe para Transformador de Potencial
class Transformador_de_Potencial(QtWidgets.QMainWindow):
    def __init__(self):
        super(Transformador_de_Potencial, self).__init__()
        uic.loadUi('Transformador de Potencial.ui', self)

# Cria uma Classe para Transformador de Corrente
class Transformador_de_Corrente(QtWidgets.QMainWindow):
    def __init__(self):
        super(Transformador_de_Corrente, self).__init__()
        uic.loadUi('Transformador de Corrente.ui', self)



# Função Main
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    app.exec_()

# Roda a Main
if __name__ == "__main__":
    main()