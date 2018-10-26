import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget): 

	def __init__(self):
		super(Window, self).__init__()
		self.initUI()

	def initUI(self):
		self.setFixedSize(400, 400)
		QtGui.QToolTip.setFont(QtGui.QFont('Arial', 10))
		self.setToolTip('example')

		add = self.createButton('+', 300, 300)
		sub = self.createButton('-', 300, 350)
		div = self.createButton('÷', 300, 250)
		mult = self.createButton('x', 300, 200)


		one = self.createButton('1', 20, 350)
		two = self.createButton('2', 110, 350)
		three = self.createButton('3', 200, 350)
		four = self.createButton('4', 20, 300)
		five = self.createButton('5', 110, 300)
		six = self.createButton('6', 200, 300)
		seven = self.createButton('7', 20, 250)
		eight = self.createButton('8', 110, 250)
		nine = self.createButton('9', 200, 250)
		equals = self.createButton('=', 200, 300)


		self.setGeometry(500, 200, 400, 400)
		self.setWindowTitle('Calculator')    
		self.show()


	def createButton(self, operation, x, y):
		btn = QtGui.QPushButton(str(operation), self)
		btn.resize(btn.sizeHint())
		btn.move(x, y) 
		return btn




def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())




if __name__ == '__main__':
	main()
