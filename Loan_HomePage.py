from tkinter import *
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
import csv

firebaseConfig = {'apiKey': "AIzaSyDR-a5PGjXpXFjvJVS9Ep3FOKXnNy9BsZg",
                  'authDomain': "fundmang-42ad8.firebaseapp.com",
                  'projectId': "fundmang-42ad8",
                  'storageBucket': "fundmang-42ad8.appspot.com",
                  'messagingSenderId': "361815074904",
                  'databaseURL': 'https://fundmang-42ad8-default-rtdb.firebaseio.com',
                  'appId': "1:361815074904:web:8504dfd52dbde0b186422d",
                  'measurementId': "G-MVMXL8CJNK"
                  }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

root = Tk()
root.geometry("550x500+600+90")
root.maxsize(550, 500)
root.minsize(550, 500)
root.configure(bg='midnight blue')
root.title("Loan Window")
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE,p1)

name_entry = StringVar()
mob_entry = StringVar()


def new():
    root.destroy()
    import NewLoan


def depo():
    root.destroy()
    import Loan_RepayPage


def export():
    with open('LoanFile.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(
            ["Name", "Loan Amount", "Interest", "Principal Paid", "Interest Paid", "Principal left", "Interest left",
             "Date"])
        file.close()
    totalData = db.child('loanDemo').get()
    for data in totalData.each():

        if data.val()['Name'] == name_entry.get() or data.val()['Phone'] == int(mob_entry.get()):
            with open('LoanFile.csv', 'a') as files:
                # print('Inside this')
                print(mob_entry.get())
                write = csv.writer(files)
                write.writerow([data.val()['Name'], data.val()['Amount'], data.val()['ROI'], data.val()['ppaid'],
                                data.val()['pleft'], data.val()['ipaid'], data.val()['ileft'], data.val()['Date']])
                files.close()
    os.system('LoanFile.csv')


def bal():
    balance = 0
    loanData = db.child('loanDemo').get()
    try:
        for loan in loanData.each():

            if loan.val()['Name'] == name_entry.get() and loan.val()['Phone'] == (mob_entry.get()):
                print(f'{name_entry.get()} entered if')
                balData = db.child('mainData').get()
                for var in balData.each():
                    if var.val()['name'] == name_entry.get():
                        balance += int(var.val()['amount'])
                    else:
                        balance += 0
                break
    except:
        tkinter.messagebox.showinfo("Search Mismatch", "No such Name in Directory!!")

    bal_lab = Label(root, bg='midnight blue', fg='gold', width=30,
                    font="Helvetica 12 bold", text="Balance:" + str(balance))
    bal_lab.place(x=10, y=248)
    download = Button(root, text="Download\nBalance Sheet", bg='gold', fg='black',
                      font="Helvetica 11 bold", borderwidth=2, relief=SUNKEN, command=export)
    download.place(x=310, y=235)
    newLoan = Button(root, text="New Loan", bg='gold', fg='black',
                     font="Helvetica 11 bold", borderwidth=2, relief=SUNKEN, command=new)
    newLoan.place(x=120, y=325)
    deposit = Button(root, text="Deposit on Existing Loan", bg='gold', fg='black',
                     font="Helvetica 11 bold", borderwidth=2, relief=SUNKEN, command=depo)
    deposit.place(x=270, y=325)


top_frame = Frame(root, bg='gold', borderwidth=10,
                  relief=RAISED, width=500, height=55)
top_frame.pack(side=TOP, fill=X)

heading = Label(top_frame, bg='gold', fg='black', font="Arial 12 bold", text="---Loan Window---")
heading.pack()

name_lab = Label(root, bg='midnight blue', fg='gold',
                 font="Helvetica 12 bold", text="Name:-")
name_lab.place(x=120, y=100)

name = Entry(root, width=27, textvariable=name_entry,
             borderwidth=5, relief=SUNKEN, font="Helvetica 11 bold")
name.place(x=200, y=98)

mob_lab = Label(root, bg='midnight blue', fg='gold',
                font="Helvetica 12 bold", text="Mobile No.:-")
mob_lab.place(x=90, y=140)

mob = Entry(root, width=27, textvariable=mob_entry,
            borderwidth=5, relief=SUNKEN, font="Helvetica 11 bold")
mob.place(x=200, y=138)

Check = Button(root, text="Check", bg='gold', font="Helvetica 11 bold", borderwidth=4, relief=RAISED, command=bal)
Check.place(x=245, y=185)

down_Frame = Frame(root, bg='gold', borderwidth=10,
                  relief=RAISED)
down_Frame.pack(side=BOTTOM,fill=X)
SyncD_button = Button(down_Frame,text="Sync Down",font="Helvetica 12 bold",bg='midnight blue',fg='gold')
SyncD_button.pack(side=LEFT,padx=100)
SyncU_button = Button(down_Frame,text="Sync Up",font="Helvetica 12 bold",bg='midnight blue',fg='gold')
SyncU_button.pack(side=LEFT,padx=10)


root.mainloop()
