# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Tue Oct  8 23:24:24 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 450)
        MainWindow.setMinimumSize(QtCore.QSize(780, 450))
        MainWindow.setMaximumSize(QtCore.QSize(780, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("myIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Condutores = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Condutores.setGeometry(QtCore.QRect(500, 20, 249, 111))
        self.pushButton_Condutores.setStyleSheet("font: 10pt \"Lucida Sans Unicode\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Wire Cu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Condutores.setIcon(icon1)
        self.pushButton_Condutores.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Condutores.setAutoDefault(False)
        self.pushButton_Condutores.setFlat(False)
        self.pushButton_Condutores.setObjectName("pushButton_Condutores")
        self.pushButton_Tp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Tp.setGeometry(QtCore.QRect(500, 160, 249, 111))
        self.pushButton_Tp.setStyleSheet("font: 10pt \"Lucida Sans Unicode\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("TP.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Tp.setIcon(icon2)
        self.pushButton_Tp.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Tp.setObjectName("pushButton_Tp")
        self.pushButton_Tc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Tc.setGeometry(QtCore.QRect(500, 300, 249, 111))
        self.pushButton_Tc.setStyleSheet("font: 10pt \"Lucida Sans Unicode\";")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("TC.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Tc.setIcon(icon3)
        self.pushButton_Tc.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Tc.setObjectName("pushButton_Tc")
        self.labelImagemPrincipal = QtWidgets.QLabel(self.centralwidget)
        self.labelImagemPrincipal.setGeometry(QtCore.QRect(-30, 130, 521, 271))
        self.labelImagemPrincipal.setText("")
        self.labelImagemPrincipal.setPixmap(QtGui.QPixmap("My Post2.png"))
        self.labelImagemPrincipal.setScaledContents(True)
        self.labelImagemPrincipal.setObjectName("labelImagemPrincipal")
        self.labelEquipamentosEletricos = QtWidgets.QLabel(self.centralwidget)
        self.labelEquipamentosEletricos.setGeometry(QtCore.QRect(60, 10, 381, 91))
        self.labelEquipamentosEletricos.setStyleSheet("font: 24pt \"MS Reference Sans Serif\";\n"
"color: rgb(60, 66, 69);")
        self.labelEquipamentosEletricos.setObjectName("labelEquipamentosEletricos")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 781, 421))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_Condutores, QtCore.SIGNAL("clicked()"), self.widget.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Equipamentos Elétricos", None, -1))
        self.pushButton_Condutores.setText(QtWidgets.QApplication.translate("MainWindow", "Condutores                ", None, -1))
        self.pushButton_Tp.setText(QtWidgets.QApplication.translate("MainWindow", "Transformador de Potencial", None, -1))
        self.pushButton_Tc.setText(QtWidgets.QApplication.translate("MainWindow", "Transformador de Corrente", None, -1))
        self.labelEquipamentosEletricos.setText(QtWidgets.QApplication.translate("MainWindow", "Equipamentos Elétricos", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

