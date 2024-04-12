# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 01:01:37 2021

@author: MADHVI
"""





from tkinter import *
from tkinter import messagebox as ms
from PIL import ImageTk 
import sqlite3

class login_system:
    def __init__(self,root):
        self.root = root
        self.root.title("log in ")
        self.root.geometry("1350x700+0+0")
        
        ##______________________All Images ___________________________##
       
    #=====Variable======#
        
    # Some Usefull variables
    # Create Widgets
        
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        
        self.bg1_icon=ImageTk.PhotoImage(file=r"img2.jpg")

        self.bg_icon=ImageTk.PhotoImage(file=r"L.jpg")
        self.user_icon=ImageTk.PhotoImage(file=r"L.jpg")
        self.pass_icon=ImageTk.PhotoImage(file=r"p1.jpg")
        
        bg_lbl=Label(self.root,image=self.bg1_icon).pack()
        
        title=Label(self.root, text="LOG IN", font=("Times new roman", 40, "bold"), bg="skyblue",fg="red",bd=5,relief=RAISED)
        title.place(x=0, y=0,relwidth=1)
        
        Login_frame=Frame(self.root,bg="white")
        Login_frame.place(x=400,y=150)
        
        logolbl=Label(Login_frame,image=self.bg_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        
        lbluser=Label(Login_frame,text="Username",image=self.user_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_frame,bd=5,textvariable=self.username ,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        
        lblpass=Label(Login_frame,text="Password",image=self.pass_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_frame,bd=5,textvariable=self.password,relief=GROOVE,font=("",15),show='*').grid(row=2,column=1,padx=20)
        
        btn_log=Button(Login_frame,text="Login",command=self.login,width=15,font=("Times new roman", 14, "bold"),bg="skyblue",fg="red").grid(row=3,column=1,pady=10)
        
        
    
       
        # Login Function
    def login(self):
        # Establish Connection

        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        db = sqlite3.connect('evaluation.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                       "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
        db.commit()
        find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(self.username.get()), (self.password.get())])
        result = c.fetchall()

        if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            root.destroy()

            from subprocess import call
            call(['python','GUI_Master_old.py'])

            # ================================================
        else:
            ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created Successfully !')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

        # Frame Packing Methords

    def registration(self):
        root.destroy()
        from subprocess import call
        call(["python", "registration.py"])

        # mainloop(root)

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    

        
    # def login(self):
        
    #     if self.uname.get()=="" or self.pass_.get()=="":
    #        ms.showerror("Error","All Fields are required!!")

    #     else:
    #         ms.showerror("Successfull","Invalid Username or Password") 
                
        
       
        
        
root = Tk()
obj = login_system(root)
root.mainloop()