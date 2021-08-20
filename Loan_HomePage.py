from tkinter import *
from functools import partial
import pandas as pd
from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
import time
import tkinter.messagebox
import os
import pyrebase
import mysql.connector
import csv
from PIL.ImageTk import PhotoImage
from envVar import firebaseConfig as fc




firebase = pyrebase.initialize_app(fc)
db = firebase.database()


root = Tk()
root.geometry("1100x700+290+55")
root.minsize(1100,700)
root.maxsize(1100,700)
root.configure(bg='midnight blue')
root.title("Loan Window")
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE,p1)


name_entry = StringVar()
mob_entry = StringVar()

def back():
    root.destroy()
    import Homepage

def displayLoan():
    root.destroy()
    import LoanTreeView

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
             "InterestPaidTotal","Date","Last Paid Date" ])
        file.close()
    totalData = db.child('loanData').get()
    for data in totalData.each():
        
        if data.val()['name'] == name_entry.get() or data.val()['mobileNumber'] == (mob_entry.get()):
            with open('LoanFile.csv', 'a') as files:
                # print('Inside this')
                print(mob_entry.get())
                write = csv.writer(files)
                write.writerow([data.val()['name'], data.val()['principalAmount'], data.val()['interestPercent'],
                                data.val()['priciplePaid'], data.val()['principalLeft'], data.val()['interestPaid'],
                                data.val()['interestLeft'], data.val()['interestPaidTillDate'],data.val()['date'], data.val()['lastPaidDate']])
                files.close()
    os.system('LoanFile.csv')


def bal():
    balance = 0
    loanData = db.child('loanData').get()
    try:
        for loan in loanData.each():
            
            if loan.val()['name'] == name_entry.get() and loan.val()['mobileNumber'] == (mob_entry.get()):
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
    bal_lab = Label(root, bg='midnight blue', fg='gold', font="Helvetica 20 bold",
                    text="Balance:-" + " "+str(balance))
    bal_lab.place(x=142, y=468)
    download = Button(root, text="Download\n"
    "Balance Sheet", bg='gold', fg='black', font="Helvetica 19 bold",
                      borderwidth=4, relief=SUNKEN, command=export)
    download.place(x=510, y=445)


def sync_up():
    
    totalData = db.child('loanData').get()
    myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",database='ivsLoan')
    mycursor = myDataBase.cursor()
    mycursor.execute('Delete From loanEntry')
    for data in totalData.each():
        dataCollection = 'Insert into loanEntry (name ,mobileNumber ,address ,shopName ,date ,pricipalAmount ,interestPercent ,principlePaid ,interestPaid, principleLeft , interestLeft, InterestPaidTillDate,dateGiven) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        datas = [(data.val()['name'], data.val()['mobileNumber'], data.val()['address'],data.val()['shopName'],data.val()['date'], data.val()['principalAmount'], data.val()['interestPercent'], data.val()['priciplePaid'], data.val()['interestPaid'], data.val()['principalLeft'], data.val()['interestLeft'], data.val()['interestPaidTillDate'],data.val()['lastPaidDate'])]
        mycursor.executemany(dataCollection, datas)
        myDataBase.commit()
    tkinter.messagebox.showinfo('Success', 'Data Synced')
    myDataBase.close()


def sync_down():
    try:
        db.child('loanData').remove()
        myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivsLoan')
        mycursor = myDataBase.cursor()
        query = 'Select * from loanEntry'
        mycursor.execute(query)
        totalEntries = mycursor.fetchall()
        
        for rows in totalEntries:
            datas = {
                     'name':            rows[0], 'mobileNumber':    rows[1], 'address':               rows[2], 'shopName':     rows[3], 'date': rows[4],
                     'principalAmount': rows[5], 'interestPercent': rows[6], 'priciplePaid':          rows[7], 'interestPaid': rows[8],
                     'principalLeft':   rows[9], 'interestLeft':    rows[10], 'interestPaidTillDate': rows[11], 'lastPaidDate':rows[12]
                    }
            db.child('loanData').push(datas)
        tkinter.messagebox.showinfo('Success', 'Database Synced')
     
    except Exception as e:
        tkinter.messagebox.showerror('Error', e)


#---------------HEADING-------------------------------#
top_frame = Frame(root, bg='gold', borderwidth=10, relief=RAISED, width=500, height=55)
top_frame.pack(side=TOP, fill=X)
heading = Label(top_frame, bg='gold', fg='black', font="Arial 20 bold", text="--------Loan Window--------")
heading.pack()
#---------------------ENTRY STUFFS--------------------------#
name_lab = Label(root, bg='midnight blue', fg='gold', font="Helvetica 20 bold", text="Name:-")
name_lab.place(x=172, y=240)
name = Entry(root, width=27, textvariable=name_entry, borderwidth=5, relief=SUNKEN, font="Helvetica 20 bold")
name.place(x=290, y=240)
mob_lab = Label(root, bg='midnight blue', fg='gold', font="Helvetica 20 bold", text="Mobile No.:-")
mob_lab.place(x=110, y=310)
mob = Entry(root, width=27, textvariable=mob_entry,borderwidth=5, relief=SUNKEN, font="Helvetica 20 bold")
mob.place(x=290, y=310)

#----Buttons Frame along with Buttons---------#
btn_frame = Frame(root,bg='gold',width= 500,height=500,borderwidth=3,relief=RAISED)
btn_frame.place(x=840,y=170)
Check = Button(btn_frame, text="CHECK", bg='gold', font="Helvetica 19 bold",
               width=10,borderwidth=4, relief=RAISED, command=bal)
Check.pack()
Display = Button(btn_frame, text="DISPLAY", bg='gold', font="Helvetica 19 bold", borderwidth=4,
                 relief=RAISED, command=displayLoan,width=10)
Display.pack()
Back = Button(btn_frame, text="BACK", bg='gold', font="Helvetica 19 bold",
              borderwidth=4, relief=RAISED, command=back,width=10)
Back.pack()
Sync_Up = Button(btn_frame, text="SYNC UP", bg='gold', font="Helvetica 19 bold",
              borderwidth=4, relief=RAISED, command=sync_up,width=10)
Sync_Up.pack()
Sync_Down = Button(btn_frame, text="SYNC DOWN", bg='gold', font="Helvetica 18 bold",
              borderwidth=4, relief=RAISED, command=sync_down,width=10)
Sync_Down.pack()
newLoan = Button(btn_frame, text="NEW LOAN", bg='gold', fg='black', font="Helvetica 19 bold", borderwidth=4,
                     relief=RAISED, command=new,width=10)
newLoan.pack()
deposit = Button(btn_frame, text="DEPOSIT", bg='gold', fg='black', font="Helvetica 19 bold",
                     borderwidth=4, relief=RAISED, command=depo,width=10)
deposit.pack()
#---------------------------------------------------------------------------------------------#
root.mainloop()
