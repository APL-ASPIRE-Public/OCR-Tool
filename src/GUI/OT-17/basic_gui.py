from tkinter import filedialog
from tkinter import *
import sys
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PIL import Image, ImageOps

class App(QWidget):
    #initilized variables
    def __init__(self):
        super().__init__()
        #set bar title
        self.title = 'OCR-Tool - "WITTER"'

        #self.palette = self.palette()
        #self.palette.setColor(QPalette.Window, QColor(185, 80, 225))
        #self.setPalette(self.palette)

        #set dimensions
        self.left = 10
        self.top = 10
        self.width = 450
        self.height = 300
        #initializes the UI
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Select a .JPG, .PNG, or .PDF file', self)
        button.move(100,100)
        button.clicked.connect(self.on_click)

        button.setIcon(QIcon('/Users/wyattja1/Downloads/website.jpg'))
        button.setIconSize(QSize(50, 50))

        button.setFlat(True)
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(1,1)
        effect.setBlurRadius(2)
        button.setGraphicsEffect(effect)
        self.show()

    @pyqtSlot()

    #when clicking the button, it opens a file selector prompt through tkinter
    def on_click(self):
        root = Tk()
        root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("pdf files","*.pdf")))
        Image.open(root.filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())