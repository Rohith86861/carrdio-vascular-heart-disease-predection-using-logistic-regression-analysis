# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cahe.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 324)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 70, 361, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 190, 361, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 130, 361, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 10, 361, 41))
        self.pushButton_5.setMaximumSize(QtCore.QSize(361, 41))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 250, 361, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 591, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Users/User/Desktop/j/WhatsApp Image 2020-03-14 at 1.38.38 PM (1).jpeg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.pushButton_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tool for cardiovascular disease & Hepatitis"))
        self.pushButton.setText(_translate("MainWindow", "Cardiovascular disease Symptoms"))
        self.pushButton_2.setText(_translate("MainWindow", "Test Results"))
        self.pushButton_3.setText(_translate("MainWindow", " Hepatitis Symptoms"))
        self.pushButton_5.setText(_translate("MainWindow", "Patient Profile Details "))
        self.pushButton_4.setText(_translate("MainWindow", "Prediction"))
