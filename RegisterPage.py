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
from PIL.ImageTk import PhotoImage


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

root = Tk()
root.geometry("550x550")
root.maxsize(550, 550)
root.minsize(550, 550)
root.configure(bg='midnight blue')
root.title("Registration Page/IVS")
p1 = PhotoImage(file='C:\\Users\\ASUS\\Desktop\\[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE,p1)


def signUp(name,passwd,confirm):
    if (passwd==confirm):
        firebase = pyrebase.initialize_app(firebaseConfig)
        auth = firebase.auth()
        auth.create_user_with_email_and_password(name, passwd)
        tkinter.messagebox.showinfo('Success', "Register Successful")
    else:
        tkinter.messagebox.showerror('Error','The two passwords must be same!!')
        quit()


def New():
    signUp(user_entry.get(), pass_entry.get(),cpass_entry.get())
    root.destroy()
    import DataEntry
def back():
    root.destroy()
    import LoginPage


user_entry = StringVar()
pass_entry = StringVar()
cpass_entry = StringVar()

f1 = Frame(root, bg='gold', borderwidth=10, relief=RAISED, width=500, height=55)
f1.pack(side=TOP, fill=X)
l1 = Label(f1, text="Please Fill The Details Below", bg='gold', fg='black', font="Helvetica 12 bold").pack(fill=X)

l2 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="New Username:-")
l2.place(x=100, y=150)
l3 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="New Password :-")
l3.place(x=100, y=190)
l4 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Confirm Password :-")
l4.place(x=75, y=230)

username = Entry(root, width=30, textvariable=user_entry, borderwidth=8, relief=SUNKEN)
username.place(x=230, y=148)
password = Entry(root, width=30, textvariable=pass_entry, borderwidth=8, relief=SUNKEN)
password.place(x=230, y=188)
C_password = Entry(root, width=30, textvariable=cpass_entry, borderwidth=8, relief=SUNKEN)
C_password.place(x=230, y=228)

b1 = Button(root, text="Register", bg='gold', fg='black', font="Helvetica 11 bold", relief=SUNKEN,command=New)
b1.place(x=190, y=270)
b2 = Button(root, text="Quit", bg='gold', fg='black', font="Helvetica 11 bold", relief=SUNKEN,command=root.destroy)
b2.place(x=300, y=270)
b3 = Button(root, text="Back", bg='gold', fg='black', font="Helvetica 11 bold", relief=SUNKEN,command=back)
b3.place(x=2,y=45)

root.mainloop()
