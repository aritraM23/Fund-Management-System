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
root.config(bg='DarkGoldenrod1')
root.geometry("1100x700+290+55")
root.minsize(1100,700)
root.maxsize(1100,700)
root.title("IVS/Loan/LoanDetails")
p1 = PhotoImage(master=root,file='[DIGICURE MAIN LOGO].png')
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
	
	myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="mancunian@2002",
										 database='ivs2')
	mycursor = myDataBase.cursor()
	mycursor.execute("select * from dataEntry")
	result = mycursor.fetchall()
	if len(result) != 0:
		tree_v.delete(*tree_v.get_children())
		for row in result:
			tree_v.insert('', END, values=row)
	myDataBase.commit()
	myDataBase.close()

def sync_on():

	try:
		totalData = db.child('mainData').get()
		
		mycursor.execute('Delete From dataEntry')
		for data in totalData.each():
			dataCollection = 'Insert into dataEntry (serialNumber,name,amount,date) values (%s,%s,%s,%s)'
			datas = [(data.val()['serialNumber'],data.val()['name'], data.val()['amount'], data.val()['date'])]
			mycursor.executemany(dataCollection, datas)
			myDataBase.commit()
		myDataBase.close()
		tkinter.messagebox.showinfo('Sync Info','Data Synced')
	except Exception as e:
		print(e)
		tkinter.messagebox.showerror('Sync Info',e)

# if (databaseChoice == 'f'):
def sync_off():
	try:
		db.child('mainData').remove()
		db.child('registerUserExp').remove()
		query = 'Select * from dataEntry'
		mycursor.execute(query)
		totalEntries = mycursor.fetchall()
		
		for rows in totalEntries:
			datas = {'serialNumber': rows[0], 'name': rows[1], 'amount': rows[2], 'date': rows[3]}
			db.child('mainData').push(datas)
			db.child('registerUserExp').child(rows[1]).push(datas)
		tkinter.messagebox.showinfo('Success', 'Done')
	except Exception as e:
		tkinter.messagebox.showerror('Sync Info', e)

def refresh():
    display()

def do_press(ev):
    display()

# #-----------------------------------Heading Frame and Label---------------------------------#
Heading = Frame(root,bg='SpringGreen4',borderwidth=4,relief=SUNKEN)
Heading.pack(fill=X)
Heading_Label = Label(Heading,text="------------ACCOUNT DETAILS------------",font="Helvetica 18 bold", bg='SpringGreen4',fg='black')
Heading_Label.pack()
#------------------------------------Time and Date Widgets----------------------------------#
def time_widget():
    string = strftime('%I:%M:%S %p')
    Time_Label.config(text=string)
    Time_Label.after(1000, time_widget)


Time_Label = Label(root, fg="black", bg="DarkGoldenrod1",
                   font="Helvetica 17 bold")
Time_Label.place(x=955, y=48)
time_widget()


date = Label(root, text=f"{dt.datetime.now():%A, %b/%d/%Y}", fg="black", bg="DarkGoldenrod1", font=(
    "Helvetica 15 bold"))
date.place(x=1, y=50)
#-----------------------------------------Tree View------------------------------------------#
tv_Frame = Frame(root, width=320, height=500,borderwidth=6,relief=SUNKEN)
tv_Frame.place(x=70, y=100)

y_scroll = Scrollbar(tv_Frame, orient=VERTICAL)
x_scroll = Scrollbar(tv_Frame, orient=HORIZONTAL)
tree_v = ttk.Treeview(tv_Frame,height=25,selectmode="extended")
y_scroll.pack(side=RIGHT, fill=Y)
x_scroll.pack(side=BOTTOM, fill=X)
tree_v['columns'] = ("Serial Number","Name","Amount","Date")
#name,mobileNumber,date,pricipalAmount,interestPercent,principleLeft,interestLeft,InterestPaidTillDate
# ~TreeView Styling~
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font="Consolas 10 bold ",fieldbackground='hotDarkGoldenrod1')
style.configure("Treeview",fieldbackground="white")
style.map('Treeview',background=[('selected','DarkGoldenrod1')])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

tree_v.column('#0', width=0, stretch=NO)
tree_v.column('Serial Number', anchor=CENTER, width=140)
tree_v.column('Name', anchor=CENTER, width=200)
tree_v.column('Amount', anchor=CENTER, width=120)
tree_v.column('Date', anchor=CENTER, width=148)
# tree_v.column('Loan Taken', anchor=CENTER, width=125)

tree_v.heading('#0', anchor=CENTER,text='')
tree_v.heading('Serial Number', anchor=CENTER, text="Serial Number")
tree_v.heading('Name', anchor=CENTER, text="Name")
tree_v.heading('Amount', anchor=CENTER, text="Amount")
tree_v.heading('Date', anchor=CENTER, text="Date")
# tree_v.heading('Loan Taken', anchor=CENTER, text="Loan Taken")

tree_v.pack(fill=X)

# while True:
#     sleep(60 - time() % 60)
tree_v.bind('<ButtonRelease-1>',do_press)
display()
#------------Buttons-------------#
btn_Frame = Frame(root,bg='SpringGreen4',height = 280,width =160,borderwidth=4,relief=SUNKEN)
btn_Frame.place(x=860,y=190)
sync_up = Button(btn_Frame,text='Sync Up',font="Helvetica 16 bold",borderwidth=4,relief=RAISED,height=0,width=9,bg='DarkGoldenrod1', command= sync_on)
sync_down = Button(btn_Frame,text='Sync Down',font="Helvetica 16 bold",borderwidth=4,relief=RAISED,height=0,width=9,bg='DarkGoldenrod1',command = sync_off)
# DataEntry = Button(btn_Frame,text='Data Entry',font="Helvetica 16 bold",borderwidth=4,relief=RAISED,height=0,width=9,bg='DarkGoldenrod1')
HomePage = Button(btn_Frame,text='Home Page',font="Helvetica 16 bold",borderwidth=4,relief=RAISED,height=0,width=9,bg='DarkGoldenrod1',command=home)
Refresh = Button(btn_Frame,text='Refresh',font="Helvetica 16 bold",borderwidth=4,relief=RAISED,height=0,width=9,bg='DarkGoldenrod1', command= refresh)
sync_up.place(x=12,y=20)
sync_down.place(x=12, y=85)
# DataEntry.place(x=12, y=150)
HomePage.place(x=12, y=150)
Refresh.place(x=12, y=215)


root.mainloop()
