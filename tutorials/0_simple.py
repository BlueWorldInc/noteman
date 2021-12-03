#!/usr/bin/python
import sys
from PySide6 import QtWidgets, QtGui, QtCore


class Example(QtWidgets.QWidget):

	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Icon')
		note_icons_file_path = "C:\\Users\\neo\\Documents\\CODE\\Python\\Noteman\\gui\\"
		app_icon = QtGui.QIcon()
		app_icon.addFile(note_icons_file_path + 'notes16x16.png', QtCore.QSize(16,16))
		self.setWindowIcon(app_icon)
		self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
