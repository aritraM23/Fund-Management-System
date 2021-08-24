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
import math
import mysql.connector
import datetime as dt
from PIL.ImageTk import PhotoImage
from envVar import firebaseConfig as fc


firebase=pyrebase.initialize_app(fc)
db= firebase.database()


root = Tk()
root.state('zoomed')
root.config(bg="navy")
root.title("HomePage")
root.resizable(0,0)
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')


name=StringVar()
amount = 0

def monthlycalc(currentDate):
	date_cur = pd.to_datetime(currentDate)
	try:
		loanDB = db.child('loanData').get()
		nameList = [info.val()['name'] for info in loanDB.each()]
		mobileList = [info.val()['name'] for info in loanDB.each()]
		ppaid = 0
		intPaid = 0
		last_date = [info.val()['lastPaidDate'] for info in loanDB.each()]
		
		count = 0
		for each in last_date:
			count = count + 1
			# each = pd.to_datetime(each)
			
		for i in range(count):
			
			last_payday = pd.to_datetime(last_date[i])
			
			if (date_cur.month - last_payday.month == 1):
			
				repay(nameList[i],mobileList[i],ppaid, intPaid, currentDate)
        
	except:
		pass

def repay(nameL = 'ALL',mobL = 'ALL', princL = 0, intL = 0, Payment_date = datetime.today().strftime("%d/%m/%Y")):
	
	name = nameL
	mobileNumber = mobL
	principlePaid = princL
	interestPaid = intL
	updateDate = Payment_date
	
	if name == 'ALL':
		monthlycalc(updateDate)
	newPriciple = 0
	newInterst = 0
	interestPaidTillDates = 0
	try:
		loanInfo = db.child('loanData').get()
		for info in loanInfo.each():
			if (name == info.val()['name'] or mobileNumber == info.val()['mobileNumber']):
				
				previousPrinciple = info.val()['principalLeft']
				interstLeft = info.val()['interestLeft']
				interestPaidTill = info.val()['interestPaidTillDate']
				newPriciple = int(previousPrinciple) - int(principlePaid)
				newInterst = int(interstLeft) - int(interestPaid) + math.ceil(
					(newPriciple * int(info.val()['interestPercent'])) / 100)
				interestPaidTillDates = float(interestPaidTill) + float(interestPaid)
				date = updateDate
				if (date.find("-") > -1):
					tday, tm, ty = date.split("-")
					mdate = tday + "/" + tm + "/" + ty
					date = mdate
				elif date.find(".") > -1:
					tday, tm, ty = date.split(".")
					mdate = tday + "/" + tm + "/" + ty
					date = mdate
				db.child('loanData').child(info.key()).update({'principalLeft': newPriciple,
															   'interestLeft': newInterst,
															   'interestPaidTillDate': interestPaidTillDates,
															   'lastPaidDate': updateDate})
		myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="Anik123#",
											 database='ivsLoan')
		mycursor = myDataBase.cursor()
		mycursor.execute(
			'UPDATE loanEntry set principleLeft= %s , interestLeft =%s , InterestPaidTillDate =%s, dateGiven = %s where name=%s and mobileNumber = %s ',
			(newPriciple, newInterst, interestPaidTillDates, updateDate, name, mobileNumber))
		tkinter.messagebox.showinfo('Success', 'Priciple and Interest Added')
	except:
		tkinter.messagebox.showinfo('No Internet',
									'You are offline. Saving your data offline. Please sync your databases later')
		myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="Anik123#",
											 database='ivsLoan')
		mycursor = myDataBase.cursor()
		
		mycursor.execute(
				'UPDATE loanEntry set principleLeft= %s , interestLeft =%s , InterestPaidTillDate =%s, dateGiven = %s where name=%s and mobileNumber = %s ',
				(newPriciple, newInterst, interestPaidTillDates, updateDate, name, mobileNumber))
		tkinter.messagebox.showinfo('Success', 'Priciple and Interest Added In Local DataBase. Please sync later')

def refresh():
    today_date = datetime.today().strftime("%d/%m/%Y")

    try:
        repay()
    except:
		pass
def updateText(data):
    #update the drop down list
    # Clear the listbox
    try:
        my_list.delete(0, END)

        # Add toppings to listbox
        for item in data:
            my_list.insert(END, item)
    except:
        pass

def fillout(event):
    # Delete whatever is in the entry box
    customer_name.delete(0, END)

    # Add clicked list item to entry box
    customer_name.insert(0, my_list.get(ANCHOR))

def check(event):
  
    typed = name.get()
  
    if typed == '':
        data = listVal
    else:
        data = []
        for item in listVal:
            if typed.lower() in item.lower():
                data.append(item)

    # update our listbox with selected items
    updateText(data)


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


