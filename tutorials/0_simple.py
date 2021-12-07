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

		# Inputs Dialog
		# self.btn = QtWidgets.QPushButton('Dialog', self)
		# self.btn.move(20, 20)
		# self.btn.clicked.connect(self.showDialog)
		# # widget = QtWidgets.QWidget()
		# # widget.setLayout(vbox)
		# # self.setCentralWidget(widget)
		# self.le = QtWidgets.QLineEdit(self)
		# self.le.move(130, 22)

		# Color Dialog
		# col = QtGui.QColor(0, 0, 0)
		# self.btn = QtWidgets.QPushButton('Dialog', self)
		# self.btn.move(20, 40)
		# self.btn.clicked.connect(self.showDialog)
		# self.frm = QtWidgets.QFrame(self)
		# self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
		# self.frm.setGeometry(130, 22, 100, 100) 

		# self.le = QtWidgets.QLineEdit(self)
		# self.le.move(130, 202)

		# Font Dialog
		# vbox = QtWidgets.QVBoxLayout()
		# btn = QtWidgets.QPushButton('Dialog', self)
		# btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed,
        #     QtWidgets.QSizePolicy.Fixed)
		# btn.move(20, 20)
		# btn.clicked.connect(self.showDialog)
		# self.lbl = QtWidgets.QLabel('Knowledge only matters', self)
		# self.lbl.move(130, 20)
		# self.lbl.setGeometry(130, 22, 1000, 1000)
		# vbox.addWidget(self.lbl)
		# self.setLayout(vbox)
		# vbox.addWidget(btn)

		# File Dialog
		# self.textEdit = QtWidgets.QTextEdit()
		# self.setCentralWidget(self.textEdit)
		# self.statusBar()

		# openFile = QtGui.QAction(app_icon, 'Open', self)
		# openFile.setShortcut('Ctrl+O')
		# openFile.setStatusTip('Open new File')
		# openFile.triggered.connect(self.showDialog)
		
		# menubar = self.menuBar()
		# fileMenu = menubar.addMenu('&File')
		# fileMenu.addAction(openFile)    

		# CheckBox
		# cb = QtWidgets.QCheckBox('Show title', self)
		# cb.move(20, 20)
		# cb.toggle()
		# cb.stateChanged.connect(self.changeTitle)

		# Toggle Button
		# self.col = QtGui.QColor(0, 0, 0)       
		# redb = QtWidgets.QPushButton('Red', self)
		# redb.setCheckable(True)
		# redb.move(10, 10)
		# redb.clicked[bool].connect(self.setColor)
		# greenb = QtWidgets.QPushButton('Green', self)
		# greenb.setCheckable(True)
		# greenb.move(10, 60)
		# greenb.clicked[bool].connect(self.setColor)
		# blueb = QtWidgets.QPushButton('Blue', self)
		# blueb.setCheckable(True)
		# blueb.move(10, 110)
		# blueb.clicked[bool].connect(self.setColor)
		# self.square = QtWidgets.QFrame(self)
		# self.square.setGeometry(150, 20, 100, 100)
		# self.square.setStyleSheet("QWidget { background-color: %s }" %  
        #     self.col.name())

		# Slider

		note_icons_file_path = "C:\\Users\\neo\\Documents\\CODE\\Python\\Noteman\\gui\\elegant_font\\images\\PNG\\"
		vol_icon = note_icons_file_path + 'icon_vol-mute.png'

		sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
		sld.setFocusPolicy(QtCore.Qt.NoFocus)
		sld.setGeometry(30, 40, 100, 30)
		sld.valueChanged[int].connect(self.changeValue)
		
		self.label = QtWidgets.QLabel(self)
		self.label.setPixmap(QtGui.QPixmap(vol_icon))
		self.label.setGeometry(160, 40, 80, 30)
		
		self.center()
		self.show()

	def changeValue(self, value):
		note_icons_file_path = "C:\\Users\\neo\\Documents\\CODE\\Python\\Noteman\\gui\\elegant_font\\images\\PNG\\"
		if value == 0:
			self.label.setPixmap(QtGui.QPixmap(note_icons_file_path + 'icon_vol-mute.png'))
		elif value > 0 and value <= 30:
			self.label.setPixmap(QtGui.QPixmap(note_icons_file_path + 'icon_volume-low.png'))
		elif value > 30 and value < 80:
			self.label.setPixmap(QtGui.QPixmap(note_icons_file_path + 'icon_volume-high.png'))
		else:
			self.label.setPixmap(QtGui.QPixmap(note_icons_file_path + 'icon_volume-high.png'))

	# def setColor(self, pressed):
	# 	source = self.sender()
				
	# 	if pressed:
	# 		val = 255
	# 	else: val = 0

	# 	if source.text() == "Red":
	# 		self.col.setRed(val)                
	# 	elif source.text() == "Green":
	# 		self.col.setGreen(val)             
	# 	else:
	# 		self.col.setBlue(val) 
		
	# 	self.square.setStyleSheet("QFrame { background-color: %s }" %
    #         self.col.name())  

	# def changeTitle(self, state):
      
	# 	if state == QtCore.Qt.Checked:
	# 		self.setWindowTitle('Checkbox')
	# 	else:
	# 		self.setWindowTitle('')

	# def showDialog(self):
	# 	fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
	# 	            '/home')
	# 	f = open(fname, 'r')
	# 	with f:
	# 		data = f.read()
	# 		self.textEdit.setText(data)

	# def showDialog(self):
	# 	ok, font = QtWidgets.QFontDialog.getFont()
	# 	if ok:
 	# 	    self.lbl.setFont(font)

	# def showDialog(self):
	# 	col = QtWidgets.QColorDialog.getColor()

	# 	if col.isValid():
	# 		self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

	# def showDialog(self):
	# 	text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 
	# 	    'Enter your name:')
	# 	if ok:
	# 		self.le.setText(str(text))

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
