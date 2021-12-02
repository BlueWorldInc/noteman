import sys
from PySide6.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout, QScrollBar
from PySide6 import QtGui, QtCore

app = QApplication(sys.argv)

fen = QWidget()
fen.setWindowTitle("Noteman")
note_icons_file_path = "C:\\Users\\neo\\Documents\\CODE\\Python\\Noteman\\gui\\"
app_icon = QtGui.QIcon()
app_icon.addFile(note_icons_file_path + 'notes16x16.png', QtCore.QSize(16,16))
app_icon.addFile(note_icons_file_path + 'notes24x24.png', QtCore.QSize(24,24))
app_icon.addFile(note_icons_file_path + 'notes32x32.png', QtCore.QSize(32,32))
app_icon.addFile(note_icons_file_path + 'notes48x48.png', QtCore.QSize(48,48))
app_icon.addFile(note_icons_file_path + 'notes256x256.png', QtCore.QSize(256,256))
fen.setWindowIcon(app_icon)
fen.resize(500,250)
fen.move(300,50)
fen.show()

layout = QVBoxLayout()
layout.setContentsMargins(0, 0, 0, 0)
# layout.setSpacing(0)
textArea = QTextEdit("")
textArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
textArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
layout.addWidget(textArea)
fen.setLayout(layout)

app.exec()