Time_Label = Label(root, fg="black", bg="DarkGoldenrod1",
                   font="Devanagari 25 bold", borderwidth=6, relief=SUNKEN)
Time_Label.place(x=1326, y=65)
Time()


def search():
    balance=Label(mainFrame,fg='black',bg='DarkGoldenrod1',width= 15,font="Constantia 26 bold",text="Balance:  " + str(ind_Bal()))
    balance.place(x=60,y=195)
    Loan=Label(mainFrame,fg='black',bg='DarkGoldenrod1', width = 20,font="Constantia 26 bold",text="Loan Remaining:  " + str(loaninfor()))
    Loan.place(x=480,y=195)


date = Label(root, text=f"{dt.datetime.now():%a, %b/%d/%Y}", bg="DarkGoldenrod1", fg="black", font=(
    "helvetica 26 bold"), borderwidth=6, relief=SUNKEN)
date.place(x=1, y=65)


top_Frame = Frame(root,bg="DarkGoldenrod1",borderwidth=4,relief=SUNKEN)
top_Frame.pack(fill=X)
top_label = Label(top_Frame,text="---------HOMEPAGE--------",bg="DarkGoldenrod1",fg="black",font="Orbitron-Bold 30 bold")
top_label.pack()

#-----MainFrame-------
mainFrame = Frame(root, bg='DarkGoldenrod1', borderwidth=6, relief=SUNKEN, width=1000, height=650)
mainFrame.place(x=307, y=140)
customer = Label(mainFrame,text="Customer Name:",font="Constantia 25 bold",bg='DarkGoldenrod1',fg='black')
customer.place(x=45, y=24)
customer_name=Entry(mainFrame,justify=CENTER,borderwidth=4,textvariable=name,font="Consolas 25 bold",width=30)
customer_name.place(x=400, y=24)

my_list = Listbox(mainFrame, font =('arial', 22, 'bold'),height = 3, width=34, justify='left')
my_list.place(x = 400, y=74)

listVal = []
def getNameList():
    try:
        listVal = []
        listname = db.child('mainData').get()
        for each in listname.each():

            listVal.append(each.val()['name'])

        listVal = list(set(listVal))
        return listVal
    except:
        pass

listVal = getNameList()

updateText(listVal)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
customer_name.bind("<KeyRelease>", check)

chk_btn_frame = Frame(mainFrame, bg='navy', borderwidth=6, relief=SUNKEN)
chk_btn_frame.place(x=30, y=70)
Check=Button(chk_btn_frame,text="Search",bg='DarkGoldenrod1',font="Helvetica 22 bold",borderwidth=4,
             relief=RIDGE,command=search,width=6)
Check.pack()
ref_btn_frame = Frame(mainFrame, bg='navy', borderwidth=6, relief=SUNKEN)
ref_btn_frame.place(x=200, y=70)
Refresh=Button(ref_btn_frame,text="Refresh",bg='DarkGoldenrod1',font="Helvetica 22 bold",borderwidth=4,
             relief=RIDGE,command=refresh,width=6)
Refresh.pack()

# Refresh=Button(root,text="Refresh",bg='DarkGoldenrod1',font="Helvetica 17 bold",borderwidth=2,relief=SUNKEN,command=refresh,width=8)
# Refresh.place(x=500,y=450)

accIcon = PhotoImage(master= root,file = "acc.png")
loanIcon = PhotoImage(master= root,file = "loan.png")

accFrame = Frame(mainFrame, bg='black', borderwidth=5, relief=SUNKEN)
accFrame.place(x=120, y=250)
accounts=Button(accFrame,image = accIcon,bg='DarkGoldenrod1',font="Helvetica 16 bold",
                borderwidth=4,relief=RIDGE, command= AccountsPage)
accounts.pack()
loanFrame = Frame(mainFrame, bg='black', borderwidth=5, relief=SUNKEN)
loanFrame.place(x=600, y=250)
loan=Button(loanFrame,image = loanIcon,bg='DarkGoldenrod1',font="Helvetica 16 bold",
            borderwidth=4,relief=SUNKEN, command= loadtransfer)
loan.pack()

accLab = Label(mainFrame,text="Accounts",font="Constantia 24 bold", bg='DarkGoldenrod1', fg='black')
accLab.place(x=160, y=450)

loanLab = Label(mainFrame,text="Loans",font="Constantia 24 bold", bg='DarkGoldenrod1', fg='black')
loanLab.place(x=670, y=450)

Treasury=Label(mainFrame,bg='DarkGoldenrod1',fg='black',font="Constantia 27 bold",text="Treasury: Rs. "+ str(treasure()))
Treasury.place(x=340, y=550)

root.mainloop()
