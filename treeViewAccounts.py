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

# #-----------------------------------Heading Frame and Label---------------------------------#
Heading = Frame(root,bg='DarkGoldenrod1',borderwidth=5,relief=SUNKEN)
Heading.pack(fill=X)
Heading_Label = Label(Heading,text="---------ACCOUNT DETAILS---------",font="Orbitron-Bold 32 bold", bg='DarkGoldenrod1',fg='black')
Heading_Label.pack()
#------------------------------------Time and Date Widgets----------------------------------#
def time_widget():
    string = strftime('%I:%M:%S %p')
    Time_Label.config(text=string)
    Time_Label.after(1000, time_widget)


timeFrame = Frame(root, bg='black', borderwidth=4, relief=SUNKEN)
timeFrame.place(x=1352, y=70)
Time_Label = Label(timeFrame, fg="black", bg="DarkGoldenrod1",
                   font="Constantia 26 bold")
Time_Label.pack()
time_widget()


dateFrame = Frame(root, bg='DarkGoldenrod1',borderwidth=4, relief=SUNKEN)
dateFrame.place(x=2, y=70)
date = Label(dateFrame, text=f"{dt.datetime.now():%a, %b/%d/%Y}", fg="black", bg="DarkGoldenrod1",
    font="Constantia 26 bold")
date.pack()
#-----------------------------------------Tree View------------------------------------------#
tv_Frame = Frame(root, width=640, height=480,borderwidth=6,relief=SUNKEN)
tv_Frame.place(x=230, y=150)

y_scroll = Scrollbar(tv_Frame, orient=VERTICAL)
x_scroll = Scrollbar(tv_Frame, orient=HORIZONTAL)
tree_v = ttk.Treeview(tv_Frame,height=28,selectmode="extended")
y_scroll.pack(side=RIGHT, fill=Y)
x_scroll.pack(side=BOTTOM, fill=X)
tree_v['columns'] = ("Name","Date","Amount","Total Amount","Loan Taken")
#name,mobileNumber,date,pricipalAmount,interestPercent,principleLeft,interestLeft,InterestPaidTillDate
# ~TreeView Styling~
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font="Orbitron-Bold 15 bold ",fieldbackground='hotDarkGoldenrod1')
style.configure("Treeview",fieldbackground="white")
style.map('Treeview',background=[('selected','DarkGoldenrod1')])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

tree_v.column('#0', width=0, stretch=NO)
tree_v.column('Name', anchor=CENTER, width=150)
tree_v.column('Date', anchor=CENTER, width=140)
tree_v.column('Amount', anchor=CENTER, width=150)
tree_v.column('Total Amount', anchor=CENTER, width=178)
tree_v.column('Loan Taken', anchor=CENTER, width=175)

tree_v.heading('#0', anchor=CENTER,text='')
tree_v.heading('Name', anchor=CENTER, text="Name")
tree_v.heading('Date', anchor=CENTER, text="Date")
tree_v.heading('Amount', anchor=CENTER, text="Amount")
tree_v.heading('Total Amount', anchor=CENTER, text="Total Amount")
tree_v.heading('Loan Taken', anchor=CENTER, text="Loan Taken")

tree_v.pack(fill=X)

# while True:
#     sleep(60 - time() % 60)
tree_v.bind('<ButtonRelease-1>')
# display()
#------------Buttons-------------#
btn_Frame = Frame(root,bg='DarkGoldenrod1',height = 520,width =280,borderwidth=4,relief=SUNKEN)
btn_Frame.place(x=1057,y=190)
sync_up = Button(btn_Frame,text='Sync Up',font="Orbitron-Bold 25 bold",borderwidth=4,relief=RAISED,
                 height=0,width=9,bg='navy', fg='white')
sync_down = Button(btn_Frame,text='Sync Down',font="Orbitron-Bold 25 bold",borderwidth=4,relief=RAISED,
                   height=0,width=9,bg='navy', fg='white')
DataEntry = Button(btn_Frame,text='Data Entry',font="Orbitron-Bold 25 bold",borderwidth=4,relief=RAISED,
                   height=0,width=9,bg='navy', fg='white')
HomePage = Button(btn_Frame,text='Home Page',font="Orbitron-Bold 25 bold",borderwidth=4,relief=RAISED,
                  height=0,width=9,bg='navy', fg='white')
Refresh = Button(btn_Frame,text='Refresh',font="Orbitron-Bold 25 bold",borderwidth=4,relief=RAISED,
                 height=0,width=9,bg='navy', fg='white')
sync_up.place(x=23,y=20)
sync_down.place(x=23, y=120)
DataEntry.place(x=23, y=220)
HomePage.place(x=23, y=320)
Refresh.place(x=23, y=420)

root.mainloop()
