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
import datetime as dt

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
root.geometry("550x450+600+90")
root.config(bg="midnight blue")
root.title("HomePage")
root.maxsize(550,450)
root.minsize(550,450)

name=StringVar()
amount = 0


def ind_Bal():
    balance = 0
    indData = db.child('registerUserExp').child(name.get()).get()
    for ind in indData.each():
        balance += int(ind.val()['amount'])

    print(name.get() + str(balance))
    return balance

def treasure():
    global amount
    totalDB = db.child('mainData').get()
    for data in totalDB.each():
        amount += int(data.val()['amount'])

    # print(amount)
    return amount

    

def Time():
    string = strftime('%H:%M:%S %p')
    Time_Label.config(text=string)
    Time_Label.after(1000, Time)


Time_Label = Label(root, fg="black", bg="gold",
                   font="Devanagari 15 bold", borderwidth=4, relief=SUNKEN)
Time_Label.place(x=426, y=2)
Time()

def srch():
    balance=Label(root,fg='gold',bg='midnight blue',font="Devanagari 15 bold",text="Balance:- " + str(ind_Bal()))
    balance.place(x=100,y=175)
    Loan=Label(root,fg='gold',bg='midnight blue',font="Devanagari 15 bold",text="Loan:-")
    Loan.place(x=320,y=175)

date = Label(root, text=f"{dt.datetime.now():%a, %b/%d/%Y}", bg="gold", fg="black", font=(
    "helvetica 15 bold"), borderwidth=4, relief=SUNKEN)
date.place(x=1, y=2)


name.set("Enter Customer Name Here")
customer_name=Entry(root,justify=CENTER,borderwidth=4,textvariable=name,font="Helvetica 12 bold",width=30)
customer_name.place(x=140,y=80)

Check=Button(root,text="Search",bg='gold',font="Helvetica 11 bold",borderwidth=4,relief=RAISED,command=srch)
Check.place(x=353,y=125)

accIcon = PhotoImage(master= root,file = "acc.png")
loanIcon = PhotoImage(master= root,file = "loan.png")

accounts=Button(root,image = accIcon,bg='gold',font="Helvetica 11 bold",borderwidth=4,relief=SUNKEN)
accounts.place(x=180,y=240)
loan=Button(root,image = loanIcon,bg='gold',font="Helvetica 11 bold",borderwidth=4,relief=SUNKEN)
loan.place(x=320,y=240)

Treasury=Label(root,bg='gold',fg='black',font="Helvetica 13 bold",text="Treasury:- " + str(treasure()))
Treasury.place(x=70,y=350)

root.mainloop()
