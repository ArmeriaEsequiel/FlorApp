# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saleswindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class Ui_SalesWindow(object):
    def setupUi(self, SalesWindow):
        self.SalesWindow = SalesWindow
        SalesWindow.setObjectName("SalesWindow")
        SalesWindow.resize(1048, 666)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SalesWindow.sizePolicy().hasHeightForWidth())
        SalesWindow.setSizePolicy(sizePolicy)
        SalesWindow.setMinimumSize(QtCore.QSize(1048, 666))
        SalesWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        SalesWindow.setStyleSheet("background-color: rgba(251, 193, 193, 158);")
        self.centralwidget = QtWidgets.QWidget(SalesWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        self.tableWidget.setStyleSheet("background-image: url(./imagenes/sophia_trans.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-color:rgb(255, 255, 255)")
        self.tableWidget.verticalHeader().setStyleSheet("background-image: url(./imagenes/headerv.png)")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.date_from = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_from.sizePolicy().hasHeightForWidth())
        self.date_from.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(29)
        self.date_from.setFont(font)
        self.date_from.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.date_from.setAlignment(QtCore.Qt.AlignCenter)
        self.date_from.setMinimumDate(QtCore.QDate(2021, 5, 1))
        self.date_from.setCalendarPopup(True)
        self.date_from.setCurrentSectionIndex(0)
        self.date_from.setDate(QtCore.QDate(2021, 5, 1))
        self.date_from.setObjectName("date_from")
        self.verticalLayout.addWidget(self.date_from)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.date_to = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_to.sizePolicy().hasHeightForWidth())
        self.date_to.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.date_to.setFont(font)
        self.date_to.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.date_to.setAlignment(QtCore.Qt.AlignCenter)
        self.date_to.setCalendarPopup(True)
        self.date_to.setDate(QtCore.QDate(2021, 1, 1))
        self.date_to.setObjectName("date_to")
        self.verticalLayout_2.addWidget(self.date_to)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.show_sales = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_sales.sizePolicy().hasHeightForWidth())
        self.show_sales.setSizePolicy(sizePolicy)
        self.show_sales.setMinimumSize(QtCore.QSize(42, 90))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.show_sales.setFont(font)
        self.show_sales.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.show_sales.setObjectName("show_sales")
        self.horizontalLayout_2.addWidget(self.show_sales)
        spacerItem3 = QtWidgets.QSpacerItem(37, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.close_button.setFont(font)
        self.close_button.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.close_button.setObjectName("close_button")
        self.verticalLayout_3.addWidget(self.close_button)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        SalesWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SalesWindow)
        self.statusbar.setObjectName("statusbar")
        SalesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SalesWindow)
        QtCore.QMetaObject.connectSlotsByName(SalesWindow)

    def retranslateUi(self, SalesWindow):
        _translate = QtCore.QCoreApplication.translate
        SalesWindow.setWindowTitle(_translate("SalesWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SalesWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SalesWindow", "Cantidad"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SalesWindow", "Codigo de Barras"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SalesWindow", "Estado"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SalesWindow", "Dia"))
        self.label_2.setText(_translate("SalesWindow", "Desde"))
        self.label_3.setText(_translate("SalesWindow", "Hasta"))
        self.show_sales.setText(_translate("SalesWindow", "Mostrar ventas"))
        self.close_button.setText(_translate("SalesWindow", "Cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    QtGui.QFontDatabase.addApplicationFont("./font/Chalinka/Chalinka-Regular.ttf")
    QtGui.QFontDatabase.addApplicationFont("./font/Z003-MediumItalic.ttf")
    SalesWindow = QtWidgets.QMainWindow()
    ui = Ui_SalesWindow()
    ui.setupUi(SalesWindow)
    SalesWindow.show()
    sys.exit(app.exec_())
