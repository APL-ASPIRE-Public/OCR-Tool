from tkinter import*
from tkPDFViewer import tkPDFViewer as pdf

root = Tk ()
root.geometry("550x750")

v1 = pdf.ShowPdf()
v2 = v1.pdf_view(root,
                 pdf_location= r"/Users/singhs2/Desktop/sample-pdf-file.pdf",
                 width= 50, height= 100)
v2.pack()
root.mainloop()