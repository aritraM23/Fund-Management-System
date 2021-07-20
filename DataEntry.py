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
import mysql.connector

firebaseConfig = {'apiKey': "AIzaSyDR-a5PGjXpXFjvJVS9Ep3FOKXnNy9BsZg",
    'authDomain': "fundmang-42ad8.firebaseapp.com",
    'projectId': "fundmang-42ad8",
    'storageBucket': "fundmang-42ad8.appspot.com",
    'messagingSenderId': "361815074904",
    'databaseURL':'https://fundmang-42ad8-default-rtdb.firebaseio.com',
    'appId': "1:361815074904:web:8504dfd52dbde0b186422d",
    'measurementId': "G-MVMXL8CJNK"
}

firebase=pyrebase.initialize_app(firebaseConfig)
db= firebase.database()


root=Tk()
root.geometry("500x450")
root.maxsize(500,450)
root.minsize(500,450)
root.configure(bg='midnight blue')
root.title("Registration Page")

f3 = Frame(root, bg='gold', borderwidth=10, relief=RAISED, width=500, height=55)
f3.pack(side=TOP, fill=X)
l8 = Label(f3, text="----Please Fill The Details Below----", bg='gold', fg='black', font="Helvetica 12 bold")
l8.pack(fill=X)
l9 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Shop Name:-")
l9.place(x=80, y=122)
l10 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Proprietor:-")
l10.place(x=88, y=162)
l11 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Address:-")
l11.place(x=103, y=202)
l12 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Mobile No.:-")
l12.place(x=86, y=242)

shop = StringVar()
pro = StringVar()
address = StringVar()
mob = StringVar()
shopname = Entry(root, width=30, textvariable=shop, borderwidth=8, relief=SUNKEN,font="Helvetica 10 bold")
shopname.place(x=190, y=118)
prop = Entry(root, width=30, textvariable=pro, borderwidth=8, relief=SUNKEN,font="Helvetica 10 bold")
prop.place(x=190, y=158)
add = Entry(root, width=30, textvariable=address, borderwidth=8, relief=SUNKEN,font="Helvetica 10 bold")
add.place(x=190, y=198)
mobile = Entry(root, width=30, textvariable=mob, borderwidth=8, relief=SUNKEN,font="Helvetica 10 bold")
mobile.place(x=190, y=238)

Reg_btn = Button(root,text="Register",bg="gold",fg="bLACK",borderwidth=2,relief=SUNKEN,font="Arial 12 bold")
Reg_btn.place(x=200,y=308)


root.mainloop()