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
		super(Ui_MainWindow ,self).__init__()
		self.setupUi(self)
		self.number = ''
		self.numbers = []

		
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("Calculator"))
		MainWindow.setMinimumSize(QtCore.QSize(305, 383))
		MainWindow.setMaximumSize(QtCore.QSize(305, 383))
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 90, 71, 261))
		self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setMargin(0)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.pushButton_11 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
		self.verticalLayout_2.addWidget(self.pushButton_11)
		self.pushButton_14 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
		self.verticalLayout_2.addWidget(self.pushButton_14)
		self.pushButton_13 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
		self.verticalLayout_2.addWidget(self.pushButton_13)
		self.pushButton_12 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
		self.verticalLayout_2.addWidget(self.pushButton_12)
		self.pushButton_10 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
		self.verticalLayout_2.addWidget(self.pushButton_10)
		self.pushButton_15 = QtGui.QPushButton(self.verticalLayoutWidget)
		self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
		self.verticalLayout_2.addWidget(self.pushButton_15)
		self.widget = QtGui.QWidget(self.centralwidget)
		self.widget.setGeometry(QtCore.QRect(10, 118, 201, 261))
		self.widget.setObjectName(_fromUtf8("widget"))
		self.gridLayout_2 = QtGui.QGridLayout(self.widget)
		self.gridLayout_2.setMargin(0)
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.pushButton_7 = QtGui.QPushButton(self.widget)
		self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
		self.gridLayout_2.addWidget(self.pushButton_7, 0, 0, 1, 1)
		self.pushButton_8 = QtGui.QPushButton(self.widget)
		self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
		self.gridLayout_2.addWidget(self.pushButton_8, 0, 1, 1, 1)
		self.pushButton_9 = QtGui.QPushButton(self.widget)
		self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
		self.gridLayout_2.addWidget(self.pushButton_9, 0, 2, 1, 1)
		self.pushButton_4 = QtGui.QPushButton(self.widget)
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)
		self.pushButton_5 = QtGui.QPushButton(self.widget)
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)
		self.pushButton_6 = QtGui.QPushButton(self.widget)
		self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
		self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)
		self.pushButton = QtGui.QPushButton(self.widget)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
		self.pushButton_2 = QtGui.QPushButton(self.widget)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 1)
		self.pushButton_3 = QtGui.QPushButton(self.widget)
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.gridLayout_2.addWidget(self.pushButton_3, 2, 2, 1, 1)
		self.verticalLayoutWidget.raise_()
		self.pushButton_5.raise_()
		self.pushButton.raise_()
		self.pushButton_2.raise_()
		self.pushButton_3.raise_()
		self.pushButton_4.raise_()
		self.pushButton_5.raise_()
		self.pushButton_6.raise_()
		self.pushButton_7.raise_()
		self.pushButton_8.raise_()
		self.pushButton_9.raise_()
		self.verticalLayoutWidget.raise_()
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		self.actionAdd = QtGui.QAction(MainWindow)
		self.actionAdd.setIconVisibleInMenu(True)
		self.actionAdd.setObjectName(_fromUtf8("actionAdd"))

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.connect_push_buttons()		

		self.show()

	def connect_push_buttons(self):
		self.pushButton_7.clicked.connect(self.digit_clicked)
		self.pushButton_8.clicked.connect(self.digit_clicked)
		self.pushButton_9.clicked.connect(self.digit_clicked)
		self.pushButton_4.clicked.connect(self.digit_clicked)
		self.pushButton_5.clicked.connect(self.digit_clicked)
		self.pushButton_6.clicked.connect(self.digit_clicked)
		self.pushButton.clicked.connect(self.digit_clicked)
		self.pushButton_2.clicked.connect(self.digit_clicked)
		self.pushButton_3.clicked.connect(self.digit_clicked)


	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "Calculator", None))
		self.pushButton_11.setText(_translate("Calculator", "CE", None))
		self.pushButton_14.setText(_translate("Calculator", "+", None))
		self.pushButton_13.setText(_translate("Calculator", "−", None))
		self.pushButton_12.setText(_translate("Calculator", "x", None))
		self.pushButton_10.setText(_translate("Calculator", "÷", None))
		self.pushButton_15.setText(_translate("Calculator", "=", None))
		self.pushButton_7.setText(_translate("Calculator", "1", None))
		self.pushButton_8.setText(_translate("Calculator", "2", None))
		self.pushButton_9.setText(_translate("Calculator", "3", None))
		self.pushButton_4.setText(_translate("Calculator", "4", None))
		self.pushButton_5.setText(_translate("Caculator", "5", None))
		self.pushButton_6.setText(_translate("Calculator", "6", None))
		self.pushButton.setText(_translate("Calculator", "7", None))
		self.pushButton_2.setText(_translate("Calculator", "8", None))
		self.pushButton_3.setText(_translate("Calculator", "9", None))
		self.actionAdd.setText(_translate("Calculator", "add", None))


	def digit_clicked(self):
		sender = self.sender()
		self.number += sender.text()
		self.numbers.append(int(self.number))
		return int(self.number)

	def operator_clicked(self):
		return self.sender().text()

	def equals_clicked(self):
		if self.operator_clicked() == '+':
			return 



def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Ui_MainWindow()
	sys.exit(app.exec_())



main()