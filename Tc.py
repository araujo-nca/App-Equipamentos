from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
import sys

class Tc(QtWidgets.QMainWindow):
    def __init__(self):
        super(Tc, self).__init__()
        uic.loadUi('Transformador de Corrente.ui', self)



        self.show()

    @pyqtSlot()
    def on_click(self):
        self.label.setText('João Pedro dá cu')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Tc()
    app.exec_()

if __name__ == "__main__":
    main()