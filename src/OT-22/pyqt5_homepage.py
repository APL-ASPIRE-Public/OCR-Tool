import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel)
from tkinter import filedialog
from tkinter import *
import sys
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PIL import Image, ImageOps
from pdf2image import convert_from_path

class Window2(QMainWindow):                           
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OCR TOOL WITTER")
    
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.palette = self.palette()
        self.palette.setColor(QPalette.Window, QColor(230, 220, 255))
        self.setPalette(self.palette)

        select_button = QPushButton('Select a .JPG, .PNG, or .PDF file', self)
        select_button.move(275, 200)
        select_button.setGeometry(200,200,300,25)
        select_button.clicked.connect(self.on_click)

        selection_page_label = QLabel(self)
        selection_page_label.setText('Please select a usable file.')
        selection_page_label.setFont(QFont('Comic Sans MS',20))
        selection_page_label.move(225,170)
        selection_page_label.setGeometry(225,170,300,50)
        selection_page_label.setAlignment(Qt.AlignLeft)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose a File", "","JPEG Files (*.jpg);;PNG Files (*.png);;PDF Files (*.pdf)", options=options)
        if fileName:
            if fileName.endswith('.pdf'):
                pages = convert_from_path(fileName)
                for page in pages:
                    temp_file_path, _ = QFileDialog.getSaveFileName(self,'Save File as a JPG',r"H:/out","JPEG Files (*.jpg)")
                    page.save(temp_file_path)           
            im = Image.open(temp_file_path)
            im.show()
        else:
            print("Invalid file")

    #when clicking the select_button
, it opens a file selector prompt through pyqt
    def on_click(self):
        self.openFileNameDialog()
        

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "OCR-TOOL WITTER"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("Start", self)
        self.pushButton.move(275, 200)
        
        self.palette = self.palette()
        self.palette.setColor(QPalette.Window, QColor(230, 220, 255))
        self.setPalette(self.palette)

        self.pushButton.clicked.connect(self.window2)              

        self.main_window()

    def main_window(self):
        self.selection_page_label = QLabel("Welcome!", self)
        self.selection_page_label.move(290, 175)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def window2(self):                                            
        self.w = Window2()
        self.w.show()
        self.hide()

        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())