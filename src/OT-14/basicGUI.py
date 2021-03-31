from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QVBoxLayout
import sys
def window2():
    app = QApplication(sys.argv)
    win1 = QMainWindow()
    win1.setGeometry(200, 200, 300, 300)
    win1.setWindowTitle("OCR WITTER TOOL")
    win1.show()
window2()
def clicked():
    window2()
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Basic GUI")
    
    label = QLabel('Hello World!')
    label.show()
    
    label2 = QLabel(win)
    label2.setText('Hey!')
    label2.move(50,50)
    
    button1 = QPushButton(win)
    button1.setText('Click!')
    button1.clicked.connect(clicked)
    
    
    win.show()
    
    window1 = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window1.setLayout(layout)
    
    
    window1.show()
    
    sys.exit(app.exec_())    
window()




