from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
import datetime as dt
import mysql.connector
from time import time, sleep
from tkinter import *
from functools import partial
import pandas as pd
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
from envVar import mycursor,myDataBase



firebase = pyrebase.initialize_app(fc)
db = firebase.database()

root = Tk()
root.config(bg='navy')
root.state('zoomed')
root.resizable(0,0)
root.title("IVS/Loan/LoanDetails")
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE, p1)
#---------------------------Functions--------------------------------#
Name = StringVar()
Mobile = StringVar()
PrincipleTaken = StringVar()
PrincipleLeft = StringVar()
Interest = StringVar()
MonthlyInterest = StringVar()
PaidInterest = StringVar()
Date = StringVar()
def home():
    _thread.exit_thread()

def display():
            myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="Anik123#",
                                         database='ivsLoan')
            mycursor = myDataBase.cursor()
            mycursor.execute("select name,mobileNumber,date,pricipalAmount,interestPercent,principleLeft,interestLeft,InterestPaidTillDate, dateGiven from loanEntry")
            result = mycursor.fetchall()
            if len(result) != 0:
                tree_v.delete(*tree_v.get_children())
                for row in result:
                    tree_v.insert('', END, values=row)
            myDataBase.commit()
            myDataBase.close()

def do_press(ev):
    display()

def refresh():
    display()

def newloan():
    _thread.start_new(newL,(1,2))
def newL(j,k):
    import NewLoan

def repayloan():
    _thread.start_new(loanRepay,(1,2))
def loanRepay(j,k):
    import Loan_RepayPage

def sync_up():
    myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="Anik123#",
                                         database='ivsLoan')
    mycursor = myDataBase.cursor()
    totalData = db.child('loanData').get()
    mycursor.execute('Delete From loanEntry')
    for data in totalData.each():
        dataCollection = 'Insert into loanEntry (name ,mobileNumber ,address ,shopName ,date ,pricipalAmount ,interestPercent ,principlePaid ,interestPaid, principleLeft , interestLeft, InterestPaidTillDate,dateGiven) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        datas = [(data.val()['name'], data.val()['mobileNumber'], data.val()['address'],data.val()['shopName'],data.val()['date'], data.val()['principalAmount'], data.val()['interestPercent'], data.val()['priciplePaid'], data.val()['interestPaid'], data.val()['principalLeft'], data.val()['interestLeft'], data.val()['interestPaidTillDate'],data.val()['lastPaidDate'])]
        mycursor.executemany(dataCollection, datas)
        myDataBase.commit()
    tkinter.messagebox.showinfo('Success', 'Data Synced')
    myDataBase.close()
    display()


def sync_down():
    try:
        myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="Anik123#",
                                             database='ivsLoan')
        mycursor = myDataBase.cursor()
        db.child('loanData').remove()
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
        display()
    except Exception as e:
        tkinter.messagebox.showerror('Error', e)
        display()


# #-----------------------------------Heading Frame and Label---------------------------------#
Heading = Frame(root,bg='DarkGoldenRod1',borderwidth=4,relief=SUNKEN)
Heading.pack(fill=X)
Heading_Label = Label(Heading,text="--------LOAN DETAILS--------",font="Orbitron-Bold 32 bold",bg='DarkGoldenRod1',fg='black')
Heading_Label.pack()
#------------------------------------Time and Date Widgets----------------------------------#
def time_widget():
    string = strftime('%I:%M:%S %p')
    Time_Label.config(text=string)
    Time_Label.after(1000, time_widget)


timeFrame = Frame(root, bg='navy', borderwidth=5, relief=SUNKEN)
timeFrame.place(x=1355, y=66)
Time_Label = Label(timeFrame, fg="black", bg="DarkGoldenrod1",
                   font="Constantia 25 bold")
Time_Label.pack()
time_widget()


dateFrame = Frame(root, bg='DarkGoldenrod1', borderwidth=5, relief=SUNKEN)
dateFrame.place(x=2, y=66)
date = Label(dateFrame, text=f"{dt.datetime.now():%a, %b/%d/%Y}", fg="black", bg="DarkGoldenrod1", font=(
    "Constantia 25 bold"))
date.pack()
#-----------------------------------------Tree View------------------------------------------#
tv_Frame = Frame(root, width=640, height=500,borderwidth=7,relief=SUNKEN)
tv_Frame.place(x=105,y=200)

