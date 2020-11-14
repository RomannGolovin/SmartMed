# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreprocessingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class PreprocessingWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(10, 170, 271, 26))
        self.comboBox1.setToolTipDuration(10)
        self.comboBox1.setObjectName("comboBox1")
        self.pushButtonNext = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNext.setGeometry(QtCore.QRect(480, 420, 113, 32))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(330, 420, 113, 32))
        self.pushButtonBack.setAutoFillBackground(False)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -20, 431, 181))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 571, 51))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 271, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox1.setToolTip(_translate("MainWindow", "tool tip", "tool tip"))
        self.pushButtonNext.setText(_translate("MainWindow", "Далее"))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Предварительная обработка данных</span></p><p><br/><br/></p><p><span style=\" font-size:14pt;\">Выберите опции предварительной обработки данных:</span></p><p><span style=\" font-size:14pt;\">Метод заполнения пропущенных данных:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Для того, чтобы выполнить загрузку данных, кликните на кнопку ниже &quot;Загрузка данных&quot;.</p><p>В открывшемся окне выберите файл в формате <span style=\" font-weight:600;\">&quot;xlsx&quot;</span> или <span style=\" font-weight:600;\">&quot;csv&quot;</span>.</p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Загрузите файл"))
