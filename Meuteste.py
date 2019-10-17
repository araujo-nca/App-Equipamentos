import sys

from PyQt5 import QtWidgets


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 200, 100)
        self.button = QtWidgets.QPushButton('Toggle second window', self)
        self.button.setGeometry(20, 20, 160, 30)

        self.app2 = App2()
        self.button.clicked.connect(self.toggle_app2)

    def toggle_app2(self):
        if self.app2.isHidden():
            self.app2.show()
        else:
            self.app2.hide()


class App2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 100, 200, 200)
        self.editor = QtWidgets.QTextEdit('Wow such text', self)
        self.editor.setGeometry(20, 20, 160, 160)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = App()
    gui.show()
    app.exec_()