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

        ##Creates a color for the window
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

        ##Creates a small icon to the left of the button, could be used for a JHU logo?
        #button.setIcon(QIcon('/Users/wyattja1/Desktop/OCR-Tool/src/josh_models/Handwritten_Digits/digit_one.jpg'))
        #button.setIconSize(QSize(12, 12))

        #Removes border of button and makes it just text
        button.setFlat(True)

        #Drop shadow effect
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(1,1)
        
        #Slightly blurs the drop shadow
        effect.setBlurRadius(2)

        #Applies effect to button
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
    
root = Tk()
root.title('lol')
root.iconbitmap('c:/gui/codemy.ico')

#returns name and location of the file
root.filename = filedialog.askopenfile(initaldir = "/gui/images", title = "Select A File", filetypes = (("png files","*.png"),("all files","*.*"))                                   