y_scroll = Scrollbar(tv_Frame, orient=VERTICAL)
x_scroll = Scrollbar(tv_Frame, orient=HORIZONTAL)
tree_v = ttk.Treeview(tv_Frame,height=25,selectmode="extended")
y_scroll.pack(side=RIGHT, fill=Y)
x_scroll.pack(side=BOTTOM, fill=X)
tree_v['columns'] = ("Name","Mobile No.","Date","Principal Taken","ROI","Priciple Left",
                     "Remaining Interest","Total Interest Paid","Last Day of payement")
#name,mobileNumber,date,pricipalAmount,interestPercent,principleLeft,interestLeft,InterestPaidTillDate
# ~TreeView Styling~
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font="Consolas 10 bold ",fieldbackground='DarkGoldenRod1')
style.configure("Treeview",fieldbackground="white")
style.map('Treeview',background=[('selected','DarkGoldenRod1')])
#~~~~~~~~~~~~~~~~~~~~#

tree_v.column('#0', width=0, stretch=NO)
tree_v.column('Name', anchor=CENTER, width=110)
tree_v.column('Mobile No.', anchor=CENTER, width=120)
tree_v.column('Date', anchor=CENTER, width=120)
tree_v.column('Principal Taken', anchor=CENTER, width=130)
tree_v.column('ROI', anchor=CENTER, width=78)
tree_v.column('Priciple Left', anchor=CENTER, width=115)
tree_v.column('Remaining Interest', anchor=CENTER, width=100)
tree_v.column('Total Interest Paid', anchor=CENTER, width=125)
tree_v.column('Last Day of payement', anchor=CENTER, width=120)

tree_v.heading('#0', anchor=CENTER,text='')
tree_v.heading('Name', anchor=CENTER, text="Name")
tree_v.heading('Mobile No.', anchor=CENTER, text="Mobile No.")
tree_v.heading('Date', anchor=CENTER, text="Date")
tree_v.heading('Principal Taken', anchor=CENTER, text="Principal Taken")
tree_v.heading('ROI', anchor=CENTER, text="ROI")
tree_v.heading('Priciple Left', anchor=CENTER, text="Principle Left")
tree_v.heading('Remaining Interest', anchor=CENTER, text="Remaining Interest")
tree_v.heading('Total Interest Paid', anchor=CENTER, text="Total Interest Paid")
tree_v.heading('Last Day of payement', anchor=CENTER, text="Last Day of Payment")

tree_v.pack(fill=X)

# while True:
#     sleep(60 - time() % 60)
tree_v.bind('<ButtonRelease-1>')
# display()
#-----------------------------Footer Frame& buttons-----------------------------------#
btn_frame = Frame(root, borderwidth=5, relief=SUNKEN, bg='black',width=250, height=600)
btn_frame.place(x=1250, y=250)
refBtn = Button(btn_frame, text='Refresh', width=9, font="Orbitron-Bold 25 bold", borderwidth=5,
                   relief=SUNKEN, bg='DarkGoldenrod1', command=refresh)
refBtn.pack()
syncupBtn = Button(btn_frame, text='Sync Up', width=9, font="Orbitron-Bold 25 bold", borderwidth=5,
                   relief=SUNKEN, bg='DarkGoldenrod1', command=sync_up)
syncupBtn.pack()
syncdwnBtn = Button(btn_frame, text='Sync Down', width=9, font="Orbitron-Bold 25 bold", borderwidth=5,
                   relief=SUNKEN, bg='DarkGoldenrod1', command=sync_down)
syncdwnBtn.pack()
newBtn = Button(btn_frame, text='New', width=9, font="Orbitron-Bold 25 bold", borderwidth=5,
                   relief=SUNKEN, bg='DarkGoldenrod1', command=newloan)
newBtn.pack()
updtBtn = Button(btn_frame, text='Update', width=9, font="Orbitron-Bold 25 bold", borderwidth=5,
                   relief=SUNKEN, bg='DarkGoldenrod1', command=repayloan)
updtBtn.pack()
homeBtn = Button(btn_frame, text='Homepage', width=9, font="Orbitron-Bold 25 bold", borderwidth=5,
                   relief=SUNKEN, bg='DarkGoldenrod1', command=home)
homeBtn.pack()


root.mainloop()
