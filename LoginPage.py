import csv
from functools import partial
import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os
from time import strftime
from datetime import datetime
import time
import pyrebase
from envVar import firebaseConfig as fc

from PIL.ImageTk import PhotoImage




firebase=pyrebase.initialize_app(fc)
db= firebase.database()

def signin(username,password):
    firebase = pyrebase.initialize_app(fc)
    auth = firebase.auth()
    name = username
    password = password
    auth.sign_in_with_email_and_password(name, password)
    print("Done")

def New():
    root.destroy()
    import RegisterPage

def Login():
    signin(user_entry.get(), pass_entry.get())
    root.destroy()
    import Homepage

root = Tk()
root.geometry("500x450")
root.maxsize(500,450)
root.minsize(500,450)
root.configure(bg='midnight blue')
root.title("Login/Register/IVS")
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE,p1)

    
user_entry = StringVar()
pass_entry = StringVar()
    
f1 = Frame(root,bg='gold',borderwidth=10,relief=RAISED,width=500,height=55)
f1.pack(side=TOP,fill =X)
l1 = Label(f1,text="---INVENTORY MANAGEMENT SYSTEM---",bg='gold',fg='black',font="Helvetica 12 bold").pack(fill=X)
    
l2 = Label(root,bg='midnight blue',fg='gold',font="Helvetica 11 bold",text="Username:-")
l2.place(x=100,y=150)
l3 = Label(root,bg='midnight blue',fg='gold',font="Helvetica 11 bold",text="Password :-")
l3.place(x=100,y=190)
    
username = Entry(root,width=30,textvariable=user_entry,borderwidth=4,relief=SUNKEN)
username.place(x=190,y=150)
password = Entry(root,width=30,textvariable=pass_entry,show="*",borderwidth=4,relief=SUNKEN)
password.place(x=190,y=190)

b1 = Button(root,text="Login",bg='gold',fg='black',font="Helvetica 11 bold",relief=SUNKEN,command=Login)
b1.place(x=220,y=230)
b2 = Button(root,text="New/Register Here",bg='gold',fg='black',font="Helvetica 10 bold",relief=SUNKEN,command=New)
b2.place(x=365,y=50)

root.mainloop()
