# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UniformityWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UniformityWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonDone = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDone.setGeometry(QtCore.QRect(460, 420, 113, 32))
        self.pushButtonDone.setObjectName("pushButtonDone")
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(330, 420, 113, 32))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 351, 51))
        self.label.setObjectName("label")
        self.radioButtonF = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonF.setGeometry(QtCore.QRect(110, 160, 241, 20))
        self.radioButtonF.setObjectName("radioButtonF")
        self.radioButtonLev = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonLev.setGeometry(QtCore.QRect(110, 210, 191, 20))
        self.radioButtonLev.setObjectName("radioButtonLev")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonDone.setText(_translate("MainWindow", "завершить"))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", " Выберите, каким способом выполнется \n"
" проверка данных на однородность:"))
        self.radioButtonF.setText(_translate("MainWindow", "F-критерий "))
        self.radioButtonLev.setText(_translate("MainWindow", "Критерий Левена"))