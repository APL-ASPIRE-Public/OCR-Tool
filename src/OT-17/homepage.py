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
        self.palette = self.palette()
        self.palette.setColor(QPalette.Window, QColor(230, 220, 255))
        self.setPalette(self.palette)

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
        label = QLabel(self)
        label.setText('Welcome to the OCR Tool "WITTER".')
        label.setFont(QFont('Comic Sans MS',20))
        label.move(60,30)
        label.setAlignment(Qt.AlignLeft)

        ##Creates a small icon to the left of the button, could be used for a JHU logo?
        #button.setIcon(QIcon('/Users/wyattja1/Desktop/OCR-Tool/src/josh_models/Handwritten_Digits/digit_one.jpg'))
        #button.setIconSize(QSize(12, 12))

        #Removes border of button and makes it just text
        #button.setFlat(True)

        #Drop shadow effect
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(1,1)
        
        #Slightly blurs the drop shadow
        effect.setBlurRadius(2)

        #Applies effect to button
        button.setGraphicsEffect(effect)
        self.show()

    @pyqtSlot()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose a File", "","JPEG Files (*.jpg);;PNG Files (*.png);;PDF Files (*,pdf)", options=options)
        if fileName:
            print(fileName)
            im = Image.open(fileName)
            im.show()
        else:
            print("Invalid file")

    #when clicking the button, it opens a file selector prompt through tkinter
    def on_click(self):
        self.openFileNameDialog()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()