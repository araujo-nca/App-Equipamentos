from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
import sys

class Condutores(QtWidgets.QMainWindow):
    def __init__(self):
        super(Condutores, self).__init__()
        uic.loadUi('Condutores.ui', self)



        self.show()

    @pyqtSlot()
    def on_click(self):
        self.label.setText('João Pedro dá cu')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Condutores()
    app.exec_()

if __name__ == "__main__":
    main()