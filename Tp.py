from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
import sys

class Tp(QtWidgets.QMainWindow):
    def __init__(self):
        super(Tp, self).__init__()
        uic.loadUi('Transformador de Potencial.ui', self)



        self.show()

    @pyqtSlot()
    def on_click(self):
        self.label.setText('João Pedro dá cu')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Tp()
    app.exec_()

if __name__ == "__main__":
    main()