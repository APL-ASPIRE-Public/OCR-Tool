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
from tensorflow import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def load_image(filename):
    	# load the image
	img = load_img(filename, color_mode="grayscale", target_size=(28, 28))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 1 channel
	img = img.reshape(1, 28, 28, 1)
	# prepare pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img

#working on making a way to select the model so this isnt a direct file open, may take a bit
model = keras.models.load_model('/Users/jwdevelops/Desktop/OCR-Tool/src/saved_cnn_models/new_model.h5')

#image prediction function
def predict_digit(image):
    # loads the image through the above function
    img = load_image(image)
    #predicts digit from the image as an interger
    prediction = np.argmax(model.predict(img), axis=-1).astype("int32")
    # print
    print("Predicted number: ",prediction)

class Window2(QMainWindow):                           
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OCR TOOL WITTER")
    
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #set the background color of the page
        self.palette = self.palette()
        self.palette.setColor(QPalette.Window, QColor(230, 220, 255))
        self.setPalette(self.palette)

        #create buttons for turning a pdf into an image and predicting numbers
        select_button = QPushButton('Select a .JPG, .PNG, or .PDF file', self)
        select_button.setGeometry(200,200,300,25)
        select_button.move(200, 200)
        select_button.setStyleSheet("color: black; background: white")
        select_button.clicked.connect(self.open_filename_dialog)

        predict_button = QPushButton('Predict the Numbers of a .JPG,or .PNG file', self)
        predict_button.setGeometry(200,200,350,25)
        predict_button.move(175, 230)
        predict_button.setStyleSheet("color: black; background: white")
        predict_button.clicked.connect(self.predict_dialog)

        #Drop shadow effect
        select_effect = QGraphicsDropShadowEffect()
        select_effect.setOffset(1,1)

        predict_effect = QGraphicsDropShadowEffect()
        predict_effect.setOffset(1,1)
        
        #Slightly blurs the drop shadow
        select_effect.setBlurRadius(2)
        predict_effect.setBlurRadius(2)

        #Applies effect to button
        select_button.setGraphicsEffect(select_effect)
        predict_button.setGraphicsEffect(predict_effect)

        #label for second page
        selection_page_label = QLabel(self)
        selection_page_label.setText('Please select a usable file.')
        selection_page_label.setFont(QFont('Comic Sans MS',20))
        selection_page_label.setStyleSheet("color: black")
        selection_page_label.setGeometry(225,170,300,50)
        selection_page_label.move(225,150)

    #function to select image, turns pdf's to images
    def open_filename_dialog(self):
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
            print("Invalid file or no file selected.")

    #function to predict based on images
    def predict_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose a File", "","JPEG Files (*.jpg);;PNG Files (*.png)", options=options)
        if fileName:
            predict_digit(fileName)
        else:
            print("Invalid file or no file selected.")


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
        self.pushButton.setStyleSheet("color: black; background: white")

        #Drop shadow effect
        push_effect = QGraphicsDropShadowEffect()
        push_effect.setOffset(1,1)
        
        #Slightly blurs the drop shadow
        push_effect.setBlurRadius(2)

        #Applies effect to button
        self.pushButton.setGraphicsEffect(push_effect)

        
        self.palette = self.palette()
        self.palette.setColor(QPalette.Window, QColor(230, 220, 255))
        self.setPalette(self.palette)

        self.pushButton.clicked.connect(self.window2)              

        self.main_window()

    def main_window(self):
        self.selection_page_label = QLabel("Welcome!", self)
        self.selection_page_label.move(280, 165)
        self.selection_page_label.setStyleSheet("color: black")
        self.selection_page_label.setFont(QFont('Comic Sans MS',20))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def window2(self):                                            
        self.w = Window2()
        self.w.show()
        self.hide()

        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    app.setStyle("Fusion")
    window = Window()
    sys.exit(app.exec())