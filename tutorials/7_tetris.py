#!/usr/bin/python
import sys, random
from PySide6 import QtWidgets, QtGui, QtCore

class Board(QtWidgets.QFrame):
	BoardWidth = 10
	BoardHeight = 22
	Speed = 300

	def __init__(self, parent):
		super(Board, self).__init__()

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		rect = self.contentsRect()
		boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()
		self.drawSquare(painter,
                        rect.left() + j * self.squareWidth(),
                        boardTop + i * self.squareHeight(), 0)

	def drawSquare(self, painter, x, y, shape):
				
		colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
		              0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

		color = QtGui.QColor(colorTable[shape])
		painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
		    self.squareHeight() - 2, color)

		painter.setPen(color.lighter())
		painter.drawLine(x, y + self.squareHeight() - 1, x, y)
		painter.drawLine(x, y, x + self.squareWidth() - 1, y)

		painter.setPen(color.darker())
		painter.drawLine(x + 1, y + self.squareHeight() - 1,
		    x + self.squareWidth() - 1, y + self.squareHeight() - 1)
		painter.drawLine(x + self.squareWidth() - 1, 
		    y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)
