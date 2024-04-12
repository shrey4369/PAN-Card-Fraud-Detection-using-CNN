# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:37:36 2021

@author: sheet
"""

import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image  
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Pancard Fraud Detection")
#------------------Frame----------------------



#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "registration.py"])   



def login():
    from subprocess import call
    call(["python", "Login1.py"])   
    


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('img1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Pancard Fraud Detection", font=('times', 40,' bold '), height=1, width=50,bg="#DC143C",fg="white")
lbl.place(x=0, y=3)

framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="pink")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=500, y=250)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(framed, text='Login Now',command=login,width=15,height=2,bg='#8B0A50',fg='white',font='bold').place(x=30,y=65)
button1 = tk.Button(framed, text='Register',command=reg,width=15,height=2,bg='#EE9A00',fg='white',font='bold').place(x=250,y=65)


root.mainloop()
