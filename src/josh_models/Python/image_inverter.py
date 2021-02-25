from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageOps
#Needs user input

def image_opener(): 
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return root.filename

def invert():  
  im = image_opener()   
  im = Image.open(im)
  im_invert = ImageOps.invert(im)
  #outputs with a quality that is 95%
  root = Tk()
  root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
  im_invert.save(root.filename, quality=95)
invert()