# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productshow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from db_handler import *


class Ui_Productshow(object):
    def __init__(self, value):
        self.value = value

    def setupUi(self, Productshow):
        self.Productshow = Productshow
        Productshow.setObjectName("Productshow")
        Productshow.resize(987, 591)
        Productshow.setStyleSheet("background-color: rgba(251, 193, 193, 158);")
        self.centralwidget = QtWidgets.QWidget(Productshow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_prices = QtWidgets.QTableWidget(self.centralwidget)
        self.show_prices.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.show_prices.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.show_prices.setObjectName("show_prices")
        self.show_prices.setColumnCount(2)
        self.show_prices.setRowCount(0)
        self.show_prices.setStyleSheet("background-image: url(./imagenes/sophia_trans.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-color:rgb(255, 255, 255)")
        self.show_prices.horizontalHeader().setStyleSheet("background-color: rgb(255,255,255)")
        self.show_prices.verticalHeader().setStyleSheet("background-image: url(./imagenes/headerv.png)")
        self.show_prices.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.show_prices.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.show_prices.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.show_prices.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.show_prices)
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        self.close_button.setMinimumSize(QtCore.QSize(0, 43))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.close_button.setFont(font)
        self.close_button.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.close_button.setObjectName("close_button")
        self.verticalLayout.addWidget(self.close_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Productshow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Productshow)
        self.statusbar.setObjectName("statusbar")
        Productshow.setStatusBar(self.statusbar)

        self.retranslateUi(Productshow)
        QtCore.QMetaObject.connectSlotsByName(Productshow)


    def retranslateUi(self, Productshow):
        _translate = QtCore.QCoreApplication.translate
        Productshow.setWindowTitle(_translate("Productshow", "MainWindow"))
        self.show_prices.setSortingEnabled(True)
        item = self.show_prices.horizontalHeaderItem(0)
        item.setText(_translate("Productshow", "Nombre"))
        item = self.show_prices.horizontalHeaderItem(1)
        item.setText(_translate("Productshow", "Precio"))
        self.close_button.setText(_translate("Productshow", "Cerrar"))

        self.send_data_to_table()



        # Activation for close_button
        self.close_button.clicked.connect(self.close_button_clicked)

    def close_button_clicked(self):
        self.Productshow.close()

    def send_data_to_table(self):
        product = show_product(self.value,0)
        self.show_prices.setRowCount(0)
        for row_number, row_data, in enumerate(product):
            self.show_prices.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                font = QtGui.QFont()
                font.setPointSize(18)
                item.setFont(font)
                self.show_prices.setItem(row_number,column_number,item)
        self.show_prices.resizeColumnsToContents()            





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Productshow = QtWidgets.QMainWindow()
    ui = Ui_Productshow()
    ui.setupUi(Productshow)
    Productshow.show()
    sys.exit(app.exec_())