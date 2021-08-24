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

firebase = pyrebase.initialize_app(fc)
db = firebase.database()

def signin(username,password):
    firebase = pyrebase.initialize_app(fc)
    auth = firebase.auth()
    name = username
    password = password
    auth.sign_in_with_email_and_password(name, password)
    

def New():
    root.destroy()
    import RegisterPage

def Login():
    signin(user_entry.get(), pass_entry.get())
    root.destroy()
    import Homepage


root = Tk()
root.geometry("1100x700+290+55")
root.minsize(1100, 700)
root.maxsize(1100, 700)
root.configure(bg='navy')
root.title("Login/Register/IVS")
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE, p1)

    
user_entry = StringVar()
pass_entry = StringVar()
#----Heading------#
Heading = Frame(root, bg='DarkGoldenRod1', borderwidth=10, relief=RAISED, width=500, height=55)
Heading.pack(side=TOP, fill=X)
Title = Label(Heading, text="------INVENTORY MANAGEMENT SYSTEM------", bg='DarkGoldenRod1', fg='black', font="Helvetica 20 bold").pack(fill=X)

#---Main Content------#
main_frame = Frame(root, bg='DarkGoldenRod1', borderwidth=8, relief=SUNKEN, width=600, height=200)
main_frame.place(x=256, y=200)
userName = Label(main_frame, bg='DarkGoldenRod1', fg='black', font="Consolas 21 bold", text='Username:-')
userName.place(x=50, y=40)
userEntry = Entry(main_frame, fg='DarkGoldenRod1', font='Helvetica 20 bold', width=20, borderwidth=4, relief=RIDGE)
userEntry.place(x=230, y=40)
passWord = Label(main_frame, bg='DarkGoldenRod1', fg='black', font="Consolas 21 bold", text='Password:-')
passWord.place(x=50, y=100)
passEntry = Entry(main_frame, fg='DarkGoldenRod1', font='Helvetica 20 bold', width=20, borderwidth=4, relief=RIDGE)
passEntry.place(x=230, y=100)

login_frame = Frame(root, bg='DarkGoldenRod1', borderwidth=6, relief=SUNKEN, width=22, height=20)
login_frame.place(x=496, y=440)
login_btn = Button(login_frame, text='Login', borderwidth=4, relief=RIDGE, bg='navy', fg='DarkGoldenrod1', font="Consolas 20 bold", command=Login)
login_btn.pack()
newReg_frame = Frame(root, bg='DarkGoldenRod1', borderwidth=4, relief=SUNKEN, width=35, height=5)
newReg_frame.place(x=942, y=56)
newReg_btn = Button(newReg_frame, fg='DarkGoldenrod1', text='Register', borderwidth=5, relief=RIDGE,
                    bg='navy', font="Consolas 20 bold", command=New)
newReg_btn.pack()

root.mainloop()
