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

def monthlycalc(currentDate):
	date_cur = pd.to_datetime(currentDate)
	try:
		print("Refreshing...")
		loanDB = db.child('loanData').get()
		nameList = [info.val()['name'] for info in loanDB.each()]
		print(nameList)
		mobileList = [info.val()['name'] for info in loanDB.each()]
		print(mobileList)
		ppaid = 0
		intPaid = 0
		last_date = [info.val()['lastPaidDate'] for info in loanDB.each()]
		print(last_date)
		count = 0
		for each in last_date:
			count = count + 1
			# each = pd.to_datetime(each)
			
		print(count)
# 		print(last_date)
		for i in range(count):
			print('inside loop')
			last_payday = pd.to_datetime(last_date[i])
			print(last_payday.month)
			if (date_cur.month - last_payday.month == 1):
				print('inside if')
				repay(nameList[i],mobileList[i],ppaid, intPaid, currentDate)
        
	except:
		pass

def repay(nameL = 'ALL',mobL = 'ALL', princL = 0, intL = 0, Payment_date = datetime.today().strftime("%d/%m/%Y")):
	
	name = nameL
	print(name)
	mobileNumber = mobL
	print(mobileNumber)
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
			print('calcuation started')
			if (name == info.val()['name'] or mobileNumber == info.val()['mobileNumber']):
				
				previousPrinciple = info.val()['principalLeft']
				interstLeft = info.val()['interestLeft']
				interestPaidTill = info.val()['interestPaidTillDate']
				newPriciple = int(previousPrinciple) - int(principlePaid)
				print(newPriciple)
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
		myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="mancunian@2002",
											 database='ivsLoan')
		mycursor = myDataBase.cursor()
		mycursor.execute(
			'UPDATE loanEntry set principleLeft= %s , interestLeft =%s , InterestPaidTillDate =%s, dateGiven = %s where name=%s and mobileNumber = %s ',
			(newPriciple, newInterst, interestPaidTillDates, updateDate, name, mobileNumber))
		tkinter.messagebox.showinfo('Success', 'Priciple and Interest Added')
	except:
		tkinter.messagebox.showinfo('No Internet',
									'You are offline. Saving your data offline. Please sync your databases later')
		myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="mancunian@2002",
											 database='ivsLoan')
		mycursor = myDataBase.cursor()
		
		mycursor.execute(
				'UPDATE loanEntry set principleLeft= %s , interestLeft =%s , InterestPaidTillDate =%s, dateGiven = %s where name=%s and mobileNumber = %s ',
				(newPriciple, newInterst, interestPaidTillDates, updateDate, name, mobileNumber))
		tkinter.messagebox.showinfo('Success', 'Priciple and Interest Added In Local DataBase. Please sync later')

def refresh():
    today_date = datetime.today().strftime("%d/%m/%Y")

    # try:
        # import Loan_RepayPage as LP
    repay()
    print('loan interest calculated')
    # except:
    #     print("loan calculation of all failed")
    
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
    # print("hello")
    # grab what was typed
    typed = name.get()
    print(typed)

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

my_list = Listbox(root, font =('arial', 13, 'bold'),height = 4, width=30, justify='left')
my_list.place(x = 495, y=200)

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

Check=Button(root,text="Search",bg='gold',font="Helvetica 17 bold",borderwidth=2,relief=SUNKEN,command=search,width=8)
Check.place(x=500,y=250)

Refresh=Button(root,text="Refresh",bg='gold',font="Helvetica 17 bold",borderwidth=2,relief=SUNKEN,command=refresh,width=8)
Refresh.place(x=500,y=450)

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
