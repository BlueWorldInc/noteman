#!/usr/bin/python
import sys, random
from PySide6 import QtWidgets, QtGui, QtCore

class Communicate(QtCore.QObject):    
	# closeApp = QtCore.Signal()
	updateBW = QtCore.Signal(int)

class BurningWidget(QtWidgets.QWidget):

	def __init__(self):
		super(BurningWidget, self).__init__()
		self.initUI()

	def initUI(self):
		self.setMinimumSize(1, 30)
		self.value = 75
		self.num = [75, 150, 225, 375, 450, 525, 600, 675]

	def setValue(self, value):
		self.value = value
	
	def paintEvent(self, e):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawWidget(qp)
		qp.end()

	def drawWidget(self, qp):
		font = QtGui.QFont('Serif', 7, QtGui.QFont.Light)
		qp.setFont(font)

		size = self.size()
		w = size.width()
		h = size.height()
		step = int(round(w / 10.0))

		till = int(((w / 750.0) * self.value))
		full = int(((w / 750.0) * 700))

		if self.value >= 700:
			qp.setPen(QtGui.QColor(255, 255, 255))
			qp.setBrush(QtGui.QCloseEvent(255, 255, 184))
			qp.drawRect(0, 0, full, h)
			qp.setPen(QtGui.QColor(255, 175, 175))
			qp.setBrush(QtGui.QColor(255, 175, 175))
			qp.drawRect(full, 0, till-full, h)
		else:
			qp.setPen(QtGui.QColor(255, 255, 255))
			qp.setBrush(QtGui.QColor(255, 255, 184))
			qp.drawRect(0, 0, till, h)

		pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1,
			QtCore.Qt.SolidLine)

		qp.setPen(pen)
		qp.setBrush(QtCore.Qt.NoBrush)
		qp.drawRect(0, 0, w-1, h-1)

		j = 0

		for i in range(step, 10 * step, step):
			qp.drawLine(i, 0, i, 5)
			metrics = qp.fontMetrics()
			fw = metrics.width(str(self.num[j]))
			qp.drawText(i - fw / 2, h / 2, str(self.num[j]))
			j = j + 1

# class Button(QtWidgets.QPushButton):
#     def __init__(self, title, parent):
#         super(Button, self).__init__(title, parent)
#         self.setAcceptDrops(True)

#     def dragEnterEvent(self, e):
#         if e.mimeData().hasFormat('text/plain'):
#             e.accept()
#         else:
#             e.ignore() 

#     def dropEvent(self, e):
#         self.setText(e.mimeData().text())

# class Button(QtWidgets.QPushButton):

#     def __init__(self, title, parent):
#         super().__init__(title, parent)


#     def mouseMoveEvent(self, e):
#         if e.buttons() != QtCore.Qt.RightButton:
#             return
#         mimeData = QtCore.QMimeData()

#         drag = QtGui.QDrag(self)
#         drag.setMimeData(mimeData)

#         drag.setHotSpot(e.position().toPoint() - self.rect().topLeft())

#         dropAction = drag.exec(QtCore.Qt.MoveAction)

