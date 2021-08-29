import tkinter.messagebox
from tkinter import *
import pyrebase
import mysql.connector
from PIL.ImageTk import PhotoImage
import pandas as pd
import math
from envVar import firebaseConfig as fc

firebase = pyrebase.initialize_app(fc)
db = firebase.database()

root = Tk()
root.geometry("550x450+600+90")
root.maxsize(550, 450)
root.minsize(550, 450)
root.configure(bg='midnight blue')
root.title("Deposit on Existing Loan")
p1 = PhotoImage(master=root,file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE, p1)

name_entry = StringVar()
mob_entry = StringVar()
p_entry = StringVar()
i_entry = StringVar()
date_L = StringVar()


def back():
    import _thread
    _thread.exit_thread()

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
			each = pd.to_datetime(each)
		i = 1
		while(i<=count):
			if date_cur.month - last_date[i].month == 1:
				repay(nameList[i],mobileList[i],ppaid, intPaid, currentDate)
			i = i+1

	except:
		pass

def delete():
	try:
		name = nameEnt.get()
		mob = mobile.get()
		deleteSum = 0
		loanDB = db.child('loanData').get()
		for datas in loanDB.each():
			if datas.val()['name']==nameEnt.get() and datas.val()['mobileNumber']==mobile.get():
				print(datas.val()['name'])
				db.child('loanData').child(datas.key()).remove()
				deleteSum = deleteSum + 1
		myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivsloan')
		mycursor = myDataBase.cursor()

		mycursor.execute("delete from loanEntry where name=%s and mobileNumber=%s", (
				nameEnt.get(),
				mobile.get()
			))
		myDataBase.commit()
		myDataBase.close()
		deleteSum += 1
		if deleteSum == 2:
				tkinter.messagebox.showinfo('Delete Info','Delete Success')
		elif (deleteSum < 2):
				tkinter.messagebox.showerror('Delete Info','Delete Failure')

	except:
		try:
			myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs2')
			mycursor = myDataBase.cursor()

			mycursor.execute("delete from loanEntry where name=%s and mobileNumber=%s", (
					nameEnt.get(),
					mobile.get()
				))
			myDataBase.commit()
			myDataBase.close()
			tkinter.messagebox.showinfo('Delete Info', 'Delete Success')
		except Exception as err:
			tkinter.messagebox.showerror(nameEnt.get(),err)

def repay():
	
	name = nameEnt.get()
	print(name)
	mobileNumber = mobile.get()
	print(mobileNumber)
	principlePaid = principal.get()
	interestPaid = interest.get()
	updateDate = dateEnt.get()
	
	if name == 'ALL':
		monthlycalc(updateDate)
	newPriciple = 0
	newInterst = 0
	interestPaidTillDates = 0
	try:
		loanInfo = db.child('loanData').get()
		for info in loanInfo.each():
			print('calcuation started')
			if (nameEnt.get() == info.val()['name'] or mobile.get() == info.val()['mobileNumber']):
				
				previousPrinciple = info.val()['principalLeft']
				interstLeft = info.val()['interestLeft']
				interestPaidTill = info.val()['interestPaidTillDate']
				newPriciple = int(previousPrinciple) - int(principlePaid)
				print(newPriciple)
				newInterst = int(interstLeft) - int(interestPaid) + math.ceil(
					(newPriciple * int(info.val()['interestPercent'])) / 100)
				interestPaidTillDates = float(interestPaidTill) + float(interestPaid)
				date = date_L.get()
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
		myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
											 database='ivsLoan')
		mycursor = myDataBase.cursor()
		mycursor.execute(
			'UPDATE loanEntry set principleLeft= %s , interestLeft =%s , InterestPaidTillDate =%s, dateGiven = %s where name=%s and mobileNumber = %s ',
			(newPriciple, newInterst, interestPaidTillDates, updateDate, name, mobileNumber))
		myDataBase.commit()
		myDataBase.close()
		tkinter.messagebox.showinfo('Success', 'Priciple and Interest Added')
	except:
		tkinter.messagebox.showinfo('No Internet',
									'You are offline. Saving your data offline. Please sync your databases later')
		myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
											 database='ivsLoan')
		mycursor = myDataBase.cursor()
		
		mycursor.execute(
				'UPDATE loanEntry set principleLeft= %s , interestLeft =%s , InterestPaidTillDate =%s, dateGiven = %s where name=%s and mobileNumber = %s ',
				(newPriciple, newInterst, interestPaidTillDates, updateDate, name, mobileNumber))
		
		myDataBase.commit()
		myDataBase.close()
		tkinter.messagebox.showinfo('Success', 'Priciple and Interest Added In Local DataBase. Please sync later')
