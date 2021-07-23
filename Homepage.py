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
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE,p1)


name=StringVar()
amount = 0

def ind_Bal():
    balance = 0
    
    try:    
        indData = db.child('registerUserExp').child(name.get()).get()
        for ind in indData.each():
            balance += int(ind.val()['amount'])
    except:
        balance = 0
        tkinter.messagebox.showinfo("Search Mismatch", "No such Name in Directory!!")

    
    print(name.get() + str(balance))
    return balance

def loaninfor():
    loanAmt = 0

    try:
        loanDatas = db.child('loanData').get()
        for ld in loanDatas.each():
            if ld.val()['name'] == name.get():
                loanAmt += int(ld.val()['principalLeft'])

    except:
        loanAmt = 0
        tkinter.messagebox.showinfo("Search Mismatch", "No such Name in Directory!!")

    return loanAmt

def treasure():
    global amount
    interest = 0
    princi = 0
    totalDB = db.child('mainData').get()
    loanDb = db.child('loanData').get()
    for data in totalDB.each():
        amount += int(data.val()['amount'])

    print(amount)
    for ld in loanDb.each():
        interest += int(ld.val()['interestPaidTillDate'])
    amount += interest
    print(amount)
    for ld in loanDb.each():
        princi += int(ld.val()['principalLeft'])

    amount -= princi 
    print(amount)
    # print(amount)
    return amount

def AccountsPage():
    root.destroy()
    import Accounts

def LoanWindow():
    root.destroy()
    import Loan_HomePage


def Time():
    string = strftime('%I:%M:%S %p')
    Time_Label.config(text=string)
    Time_Label.after(1000, Time)


Time_Label = Label(root, fg="black", bg="gold",
                   font="Devanagari 12 bold", borderwidth=4, relief=SUNKEN)
Time_Label.place(x=444, y=38)
Time()


def search():
    balance=Label(root,fg='gold',bg='midnight blue',width= 20,font="Devanagari 15 bold",text="Balance:  " + str(ind_Bal()))
    balance.place(x=15,y=174)
    Loan=Label(root,fg='gold',bg='midnight blue',width= 30, font="Devanagari 15 bold",text="Loan\nRemaining:  " + str(loaninfor()))
    Loan.place(x=240,y=174)


date = Label(root, text=f"{dt.datetime.now():%a, %b/%d/%Y}", bg="gold", fg="black", font=(
    "helvetica 12 bold"), borderwidth=4, relief=SUNKEN)
date.place(x=1, y=38)


top_Frame = Frame(root,bg="gold",borderwidth=4,relief=SUNKEN)
top_Frame.pack(fill=X)
top_label = Label(top_Frame,text="----HOMEPAGE----",bg="gold",fg="black",font="Helvetica 14 bold")
top_label.pack()

customer = Label(root,text="Customer Name:",font="Helvetica 13 bold",bg='midnight blue',fg='gold')
customer.place(x=50,y=120)
customer_name=Entry(root,justify=CENTER,borderwidth=4,textvariable=name,font="Helvetica 10 bold",width=25)
customer_name.place(x=190,y=120)

Check=Button(root,text="Search",bg='gold',font="Helvetica 12 bold",borderwidth=2,relief=SUNKEN,command=search,width=10)
Check.place(x=385,y=116)

accIcon = PhotoImage(master= root,file = "acc.png")
loanIcon = PhotoImage(master= root,file = "loan.png")

accounts=Button(root,image = accIcon,bg='gold',font="Helvetica 11 bold",borderwidth=4,relief=SUNKEN, command= AccountsPage)
accounts.place(x=160,y=240)
loan=Button(root,image = loanIcon,bg='gold',font="Helvetica 11 bold",borderwidth=4,relief=SUNKEN, command= LoanWindow)
loan.place(x=300,y=240)

accLab = Label(root,text="Accounts",font="Helvetica 10 bold",bg='midnight blue',fg='gold')
accLab.place(x=180,y=330)

loanLab = Label(root,text="Loans",font="Helvetica 10 bold",bg='midnight blue',fg='gold')
loanLab.place(x=320,y=330)

Treasury=Label(root,bg='gold',fg='black',font="Helvetica 13 bold",text="Treasury: Rs. "+ str(treasure()))
Treasury.place(x=200,y=380)

root.mainloop()
