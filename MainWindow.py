from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_Condutores') # Find the button
        self.button.clicked.connect(self.on_click) # Remember to pass the definition/method, not the return value!

        self.label = self.findChild(QtWidgets.QLabel, 'labelEquipamentosEletricos')

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.label.setText('João Pedro dá cu')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()

if __name__ == "__main__":
    main()