def updateText(data):
	try:
		#update the drop down list
		# Clear the listbox
		my_list.delete(0, END)

		# Add toppings to listbox
		for item in data:
			my_list.insert(END, item)
	except:
		pass

def fillout(event):
    # Delete whatever is in the entry box
    nameEnt.delete(0, END)

    # Add clicked list item to entry box
    nameEnt.insert(0, my_list.get(ANCHOR))

def check(event):
    # print("hello")
    # grab what was typed
    typed = name_entry.get()
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


Back = Button(root, text="Back", bg='gold', font="Helvetica 11 bold", borderwidth=4, relief=RAISED, command=back)
Back.place(x=20, y=50)

f1 = Frame(root, bg='gold', borderwidth=10,
		   relief=RAISED, width=500, height=55)
f1.pack(side=TOP, fill=X)
l1 = Label(f1, text="----Deposit Loan----", bg='gold',
		   fg='black', font="Helvetica 12 bold").pack(fill=X)

name_label = Label(root, bg='midnight blue', fg='gold',
				   font="Helvetica 11 bold", text="Name")
name_label.place(x=165, y=135)
mob_label = Label(root, bg='midnight blue', fg='gold',
				  font="Helvetica 11 bold", text="Mobile No.")
mob_label.place(x=129, y=219)
principal_label = Label(root, bg='midnight blue', fg='gold',
						font="Helvetica 11 bold", text="Principal Given")
principal_label.place(x=94, y=249)
interest_label = Label(root, bg='midnight blue', fg='gold',
					   font="Helvetica 11 bold", text="Interest Given")
interest_label.place(x=102, y=279)

date_label = Label(root, bg='midnight blue', fg='gold',
				   font="Helvetica 11 bold", text="Date")
date_label.place(x=172, y=309)

nameEnt = Entry(root, width=27, textvariable=name_entry,
			 borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
nameEnt.place(x=230, y=131)

my_list = Listbox(root, font =('arial', 13, 'bold'),height = 2, width=25, justify='left')
my_list.place(x = 232, y=170)

listVal = []
def getNameList():
	try:
		listVal = []
		listname = db.child('loanData').get()
		for each in listname.each():
			print(each.val()['name'])
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
nameEnt.bind("<KeyRelease>", check)


mobile = Entry(root, width=27, textvariable=mob_entry,
			   borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
mobile.place(x=230, y=218)
principal = Entry(root, width=27, textvariable=p_entry,
				  borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
principal.place(x=230, y=248)
interest = Entry(root, width=27, textvariable=i_entry,
				 borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
interest.place(x=230, y=278)

dateEnt = Entry(root, width=27, textvariable=date_L,
				borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
dateEnt.place(x=230, y=308)

name_entry = nameEnt.get()
mob_entry = mobile.get()
p_entry= principal.get()
i_entry = interest.get()
date_L = dateEnt.get()

submit_button = Button(root, text="Add", bg='gold', fg='black',
					   font="Helvetica 11 bold", relief=SUNKEN, command=repay)
submit_button.place(x=360, y=350)

delete_button = Button(root, text="Delete", bg='gold', fg='black',
					   font="Helvetica 11 bold", relief=SUNKEN, command=delete)
delete_button.place(x=403, y=350)

root.mainloop()
