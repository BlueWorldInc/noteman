#!/usr/bin/python
import sys
from PySide6 import QtWidgets, QtGui, QtCore

class Communicate(QtCore.QObject):    
    closeApp = QtCore.Signal()

class Example(QtWidgets.QMainWindow):

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
		# qbtn = QtWidgets.QPushButton('Quit', self)
		# qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

		# Icon
		note_icons_file_path = "C:\\Users\\neo\\Documents\\CODE\\Python\\Noteman\\gui\\"
		app_icon = QtGui.QIcon()
		app_icon.addFile(note_icons_file_path + 'notes16x16.png', QtCore.QSize(16,16))
		self.setWindowIcon(app_icon)

		# Status Bar
		self.statusBar().showMessage('Ready')

		# Menu
		exitAction = QtGui.QAction(app_icon, '&Exit', self)
		aboutAction = QtGui.QAction(app_icon, '&About', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.close)
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		helpMenu = menubar.addMenu('&Help')
		helpMenu.addAction(aboutAction)
		fileMenu.addAction(exitAction)

		# Toolbars
		# exitAction = QtGui.QAction(app_icon, 'Exit', self)
		# exitAction.setShortcut('Ctrl+Q')
		# exitAction.triggered.connect(self.close)
		# self.toolbar = self.addToolBar('Exit')
		# self.toolbar.addAction(exitAction)
		# self.toolbar.setFloatable(False)
		# self.toolbar.setMovable(False)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Icon')

		# TextEdit
		# textEdit = QtWidgets.QTextEdit()
		# self.setCentralWidget(textEdit)
		
		# Layout
		# label1 = QtWidgets.QLabel('Zetcode', self)
		# label1.move(15, 10)
		# label2 = QtWidgets.QLabel('tutorials', self)
		# label2.move(35, 40)
		# label3 = QtWidgets.QLabel('for programmers', self)
		# label3.move(55, 70)

		# Box Layout
		# okButton = QtWidgets.QPushButton("OK")
		# cancelButton = QtWidgets.QPushButton("Cancel")
		# hbox = QtWidgets.QHBoxLayout()
		# hbox.addStretch(1)
		# hbox.addWidget(okButton)
		# hbox.addWidget(cancelButton)
		# vbox = QtWidgets.QVBoxLayout()
		# vbox.addStretch(1)
		# vbox.addLayout(hbox)
		# widget = QtWidgets.QWidget()
		# widget.setLayout(vbox)
		# self.setCentralWidget(widget)

		# Grid Layout
		# names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
        #         '4', '5', '6', '*', '1', '2', '3', '-',
        #         '0', '.', '=', '+']

		# grid = QtWidgets.QGridLayout()

		# j = 0
		# pos = [(0, 0), (0, 1), (0, 2), (0, 3),
        #         (1, 0), (1, 1), (1, 2), (1, 3),
        #         (2, 0), (2, 1), (2, 2), (2, 3),
        #         (3, 0), (3, 1), (3, 2), (3, 3 ),
        #         (4, 0), (4, 1), (4, 2), (4, 3)]

		# for i in names:
		# 	button = QtWidgets.QPushButton(i)
		# 	if j == 2:
		# 		grid.addWidget(QtWidgets.QLabel(''), 0, 2)
		# 	else: grid.addWidget(button, pos[j][0], pos[j][1])
		# 	j = j + 1

		# widget = QtWidgets.QWidget()
		# widget.setLayout(grid)
		# self.setCentralWidget(widget)

		# Grid Layout 2

		# title = QtWidgets.QLabel('Title')
		# author = QtWidgets.QLabel('Author')
		# review = QtWidgets.QLabel('Review')

		# titleEdit = QtWidgets.QLineEdit()
		# authorEdit = QtWidgets.QLineEdit()
		# reviewEdit = QtWidgets.QTextEdit()

		# grid = QtWidgets.QGridLayout()
		# grid.setSpacing(10)

		# grid.addWidget(title, 1, 0)
		# grid.addWidget(titleEdit, 1, 1)

		# grid.addWidget(author, 2, 0)
		# grid.addWidget(authorEdit, 2, 1)

		# grid.addWidget(review, 3, 0)
		# grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
		# widget = QtWidgets.QWidget()
		# widget.setLayout(grid)
		# self.setCentralWidget(widget)
		
		# Signals and Slots
		# lcd = QtWidgets.QLCDNumber(self)
		# sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)

		# vbox = QtWidgets.QVBoxLayout()
		# vbox.addWidget(lcd)
		# vbox.addWidget(sld)

		# widget = QtWidgets.QWidget()
		# widget.setLayout(vbox)
		# self.setCentralWidget(widget)
		# sld.valueChanged.connect(lcd.display)

		# Event Sender
		# btn1 = QtWidgets.QPushButton("Button 1", self)
		# btn1.move(30, 50)
		# btn2 = QtWidgets.QPushButton("Button 2", self)
		# btn2.move(150, 50)
		# btn1.clicked.connect(self.buttonClicked)            
		# btn2.clicked.connect(self.buttonClicked)
		# self.statusBar()

		# Custom Signals
		# self.c = Communicate()
		# self.c.closeApp.connect(self.close)  

		# Inputs dialog
		self.btn = QtWidgets.QPushButton('Dialog', self)
		self.btn.move(20, 20)
		self.btn.clicked.connect(self.showDialog)
		# widget = QtWidgets.QWidget()
		# widget.setLayout(vbox)
		# self.setCentralWidget(widget)
		self.le = QtWidgets.QLineEdit(self)
		self.le.move(130, 22)

		self.center()
		self.show()

	def showDialog(self):
		text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 
		    'Enter your name:')
			
		if ok:
			self.le.setText(str(text))

	# def mousePressEvent(self, event):
	    # self.c.closeApp.emit()

	# def buttonClicked(self):
	# 	sender = self.sender()
	# 	self.statusBar().showMessage(sender.text() + ' was pressed')


	# def keyPressEvent(self, e):
		# if e.key() == QtCore.Qt.Key_Escape:
			# self.close()

	# def closeEvent(self, event):
		# reply = QtWidgets.QMessageBox.question(self, 'Message',
	    # "Are you sure to quit?", QtWidgets.QMessageBox.Yes | 
    	# QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

		# if reply == QtWidgets.QMessageBox.Yes:
		#     event.accept()
		# else:
		#     event.ignore()
	
	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
