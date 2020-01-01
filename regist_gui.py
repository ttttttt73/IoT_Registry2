import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel
from PyQt5 import QtGui

form_class = uic.loadUiType("regist_gui.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.modelcsv = QStandardItemModel()

        # Connect button's function
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)
        self.pushbutton.clicked.connect(self.pushbuttonClicked)
        self.dialog = Second()

        # qTableWidgetItem
        self.setTableWidgetData()

    # Define button's function
    def button1Function(self):
        print("btn_1 Clicked")

    def button2Function(self):
        print("btn_2 Clicked")

    def pushbuttonClicked(self):
        self.dialog.show()

    def setTableWidgetData(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0, 0)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0, 1)"))


class Second(QMainWindow):
    def __init__(self):
        super(Second, self).__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()