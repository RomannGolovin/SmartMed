# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MetricsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MetricsWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        MainWindow.setToolTipDuration(5)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonNext = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNext.setGeometry(QtCore.QRect(480, 420, 113, 32))
        self.pushButtonNext.setToolTipDuration(10)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(330, 420, 113, 32))
        self.pushButtonBack.setToolTipDuration(10)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.label.setObjectName("label")
        self.pushButtonCountQ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCountQ.setGeometry(QtCore.QRect(150, 100, 51, 31))
        self.pushButtonCountQ.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/timofejvilkov/Desktop/q.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCountQ.setIcon(icon)
        self.pushButtonCountQ.setObjectName("pushButtonCountQ")
        self.pushButtonStdQ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStdQ.setGeometry(QtCore.QRect(290, 180, 51, 31))
        self.pushButtonStdQ.setText("")
        self.pushButtonStdQ.setIcon(icon)
        self.pushButtonStdQ.setObjectName("pushButtonStdQ")
        self.pushButtonQuantsQ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonQuantsQ.setGeometry(QtCore.QRect(170, 310, 51, 31))
        self.pushButtonQuantsQ.setText("")
        self.pushButtonQuantsQ.setIcon(icon)
        self.pushButtonQuantsQ.setObjectName("pushButtonQuantsQ")
        self.checkBoxMax = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxMax.setGeometry(QtCore.QRect(10, 231, 248, 20))
        self.checkBoxMax.setObjectName("checkBoxMax")
        self.checkBoxMin = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxMin.setGeometry(QtCore.QRect(10, 274, 242, 20))
        self.checkBoxMin.setObjectName("checkBoxMin")
        self.checkBoxQuants = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxQuants.setGeometry(QtCore.QRect(10, 317, 149, 20))
        self.checkBoxQuants.setObjectName("checkBoxQuants")
        self.checkBoxCount = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxCount.setGeometry(QtCore.QRect(10, 102, 124, 20))
        self.checkBoxCount.setObjectName("checkBoxCount")
        self.checkBoxMean = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxMean.setGeometry(QtCore.QRect(10, 145, 153, 20))
        self.checkBoxMean.setObjectName("checkBoxMean")
        self.checkBoxStd = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxStd.setGeometry(QtCore.QRect(10, 188, 259, 20))
        self.checkBoxStd.setObjectName("checkBoxStd")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonNext.setText(_translate("MainWindow", "Далее"))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Выбор статистических метрик</span></p></body></html>"))
        self.checkBoxMax.setText(_translate("MainWindow", "максимальное значение в столбце"))
        self.checkBoxMin.setText(_translate("MainWindow", "минимальное значение в столбце"))
        self.checkBoxQuants.setToolTip(_translate("MainWindow", "<html><head/><body><p>По этим значениям можно оценить распределение выборки</p><p><br/></p></body></html>"))
        self.checkBoxQuants.setText(_translate("MainWindow", "квантили 25, 50, 75"))
        self.checkBoxCount.setText(_translate("MainWindow", "объем выборки"))
        self.checkBoxMean.setText(_translate("MainWindow", "среднее по столбцу"))
        self.checkBoxStd.setToolTip(_translate("MainWindow", "<html><head/><body><p>Показывает разброс значений в столбце</p></body></html>"))
        self.checkBoxStd.setText(_translate("MainWindow", "стандартное отклонение по столбцу"))
