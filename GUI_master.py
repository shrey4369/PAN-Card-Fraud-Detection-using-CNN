import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 

##############################################+=============================================================

root = tk.Tk()
#root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
my_conn = sqlite3.connect('face.db')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Document  Summarization ")


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('img7.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

lbl = tk.Label(root, text="Pancard Fraud Detection", font=('times', 35,' bold '), height=1, width=55,bg="violet Red",fg="Black")
lbl.place(x=0, y=0)



  #################################################################################################################
def detection():
    #print("Registration")
    from subprocess import call
    call(["python", "GUI_Master_old.py"]) 




 



def window():
    root.destroy()


button1 = tk.Button(root, text="Pan Card Detection", command=detection,width=20, height=1, font=('times', 15, ' bold '),bg="brown",fg="white")
button1.place(x=200, y=410)




##
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=10, y=280)


exit = tk.Button(root, text="Exit", command=window, width=20, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=1000, y=410)



root.mainloop()