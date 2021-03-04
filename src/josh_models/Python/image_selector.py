from tkinter import filedialog
from tkinter import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    #initilized variables
    def __init__(self):
        super().__init__()
        #set bar title
        self.title = 'OCR-Tool - "WITTER"'
        #set dimensions
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 300
        #initializes the UI
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Select a .JPG file', self)
        button.setToolTip('This is used to select files!')
        button.move(100,100)
        button.clicked.connect(self.on_click)
        
        self.show()

    @pyqtSlot()
    #when clicking the button, it opens a file selector prompt through tkinter
    def on_click(self):
        root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print(root.filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())