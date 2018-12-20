# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import operator


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(Ui_MainWindow, self).__init__()

		self.multClicked = False
		self.pendingMult = 1
		self.digits = []
		self.numbers = []

		self.setupUi(self)
		
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("Calculator"))
		MainWindow.resize(305, 383)
		MainWindow.setMinimumSize(QtCore.QSize(305, 383))
		MainWindow.setMaximumSize(QtCore.QSize(305, 383))
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 100, 71, 261))
		self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.pushButton_11 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
		self.verticalLayout_2.addWidget(self.pushButton_11)
		self.pushButton_12 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
		self.verticalLayout_2.addWidget(self.pushButton_12)
		self.pushButton_10 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
		self.verticalLayout_2.addWidget(self.pushButton_10)
		self.pushButton_13 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
		self.verticalLayout_2.addWidget(self.pushButton_13)
		self.pushButton_14 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
		self.verticalLayout_2.addWidget(self.pushButton_14)
		self.pushButton_15 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
		self.verticalLayout_2.addWidget(self.pushButton_15)
		self.layoutWidget = QtGui.QWidget(self.centralwidget)
		self.layoutWidget.setGeometry(QtCore.QRect(0, 120, 211, 261))
		self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
		self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
		self.gridLayout_2.setMargin(0)
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.pushButton_7 = QtGui.QPushButton(self.layoutWidget)
		self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
		self.gridLayout_2.addWidget(self.pushButton_7, 0, 0, 1, 1)
		self.pushButton_8 = QtGui.QPushButton(self.layoutWidget)
		self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
		self.gridLayout_2.addWidget(self.pushButton_8, 0, 1, 1, 1)
		self.pushButton_9 = QtGui.QPushButton(self.layoutWidget)
		self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
		self.gridLayout_2.addWidget(self.pushButton_9, 0, 2, 1, 1)
		self.pushButton_4 = QtGui.QPushButton(self.layoutWidget)
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)
		self.pushButton_5 = QtGui.QPushButton(self.layoutWidget)
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)
		self.pushButton_6 = QtGui.QPushButton(self.layoutWidget)
		self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
		self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)
		self.pushButton = QtGui.QPushButton(self.layoutWidget)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
		self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 1)
		self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.gridLayout_2.addWidget(self.pushButton_3, 2, 2, 1, 1)
		self.lcdNumber = QtGui.QLCDNumber(9, self.centralwidget)
		self.lcdNumber.setGeometry(QtCore.QRect(20, 20, 271, 51))
		self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
		self.layoutWidget.raise_()
		self.verticalLayoutWidget.raise_()
		self.lcdNumber.raise_()
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.setButtons()

		self.show()

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "Calculator", None))
		self.pushButton_11.setText(_translate("MainWindow", "CE", None))
		self.pushButton_12.setText(_translate("MainWindow", "x", None))
		self.pushButton_10.setText(_translate("MainWindow", "÷", None))
		self.pushButton_13.setText(_translate("MainWindow", "−", None))
		self.pushButton_14.setText(_translate("MainWindow", "+", None))
		self.pushButton_15.setText(_translate("MainWindow", "=", None))
		self.pushButton_7.setText(_translate("MainWindow", "1", None))
		self.pushButton_8.setText(_translate("MainWindow", "2", None))
		self.pushButton_9.setText(_translate("MainWindow", "3", None))
		self.pushButton_4.setText(_translate("MainWindow", "4", None))
		self.pushButton_5.setText(_translate("MainWindow", "5", None))
		self.pushButton_6.setText(_translate("MainWindow", "6", None))
		self.pushButton.setText(_translate("MainWindow", "7", None))
		self.pushButton_2.setText(_translate("MainWindow", "8", None))
		self.pushButton_3.setText(_translate("MainWindow", "9", None))

	def setButtons(self):
		self.pushButton_7.clicked.connect(self.digit_clicked)
		self.pushButton_8.clicked.connect(self.digit_clicked)
		self.pushButton_9.clicked.connect(self.digit_clicked)
		self.pushButton_4.clicked.connect(self.digit_clicked)
		self.pushButton_5.clicked.connect(self.digit_clicked)
		self.pushButton_6.clicked.connect(self.digit_clicked)
		self.pushButton.clicked.connect(self.digit_clicked)
		self.pushButton_2.clicked.connect(self.digit_clicked)
		self.pushButton_3.clicked.connect(self.digit_clicked)

		self.pushButton_11.clicked.connect(self.clear)
		self.pushButton_12.clicked.connect(self.multiply)
		self.pushButton_15.clicked.connect(self.equals)

		

	def digit_clicked(self):
		number = ''
		sender = self.sender()
		self.digits.append(int(sender.text()))

		if len(self.digits) < 10:
			for digit in self.digits:
				number += str(digit)
		else:
			self.lcdNumber.display('Error')
			self.digits.clear()

		self.lcdNumber.display(int(number))

	def clear(self):
		self.digits.clear()
		self.lcdNumber.display(0)
		self.pendingMult = 1

	def multiply(self):
		self.digits.clear()
		self.multClicked = True
		self.pendingMult *= self.lcdNumber.value()
		print(self.pendingMult)

	def equals(self):
		self.pendingMult *= self.lcdNumber.value()
		print(self.pendingMult)
		self.lcdNumber.display(self.pendingMult)
		self.pendingMult = 1
		print(self.pendingMult)




def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Ui_MainWindow()
	sys.exit(app.exec_())
	
main()