#     def mousePressEvent(self, e):
#         super().mousePressEvent(e)
#         if e.button() == QtCore.Qt.LeftButton:
#             print('press')

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
		# self.statusBar().showMessage('Ready')

		# Menu
		# exitAction = QtGui.QAction(app_icon, '&Exit', self)
		# aboutAction = QtGui.QAction(app_icon, '&About', self)
		# exitAction.setShortcut('Ctrl+Q')
		# exitAction.setStatusTip('Exit application')
		# exitAction.triggered.connect(self.close)
		# menubar = self.menuBar()
		# fileMenu = menubar.addMenu('&File')
		# helpMenu = menubar.addMenu('&Help')
		# helpMenu.addAction(aboutAction)
		# fileMenu.addAction(exitAction)

		# Toolbars
		# exitAction = QtGui.QAction(app_icon, 'Exit', self)
		# exitAction.setShortcut('Ctrl+Q')
		# exitAction.triggered.connect(self.close)
		# self.toolbar = self.addToolBar('Exit')
		# self.toolbar.addAction(exitAction)
		# self.toolbar.setFloatable(False)
		# self.toolbar.setMovable(False)

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
		# note_icons_file_path = "C:\\Users\\neo\\Documents\\CODE\\Python\\Noteman\\gui\\elegant_font\\images\\PNG\\"
		# vol_icon = note_icons_file_path + 'icon_vol-mute.png'

		# sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
		# sld.setFocusPolicy(QtCore.Qt.NoFocus)
		# sld.setGeometry(30, 40, 100, 30)
		# sld.valueChanged[int].connect(self.changeValue)
		
		# self.label = QtWidgets.QLabel(self)
		# self.label.setPixmap(QtGui.QPixmap(vol_icon))
		# self.label.setGeometry(160, 40, 80, 30)

		# Slider picture
		# note_icons_file_path = "C:\\Users\\neo\\Pictures"
		# QtCore.QDir(note_icons_file_path).entryList()
		# self.label2 = QtWidgets.QLabel(self)
		# i = 0
		# y = 0
		# scale = 100
		# for x in QtCore.QDir(note_icons_file_path).entryList():
		# 	self.label = QtWidgets.QLabel(self)
		# 	pixmap = QtGui.QPixmap(note_icons_file_path + "\\" + x)
		# 	if not pixmap.isNull():
		# 		pixmap = pixmap.scaled(scale, scale)
		# 		self.label.setPixmap(pixmap)
		# 		self.label.setGeometry(pixmap.rect())
		# 		self.label.move(i * scale, y * scale)
		# 		i += 1
		# 		if (i * scale) == 1600:
		# 			i = 0
		# 			y += 1
		# 		# print(x)

		# Progress Bar
		# self.pbar = QtWidgets.QProgressBar(self)
		# self.pbar.setGeometry(30, 40, 200, 25)

		# self.btn = QtWidgets.QPushButton('Start', self)
		# self.btn.move(40, 80)
		# self.btn.clicked.connect(self.doAction)

		# self.timer = QtCore.QBasicTimer()
		# self.step = 0

		# Calendar Widget
		# cal = QtWidgets.QCalendarWidget(self)
		# cal.setGridVisible(True)
		# cal.move(20, 20)
		# cal.adjustSize()
		# cal.clicked[QtCore.QDate].connect(self.showDate)
		
		# self.lbl = QtWidgets.QLabel(self)
		# date = cal.selectedDate()
		# self.lbl.setText(date.toString())
		# self.lbl.move(130, 260)

		# Pixmap Widget
		# pixmap = QtGui.QPixmap(note_icons_file_path + "\\notes16x16.png")
		# lbl = QtWidgets.QLabel(self)
		# lbl.setPixmap(pixmap)

		# LineEdit Widget
		# self.lbl = QtWidgets.QLabel(self)
		# qle = QtWidgets.QLineEdit(self)
		# qle.move(60, 100)
		# self.lbl.move(60, 40)
		# qle.textChanged[str].connect(self.onChanged)

		# Splitter
		# hbox = QtWidgets.QHBoxLayout()

		# topleft = QtWidgets.QFrame(self)
		# topleft.setFrameShape(QtWidgets.QFrame.StyledPanel)
		# topright = QtWidgets.QFrame(self)
		# topright.setFrameShape(QtWidgets.QFrame.StyledPanel)
		# bottom = QtWidgets.QFrame(self)
		# bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)

		# splitter1 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
		# splitter1.addWidget(topleft)
		# splitter1.addWidget(topright)
		# splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
		# splitter2.addWidget(splitter1)
		# splitter2.addWidget(bottom)

		# hbox.addWidget(splitter2)
		# widget = QtWidgets.QWidget()
		# widget.setLayout(hbox)
		# self.setCentralWidget(widget)
		# QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Cleanlooks'))

		# Combobox
		# self.lbl = QtWidgets.QLabel("Ubuntu", self)

		# combo = QtWidgets.QComboBox(self)
		# combo.addItem("Ubuntu")
		# combo.addItem("Mandriva")
		# combo.addItem("Fedora")
		# combo.addItem("Red Hat")
		# combo.addItem("Gentoo")

		# combo.move(50, 50)
		# self.lbl.move(50, 150)

		# combo.currentTextChanged.connect(self.onActivated)

		# Drag and Drop
		# qe = QtWidgets.QLineEdit('', self)
		# qe.setDragEnabled(True)
		# qe.move(30, 65)

		# Drag and Drop button
		# self.button = Button("Button", self)
		# self.button.move(190, 65)
		# self.setAcceptDrops(True)

		# Drawing Text
		# self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
		# 	\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
		# 	\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

		# Drawing Points
		# self.timer = QtCore.QTimer(self)
		# self.timer.timeout.connect(self.update)
		# self.timer.start(1)

		# Drawing Colors
		# self.lbl = QtWidgets.QLabel('Colors Fusion', self)
		# self.lbl.move(160, 20)

		# Drawing Lines
		# sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
		# sld.setFocusPolicy(QtCore.Qt.NoFocus)
		# sld.setGeometry(20, 270, 200, 10)
		# sld.setMaximum(10)
		# self.lineSize = 2
		# sld.valueChanged[int].connect(self.changeLineSize)

		# # Drawing Brush
		# self.brushs = [QtCore.Qt.SolidPattern, QtCore.Qt.Dense1Pattern, QtCore.Qt.Dense2Pattern, QtCore.Qt.Dense3Pattern, QtCore.Qt.DiagCrossPattern, QtCore.Qt.Dense5Pattern, QtCore.Qt.Dense6Pattern, QtCore.Qt.HorPattern, QtCore.Qt.VerPattern, QtCore.Qt.BDiagPattern]
		# self.currentBrush = 1
		# self.brush = QtGui.QBrush(self.brushs[self.currentBrush])

		# self.leftArrowBtn = QtWidgets.QPushButton("<", self)
		# self.leftArrowBtn.move(130, 265)
		# self.leftArrowBtn.setFixedWidth(30)
		# self.leftArrowBtn.clicked.connect(self.drawChange)
		# self.rightArrowBtn = QtWidgets.QPushButton(">", self)
		# self.rightArrowBtn.move(190, 265)
		# self.rightArrowBtn.setFixedWidth(30)
		# self.rightArrowBtn.clicked.connect(self.drawChange)

		# Custom Widget
		sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
		sld.setFocusPolicy(QtCore.Qt.NoFocus)
		sld.setRange(1, 750)
		sld.setValue(75)
		sld.setGeometry(30, 40, 150, 30)

		self.c = Communicate()
		self.wid = BurningWidget()
		self.c.updateBW[int].connect(self.wid.setValue)

		sld.valueChanged[int].connect(self.changeValue)
		hbox = QtWidgets.QHBoxLayout()
		hbox.addWidget(self.wid)
		vbox = QtWidgets.QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)

		widget = QtWidgets.QWidget()
		widget.setLayout(vbox)
		self.setCentralWidget(widget)

		self.setGeometry(0, 0, 550, 450)
		self.setWindowTitle('Icon')
		self.center()
		self.show()

	def changeValue(self, value):
		self.c.updateBW.emit(value)
		self.wid.repaint()

	# def paintEvent(self, e):
	# 	qp = QtGui.QPainter()
	# 	qp.begin(self)
	# 	# self.drawCircle(qp)
	# 	# self.drawLines(qp)
	# 	self.drawBigBrushes(qp)
	# 	qp.end()

	# def drawCircle(self, qp):
	# 	qp.setPen(QtCore.Qt.NoPen)

	# 	qp.setBrush(QtGui.QColor(0, 255, 0, 200))
	# 	qp.drawEllipse(180, 100, 100, 100)

	# 	qp.setBrush(QtGui.QColor(0, 0, 255, 200))
	# 	qp.drawEllipse(100, 100, 100, 100)

	# 	qp.setBrush(QtGui.QColor(255, 0, 0, 200))
	# 	qp.drawEllipse(140, 140, 100, 100)

	# def changeLineSize(self, value):
	# 	print (value)
	# 	self.lineSize = value
	# 	self.update()

	# def drawChange(self):
	# 	if (self.sender().text() == ">"):
	# 		if (self.currentBrush + 1 == len(self.brushs)):
	# 			self.currentBrush = 0
	# 		else:
	# 			self.currentBrush += 1
	# 	else:
	# 		if (self.currentBrush == 0):
	# 			self.currentBrush = len(self.brushs) - 1
	# 		else:
	# 			self.currentBrush -= 1

	# 	self.update()

	# def drawBigBrushes(self, qp):
	# 	qp.setBrush(self.brushs[self.currentBrush])
	# 	qp.drawRect(30, 50, 300, 200)

	# def drawBrushes(self, qp):
	# 	brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
	# 	qp.setBrush(brush)
	# 	qp.drawRect(10, 15, 90, 60)

	# 	brush.setStyle(QtCore.Qt.Dense1Pattern)
	# 	qp.setBrush(brush)
	# 	qp.drawRect(130, 15, 90, 60)

	# 	brush.setStyle(QtCore.Qt.Dense2Pattern)
	# 	qp.setBrush(brush)
	# 	qp.drawRect(250, 15, 90, 60)

	# 	brush.setStyle(QtCore.Qt.Dense3Pattern)
	# 	qp.setBrush(brush)
	# 	qp.drawRect(10, 105, 90, 60)

	# 	brush.setStyle(QtCore.Qt.DiagCrossPattern)
	# 	qp.setBrush(brush)
	# 	qp.drawRect(10, 105, 90, 60)

	# 	brush.setStyle(QtCore.Qt.Dense5Pattern)
	# 	qp.setBrush(brush)
	# 	qp.drawRect(130, 105, 90, 60)

	# 	brush.setStyle(QtCore.Qt.Dense6Pattern)
	# 	qp.setBrush(brush)
	# 	qp.drawRect(250, 105, 90, 60)

	# 	brush.setStyle(QtCore.Qt.HorPattern)
	# 	qp.setBrush(brush)
	# 	qp.drawRect(10, 195, 90, 60)

	# 	brush.setStyle(QtCore.Qt.VerPattern)
	# 	qp.setBrush(brush)
	# 	qp.drawRect(130, 195, 90, 60)

	# 	brush.setStyle(QtCore.Qt.BDiagPattern)
	# 	qp.setBrush(brush)
	# 	qp.drawRect(250, 195, 90, 60)

	# def drawLines(self, qp):
	# 	pen = QtGui.QPen(QtCore.Qt.black, self.lineSize, QtCore.Qt.SolidLine)
	# 	qp.setPen(pen)
	# 	qp.drawLine(20, 40, 250, 40)

	# 	pen.setStyle(QtCore.Qt.DashLine)
	# 	qp.setPen(pen)
	# 	qp.drawLine(20, 80, 250, 80)

	# 	pen.setStyle(QtCore.Qt.DashDotLine)
	# 	qp.setPen(pen)
	# 	qp.drawLine(20, 120, 250, 120)

	# 	pen.setStyle(QtCore.Qt.DotLine)
	# 	qp.setPen(pen)
	# 	qp.drawLine(20, 160, 250, 160)

	# 	pen.setStyle(QtCore.Qt.DashDotDotLine)
	# 	qp.setPen(pen)
	# 	qp.drawLine(20, 200, 250, 200)

	# 	pen.setStyle(QtCore.Qt.CustomDashLine)
	# 	pen.setDashPattern([1, 4, 5, 4])
	# 	qp.setPen(pen)
	# 	qp.drawLine(20, 240, 250, 240)
	
	# def paintEvent(self, e):
		# qp = QtGui.QPainter()
		# qp.begin(self)
		# self.drawRectangles(qp)
		# qp.end()

	# def drawRectangles(self, qp):
		# color = QtGui.QColor(0, 0, 0)
		# color.setNamedColor('#d4d4d4')
		# qp.setPen(color)

		# qp.setBrush(QtGui.QColor(200, 0, 0))
		# qp.drawRect(10, 15, 90, 60)

		# qp.setBrush(QtGui.QColor(255, 80, 0, 160))
		# qp.drawRect(130, 15, 90, 60)

		# qp.setBrush(QtGui.QColor(25, 0, 90, 200))
		# qp.drawRect(250, 15, 90, 60)

	# def paintEvent(self, e):
			# self.qp = QtGui.QPainter()
			# self.qp.begin(self)
			# self.drawPoints(self.qp)
			# self.qp.end()

	# def drawPoints(self, qp):
		# qp.setPen(QtCore.Qt.red)
		# size = self.size()
		# for i in range(1000):
			# x = random.randint(1, size.width()-1)
			# y = random.randint(1, size.height()-1)
			# qp.drawPoint(x, y)

	# def paintEvent(self, event):
	# 	qp = QtGui.QPainter()
	# 	qp.begin(self)
	# 	self.drawText(event, qp)
	# 	qp.end()
        
	# def drawText(self, event, qp):
	# 	qp.setPen(QtGui.QColor(168, 134, 13))
	# 	qp.setFont(QtGui.QFont('SansSerif', 10))
	# 	qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text) 

	# def dragEnterEvent(self, e):
		# e.accept()
	
	# def dropEvent(self, e):
		# position = e.position()
		# self.button.move(position.toPoint())
		# e.setDropAction(QtCore.Qt.MoveAction)
		# e.accept()

	# def onActivated(self, text):
		# self.lbl.setText(text)
		# self.lbl.adjustSize()  

	# def onChanged(self, text):
	# 	self.lbl.setText(text)
	# 	self.lbl.adjustSize() 

	# def showDate(self, date):     
		# self.lbl.setText(date.toString())

	# def timerEvent(self, e):
      
	# 	if self.step >= 100:
	# 		self.timer.stop()
	# 		self.btn.setText('Finished')
	# 		return
	# 	self.step = self.step + 1
	# 	self.pbar.setValue(self.step)

	# def doAction(self):
		
	# 	if self.timer.isActive():
	# 		self.timer.stop()
	# 		self.btn.setText('Start')
	# 	else:
	# 		if self.step >= 100:
	# 			return
	# 		self.timer.start(100, self)
	# 		self.btn.setText('Stop')

	# def changeValue(self, value):
	# 	note_icons_file_path = "C:\\Users\\neo\\Documents\\CODE\\Python\\Noteman\\gui\\elegant_font\\images\\PNG\\"
	# 	if value == 0:
	# 		self.label.setPixmap(QtGui.QPixmap(note_icons_file_path + 'icon_vol-mute.png'))
	# 	elif value > 0 and value <= 30:
	# 		self.label.setPixmap(QtGui.QPixmap(note_icons_file_path + 'icon_volume-low.png'))
	# 	elif value > 30 and value < 80:
	# 		self.label.setPixmap(QtGui.QPixmap(note_icons_file_path + 'icon_volume-high.png'))
	# 	else:
	# 		self.label.setPixmap(QtGui.QPixmap(note_icons_file_path + 'icon_volume-high.png'))

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
