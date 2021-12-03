#!/usr/bin/python
import sys
from PySide6 import QtWidgets, QtGui, QtCore


class Example(QtWidgets.QWidget):

	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		
		# ToolTips
		# QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		# self.setToolTip('This is a <b>QWidget</b> widget')
		# btn = QtWidgets.QPushButton('Button', self)
		# btn.resize(btn.sizeHint())
		# btn.move(50, 50)
		# btn.setToolTip('This is a <b>QPushButton</b> widget')

		# Exit button
		qbtn = QtWidgets.QPushButton('Quit', self)
		qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Icon')
		note_icons_file_path = "C:\\Users\\neo\\Documents\\CODE\\Python\\Noteman\\gui\\"
		app_icon = QtGui.QIcon()
		app_icon.addFile(note_icons_file_path + 'notes16x16.png', QtCore.QSize(16,16))
		self.setWindowIcon(app_icon)
		self.center()
		self.show()

	def closeEvent(self, event):
		reply = QtWidgets.QMessageBox.question(self, 'Message',
	    "Are you sure to quit?", QtWidgets.QMessageBox.Yes | 
    	QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

		if reply == QtWidgets.QMessageBox.Yes:
		    event.accept()
		else:
		    event.ignore()
	
	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QScreen().availableGeometry().center()
		qr.moveCenter(cp)
		# self.move(qr.topLeft())
		# self.move(qr.topLeft())
	

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
