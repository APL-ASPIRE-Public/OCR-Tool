# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog
import sys
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PIL import Image, ImageOps
  
# creates a Tk() object
master = Tk()
  
# sets the size of main video
master.geometry("800x800")

  
# def of function to open a new window
def openNewWindow():
      
    # Toplevel object which acts as window
    newWindow = Toplevel(master)
  
    # sets the title
    newWindow.title("OCT-TOOL WITTER")
  
    # sets the size of window
    newWindow.geometry("400x400")
    
    
    # labels
    Label(newWindow, 
        text ="This is a new window").pack()
    Label(newWindow, 
        text ="First upload a file (JPG, PNG, PDF").pack()
    
    
  
label = Label(master, 
    text ="Welcome to the OCR Tool WITTER!!")
  
label.pack(pady = 10)


# a button widget
btn = Button(master, 
    text ="Get Started!", 
    command = openNewWindow)
btn.pack(pady = 10)

  
# mainloop which runs infinitely
mainloop()
  