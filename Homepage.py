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
from PIL.ImageTk import PhotoImage
from envVar import firebaseConfig as fc
import threading
import concurrent.futures

firebase=pyrebase.initialize_app(fc)
db= firebase.database()


root = Tk()
root.geometry("1100x700+290+55")
root.config(bg="midnight blue")
root.title("HomePage")
root.minsize(1100,700)
root.maxsize(1100,700)
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
#root.iconphoto(False,p1)


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

    
    try:
        for ld in loanDb.each():
            interest += int(ld.val()['interestPaidTillDate'])
        amount += interest
        for ld in loanDb.each():
            princi += int(ld.val()['principalLeft'])
        amount -= princi

    except:
        pass

    return amount


def AccountsPage():
    import _thread
    _thread.start_new(accountsPage, (1,2))
def accountsPage(w,e):
    import Accounts
def loadtransfer():
    import _thread
    _thread.start_new(LoanWindow,(1,2))
def LoanWindow(l,s):
    import Loan_HomePage


def Time():
    string = strftime('%I:%M:%S %p')
    Time_Label.config(text=string)
    Time_Label.after(1000, Time)


Time_Label = Label(root, fg="black", bg="gold",
                   font="Devanagari 17 bold", borderwidth=4, relief=SUNKEN)
Time_Label.place(x=954, y=48)
Time()


def search():
    balance=Label(root,fg='gold',bg='midnight blue',width= 20,font="Devanagari 15 bold",text="Balance:  " + str(ind_Bal()))
    balance.place(x=15,y=174)
    Loan=Label(root,fg='gold',bg='midnight blue',width= 30, font="Devanagari 15 bold",text="Loan\nRemaining:  " + str(loaninfor()))
    Loan.place(x=240,y=174)


date = Label(root, text=f"{dt.datetime.now():%a, %b/%d/%Y}", bg="gold", fg="black", font=(
    "helvetica 17 bold"), borderwidth=4, relief=SUNKEN)
date.place(x=1, y=48)


top_Frame = Frame(root,bg="gold",borderwidth=4,relief=SUNKEN)
top_Frame.pack(fill=X)
top_label = Label(top_Frame,text="---------HOMEPAGE--------",bg="gold",fg="black",font="Helvetica 20 bold")
top_label.pack()

customer = Label(root,text="Customer Name:",font="Helvetica 20 bold",bg='midnight blue',fg='gold')
customer.place(x=230, y=180)
customer_name=Entry(root,justify=CENTER,borderwidth=4,textvariable=name,font="Helvetica 20 bold",width=25)
customer_name.place(x=500, y=180)

Check=Button(root,text="Search",bg='gold',font="Helvetica 17 bold",borderwidth=2,relief=SUNKEN,command=search,width=8)
Check.place(x=500,y=250)

accIcon = PhotoImage(master= root,file = "acc.png")
loanIcon = PhotoImage(master= root,file = "loan.png")

accounts=Button(root,image = accIcon,bg='gold',font="Helvetica 18 bold",borderwidth=4,relief=SUNKEN, command= AccountsPage)
accounts.place(x=400,y=330)
loan=Button(root,image = loanIcon,bg='gold',font="Helvetica 20 bold",borderwidth=4,relief=SUNKEN, command= loadtransfer)
loan.place(x=600,y=330)

accLab = Label(root,text="Accounts",font="Helvetica 17 bold", bg='midnight blue', fg='gold')
accLab.place(x=390,y=430)

loanLab = Label(root,text="Loans",font="Helvetica 17 bold", bg='midnight blue', fg='gold')
loanLab.place(x=610,y=430)

Treasury=Label(root,bg='gold',fg='black',font="Helvetica 18 bold",text="Treasury: Rs. "+ str(treasure()))
Treasury.place(x=440,y=500)

root.mainloop()
