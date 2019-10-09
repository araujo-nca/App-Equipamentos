from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mainwindow.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton_Condutores') # Find the button
        self.button.clicked.connect(self.on_click) # Remember to pass the definition/method, not the return value!

        self.label = self.findChild(QtWidgets.QLabel, 'labelEquipamentosEletricos')

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.label.setText('some text')

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()