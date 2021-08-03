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


firebaseConfig = {
                  'apiKey': "AIzaSyDR-a5PGjXpXFjvJVS9Ep3FOKXnNy9BsZg",
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
root.config(bg='midnight blue')
root.geometry("1100x700+290+55")
root.minsize(1100,700)
root.maxsize(1100,700)
root.title("IVS/Loan/LoanDetails")
p1 = PhotoImage(file='C:\\Users\\ASUS\\Desktop\\[DIGICURE MAIN LOGO].png')
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
    root.destroy()
    import Homepage

def display():
            myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivsLoan')
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
    root.destroy()
    import NewLoan

def repayloan():
    root.destroy()
    import Loan_RepayPage

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
    display()


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
        display()
    except Exception as e:
        tkinter.messagebox.showerror('Error', e)
        display()



#-----------------------------------Heading Frame and Label---------------------------------#
Heading = Frame(root,bg='gold',borderwidth=4,relief=SUNKEN)
Heading.pack(fill=X)
Heading_Label = Label(Heading,text="------------LOAN DETAILS------------",font="Helvetica 18 bold",bg='gold',fg='black')
Heading_Label.pack()
#------------------------------------Time and Date Widgets----------------------------------#
def time_widget():
    string = strftime('%I:%M:%S %p')
    Time_Label.config(text=string)
    Time_Label.after(1000, time_widget)


Time_Label = Label(root, fg="gold", bg="midnight blue",
                   font="Helvetica 17 bold")
Time_Label.place(x=955, y=48)
time_widget()


date = Label(root, text=f"{dt.datetime.now():%A, %b/%d/%Y}", fg="gold", bg="midnight blue", font=(
    "Helvetica 15 underline"))
date.place(x=1, y=50)
#-----------------------------------------Tree View------------------------------------------#
tv_Frame = Frame(root, width=240, height=500,borderwidth=6,relief=SUNKEN)
tv_Frame.place(x=55,y=100)

y_scroll = Scrollbar(tv_Frame, orient=VERTICAL)
x_scroll = Scrollbar(tv_Frame, orient=VERTICAL)
tree_v = ttk.Treeview(tv_Frame,height=25,selectmode="extended")
y_scroll.pack(side=RIGHT, fill=Y)
x_scroll.pack(side=BOTTOM, fill=X)
tree_v['columns'] = ("Name","Mobile No.","Date","Principal Taken","ROI","Priciple Left",
                     "Remaining Interest","Total Interest Paid","Last Day of payement")
#name,mobileNumber,date,pricipalAmount,interestPercent,principleLeft,interestLeft,InterestPaidTillDate
# ~TreeView Styling~
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font="Consolas 10 bold ",fieldbackground='gold')
style.configure("Treeview",fieldbackground="gold")
style.map('Treeview',background=[('selected','white')])
#~~~~~~~~~~~~~~~~~~~~#

tree_v.column('#0', width=0, stretch=NO)
tree_v.column('Name', anchor=CENTER, width=110)
tree_v.column('Mobile No.', anchor=CENTER, width=110)
tree_v.column('Date', anchor=CENTER, width=120)
tree_v.column('Principal Taken', anchor=CENTER, width=110)
tree_v.column('ROI', anchor=CENTER, width=78)
tree_v.column('Priciple Left', anchor=CENTER, width=125)
tree_v.column('Remaining Interest', anchor=CENTER, width=100)
tree_v.column('Total Interest Paid', anchor=CENTER, width=90)
tree_v.column('Last Day of payement', anchor=CENTER, width=120)

tree_v.heading('#0', anchor=CENTER,text='')
tree_v.heading('Name', anchor=CENTER, text="Name")
tree_v.heading('Mobile No.', anchor=CENTER, text="Mobile No.")
tree_v.heading('Date', anchor=CENTER, text="Date")
tree_v.heading('Principal Taken', anchor=CENTER, text="Principal Taken")
tree_v.heading('ROI', anchor=CENTER, text="ROI")
tree_v.heading('Priciple Left', anchor=CENTER, text="Priciple Left")
tree_v.heading('Remaining Interest', anchor=CENTER, text="Remaining Interest")
tree_v.heading('Total Interest Paid', anchor=CENTER, text="Total Interest Paid")
tree_v.heading('Last Day of payement', anchor=CENTER, text="Last Day of Payment")

tree_v.pack(fill=X)

# while True:
#     sleep(60 - time() % 60)
tree_v.bind('<ButtonRelease-1>',do_press)
display()
#-----------------------------Footer Frame& buttons-----------------------------------#
footer = Frame(root,borderwidth=4,relief=RAISED)
footer.pack(side=BOTTOM,fill=X)
btn_syncup = Button(footer,text="Sync Up",font="Helvetica 12 bold",bg="gold", command= sync_up)
btn_syncup.pack(side=LEFT,padx=40)
btn_syncdown = Button(footer,text="Sync Down",font="Helvetica 12 bold",bg="gold", command = sync_down)
btn_syncdown.pack(side=RIGHT,padx=40)
btn_new = Button(footer,text="New",font="Helvetica 12 bold",bg="gold", command= newloan)
btn_new.pack(side=LEFT,padx= 135)
btn_update = Button(footer,text="Update",font="Helvetica 12 bold",bg="gold", command = repayloan)
btn_update.pack(side=RIGHT,padx=135)

btn_back = Button(root,text="HOMEPAGE",font="Helvetica 12 bold",bg="gold",command=home)
btn_back.place(x=550,y=55)
ref_btn = Button(root,text="REFRESH",font="Helvetica 12 bold",bg="gold", command= refresh)
ref_btn.place(x=435,y=55)

root.mainloop()
