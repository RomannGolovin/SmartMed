# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloadWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class DownloadWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 170, 271, 26))
        self.comboBox.setToolTipDuration(10)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 270, 271, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(330, 420, 113, 32))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.pushButtonNext = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNext.setGeometry(QtCore.QRect(460, 420, 113, 32))
        self.pushButtonNext.setObjectName("pushButtonNext")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setToolTip(_translate("MainWindow", "tool tip", "tool tip"))
        self.pushButton.setText(_translate("MainWindow", "Загрузите файл"))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))
        self.pushButtonNext.setText(_translate("MainWindow", "Вперед"))
