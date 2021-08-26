import csv
from functools import partial
import _thread
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
from envVar import firebaseConfig as fc
from envVar import mycursor, myDataBase
from PIL.ImageTk import PhotoImage
firebase = pyrebase.initialize_app(fc)
db = firebase.database()

root = tkinter.Tk()


	

titlespace = " "
root.title(100 * titlespace + "Money Management System")
root.geometry("883x750+330+0")
root.maxsize(883, 750)
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
#		root.iconphoto(False, p1)

# clock function for live clock
QName = StringVar()
sumDep = 0

def times():
	current_time = time.strftime("%I:%M:%S")
	clock.config(text=current_time)
	clock.after(200, times)

btnState = False

def switch():
	global btnState
	if btnState is True:
		for x in range(300):
			navRoot.place(x=-x, y=0)
			TitleFrame.update()
		
		btnState = False
	
	else:
		
		for x in range(-300, 0):
			navRoot.place(x=x, y=0)
			TitleFrame.update()
		
		btnState = True

def export():
	with open('FullFile.csv', 'w') as file:
		write = csv.writer(file)
		write.writerow(["Name", "Amount", "Date", "Loan Taken", "Principal To be Paid", "Interest To be Paid"])
		file.close()
	totalData = db.child('mainData').get()
	loanDB = db.child('loanData').get()
	for data in totalData.each():
		for ld in loanDB.each():
			with open('FullFile.csv', 'a') as files:
				write = csv.writer(files)
				if ld.val()['name'] == data.val()['name']:
					write.writerow([data.val()['name'], data.val()['amount'], data.val()['date'],
									ld.val()['principalAmount'], ld.val()['principalLeft'],
									ld.val()['interestLeft']])
					files.close()
				else:
					write.writerow(
						[data.val()['name'], data.val()['amount'], data.val()['date'], 'N/A', 'N/A', 'N/A'])
					files.close()
	os.system('FullFile.csv')
	return 0

def ind_import():
	
	def s_byname():
		name = QName.get()
		sumDep = 0
		totalData = db.child('registerUserExp').child(name).get()
		
		for data in totalData.each():
			sumDep += int(data.val()['amount'])
		
		deposit.config(text=str(sumDep))
	
	# return sumDep
	
	ind = Toplevel(root)
	ind.geometry("578x340+330+0")
	ind.title(50 * titlespace + "Money Management System")
	# ind.maxsize("570x250")
	# ind.resizable(False)
	
	mainFrame = Frame(ind, bd=10, width=500, height=370, relief=RIDGE, bg='black')
	mainFrame.grid()
	
	# labelMain = Label(ind, bd=7, width=500, height=400, bg='black')
	# labelMain.grid(row = 0, column = 0)
	topFrame = Frame(mainFrame, bd=10, width=500, height=370, relief=RIDGE, bg='black')
	topFrame.grid(row=1, column=0)
	
	indtitleFrame = Frame(mainFrame, bd=10, width=500, height=70, bg='black')
	indtitleFrame.grid(row=0, column=0)
	
	indtitle = Label(indtitleFrame, font=('Arial', 18, 'bold'), fg='pink',
						  text="Import Individual Data by Name:", bd=7, bg='black')
	indtitle.grid(row=0, column=1, padx=70)
	
	indEntry = Entry(topFrame, font=('arial', 13, 'bold'), bd=13, width=50, justify='left',
						  textvariable=QName)
	indEntry.grid(row=0, column=0, padx=5)
	
	Label(topFrame, font=('Arial', 18, 'bold'), text=" ", bd=3, bg='black').grid(row=1, column=0,
																				 padx=70)
	
	Button(topFrame, font=('arial', 13, 'bold'), text="IMPORT", bd=5, padx=10, pady=1, width=5, height=2,
		   bg='pink', command=s_byname).grid(row=2, column=0, padx=1)
	
	output = Label(topFrame, font=('arial', 13, 'bold'), bd=13, width=50, justify='left',
						bg='black', fg='pink', text="Total Output:")
	output.grid(row=3, column=0, padx=5)
	
	deposit = Label(topFrame, font=('arial', 13, 'bold'), bd=13, width=50, justify='left',
						 bg='black', fg='pink', text=str(sumDep))
	deposit.grid(row=4, column=0, padx=5)

# root.maxsize(460,350)
# root.destroy()
# import indiv
# root.destroy()
# indiv.gui(tkinter.Tk())

def display_all():
	_thread.start_new_thread(accountsInfo,(1,2))
def accountsInfo(j,k):
	import treeViewAccounts
def back():
	_thread.exit_thread()
	
	
###################################################################################################################################
MainFrame = Frame(root, bd=10, width=770, height=700, relief=RIDGE, bg='black')
MainFrame.grid()

TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, bg='black')
TitleFrame.grid(row=0, column=0)
TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, bg='pink')
TopFrame3.grid(row=1, column=0)

LeftFrame = Frame(TopFrame3, bd=5, width=770, height=500, padx=2, pady=0, bg='black')
LeftFrame.pack(side=LEFT, expand=True, fill='both')
LeftFrame1 = Frame(LeftFrame, bd=5, width=770, height=180, padx=2, pady=0, bg='pink')
LeftFrame1.pack(side=TOP, expand=True, fill='both')

RightFrame = Frame(TopFrame3, bd=5, width=50, height=100, relief=RIDGE, padx=2, bg='black')
RightFrame.pack(side=RIGHT, expand=True, fill='both')
RightFrame1a = Frame(RightFrame, bd=5, width=40, height=90, padx=12, pady=4, bg='black')
RightFrame1a.pack(side=TOP, expand=True, fill='both')

lbltitle = Label(TitleFrame, font=('Arial', 33, 'bold'), fg='pink', text="Money Management System", bd=7,
					  bg='black')
lbltitle.grid(row=0, column=1, padx=70)

SerialNumber = StringVar()
Name = StringVar()
Amount = StringVar()
Date = StringVar()

# ===============================================================================================================================================================================================

def updateText(data):
	# update the drop down list
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
	try:
		entName.delete(0, END)
		
		# Add clicked list item to entry box
		entName.insert(0, my_list.get(ANCHOR))
	except:
		pass
def check(event):
	# print("hello")
	# grab what was typed
	try:
		typed = Name.get()
		
		
		if typed == '':
			data = listVal
		else:
			data = []
			for item in listVal:
				if typed.lower() in item.lower():
					data.append(item)
		
		# update our listbox with selected items
		updateText(data)
	except:
		pass
# Input Fields:

lblserial = Label(LeftFrame1, font=('arial', 13, 'bold'), text='Serial Number', bd=13, bg='pink')
lblserial.grid(row=1, column=0, sticky=W, padx=2)

entserial = Entry(LeftFrame1, font=('arial', 13, 'bold'), bd=6, width=50, justify='left',
					   textvariable=SerialNumber)
entserial.grid(row=1, column=1, sticky=W, padx=2)

lblname = Label(LeftFrame1, font=('arial', 13, 'bold'), text='Name', bd=13, bg='pink')
lblname.grid(row=2, column=0, sticky=W, padx=2)

entName = Entry(LeftFrame1, font=('arial', 13, 'bold'), bd=6, width=50, justify='left', textvariable=Name)
entName.grid(row=2, column=1, sticky=W, padx=2)

my_list = Listbox(LeftFrame1, font=('arial', 13, 'bold'), height=3, width=51, justify='left')
my_list.grid(row=3, column=1, sticky=W, padx=2)

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
# entName['values'] = listVal
# entName.current()
listVal = getNameList()

# Add the toppings to our list
updateText(listVal)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
entName.bind("<KeyRelease>", check)

# entname = Entry(LeftFrame1, font=('arial', 13, 'bold'), bd=6, width=50, justify='left', textvariable=Name)
# entname.grid(row=2, column=1, sticky=W, padx=2)

lblamount = Label(LeftFrame1, font=('arial', 13, 'bold'), text='Amount', bd=13, bg='pink')
lblamount.grid(row=4, column=0, sticky=W, padx=2)

entamount = Entry(LeftFrame1, font=('arial', 13, 'bold'), bd=6, width=50, justify='left',
					   textvariable=Amount)
entamount.grid(row=4, column=1, sticky=W, padx=2)

lblDate = Label(LeftFrame1, font=('arial', 13, 'bold'), text='Date', bd=13, bg='pink')
lblDate.grid(row=5, column=0, sticky=W, padx=2)

entDate = Entry(LeftFrame1, font=('arial', 13, 'bold'), bd=6, width=50, justify='left', textvariable=Date)
entDate.grid(row=5, column=1, sticky=W, padx=2)

# label for clock display
clock = Label(TitleFrame, font=("times", 15, "bold"), bg="black", fg='pink')
clock.grid(row=0, column=2, padx=0, pady=0)
times()
# ===============================================================================================================================================================================================

# nav bar
navIcon = PhotoImage(master = root,file='navbar.png')
closeIcon = PhotoImage(master= root,file='exit.png')

nvbarbtn = Button(TitleFrame, image = navIcon ,width=24, height=24, bd=0, padx=1, command=switch).grid(
	row=0, column=0, padx=0, pady=0)
navRoot = Frame(root, bg='pink', height=500, width=200)
navRoot.place(x=-300, y=0)

Label(navRoot, text="Menu", font='arial 10 bold', bg='black', fg='pink', height=3, width=200,
	  padx=0).place(x=0, y=0)

y = 80

options = ["Export All", "Import Individual", "Display All"]
methods = [export, ind_import, display_all, back]

navExp = Button(navRoot, text="Export All", font="arial 13", bg="pink", fg='black',
					 activebackground="pink", activeforeground="black", bd=0, command=export).place(x=25,
																									y=y)
y += 40

navInd = Button(navRoot, text="Import Individual", font="arial 13", bg="pink", fg='black',
					 activebackground="pink", activeforeground="black", bd=0, command=ind_import).place(x=25,
																										y=y)
y += 40

navInd = Button(navRoot, text="Display All", font="arial 13", bg="pink", fg='black',
					 activebackground="pink", activeforeground="black", bd=0, command=display_all).place(x=25,
																										y=y)
y += 40

navAbt = Button(navRoot, text="Back", font="arial 13", bg="pink", fg='black',
					 activebackground="pink", activeforeground="black", bd=0, command=back).place(x=25,
																								  y=y)

closeBtn = Button(navRoot, image = closeIcon, width=22, height=22, relief=RIDGE, bd=0, padx=1,
					   command=switch)
closeBtn.place(x=150, y=20)

# ===============================================================================================================================================================================================
# The functions:

def exit():
	Exit = tkinter.messagebox.askyesno("Funds Man Sys", "Confirm if you want to exit?")
	if Exit > 0:
		root.destroy()
		return

def saveData():
	global listVal
	serialNumber = SerialNumber.get()
	name = Name.get()
	amount = Amount.get()
	date = Date.get()
	if (date.find("-") > -1):
		tday, tm, ty = date.split("-")
		mdate = tday + "/" + tm + "/" + ty
		date = mdate
	elif date.find(".") > -1:
		tday, tm, ty = date.split(".")
		mdate = tday + "/" + tm + "/" + ty
		date = mdate
	try:
		if (Name.get() != '' and Date.get() != '' and Amount.get() != ''):
			datas = {'serialNumber': serialNumber, 'name': name, 'amount': amount, 'date': date}
			db.child('mainData').push(datas)
			db.child('registerUserExp').child(name).push(datas)
			listVal = getNameList()
			updateText(listVal)
			myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs2')
			mycursor = myDataBase.cursor()
			dataCollection = 'Insert into dataEntry (serialNumber,name,amount,date) values (%s,%s,%s,%s)'
			datas = [(serialNumber, name, amount, date)]
			
			mycursor.executemany(dataCollection, datas)
			myDataBase.commit()
			myDataBase.close()
			display()
		
		else:
			alertMssg('Error', 'Insert Data In All Fields')
	except:
		
		dataCollection = 'Insert into dataEntry (serialNumber,name,amount,date) values (%s,%s,%s,%s)'
		datas = [(serialNumber, name, amount, date)]
		
		mycursor.executemany(dataCollection, datas)
		myDataBase.commit()
		myDataBase.close()
		succesMsg('Offline','Data Inserted')

def update():
	try:
		tempData = 0
		totalMainData = db.child('mainData').get()
		totalIndividualData = db.child('registerUserExp').child(Name.get()).get()
		for data in totalMainData.each():
				date = Date.get()
				if (date.find("-") > -1):
					tday, tm, ty = date.split("-")
					mdate = tday + "/" + tm + "/" + ty
					date = mdate
				elif date.find(".") > -1:
					tday, tm, ty = date.split(".")
					mdate = tday + "/" + tm + "/" + ty
					date = mdate
				if data.val()['name'] == Name.get() and data.val()['date'] == date:
					db.child('mainData').child(data.key()).update({'serialNumber': SerialNumber.get(), 'name': Name.get(), 'amount': Amount.get(),'date': date})
				tempData += 1
		for indi in totalIndividualData.each():
			date = Date.get()
			if (date.find("-") > -1):
				tday, tm, ty = date.split("-")
				mdate = tday + "/" + tm + "/" + ty
				date = mdate
			elif date.find(".") > -1:
				tday, tm, ty = date.split(".")
				mdate = tday + "/" + tm + "/" + ty
				date = mdate
			if indi.val()['name'] == Name.get() and indi.val()['date'] == date:
				db.child('registerUserExp').child(Name.get()).child(indi.key()).update(
							{'serialNumber': SerialNumber.get(),
							 'name': Name.get(),
							 'amount': Amount.get(),
							 'date': date
							 }
				)
			tempData += 1
		myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
											 database='ivs2')
		mycursor = myDataBase.cursor()
		
		mycursor.execute(
			'update dataEntry set amount=%s,name=%s,date=%s where serialNumber = %s', (
				Amount.get(),
				Name.get(),
				date,
				SerialNumber.get()
			))
		myDataBase.commit()
		myDataBase.close()
		tempData += 1
		
		if tempData > 0:
			succesMsg('Update Info', 'Data Updated' )
		else:
			alertMssg('Update Info', 'Problem Not Updated')
	
	except Exception as e:
		
		myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
											 database='ivs2')
		mycursor = myDataBase.cursor()
		
		tempData = 0
		mycursor.execute(
			'update dataEntry set amount=%s,name=%s,date=%s where serialNumber = %s', (
				Amount.get(),
				Name.get(),
				Date.get(),
				SerialNumber.get()
			))
		myDataBase.commit()
		myDataBase.close()
		tempData += 1
		if tempData >= 3:
			succesMsg('Update Info', e)
		else:
			alertMssg('Update Info', 'Problem Not Updated')

def search():
	sum = 0
	callAll = 'all'
	totalData = db.child('mainData').get()
	loanDB = db.child('loanData').get()
	
	date = Date.get()
	if (date.find("-") > -1):
		tday, tm, ty = date.split("-")
		mdate = tday + "/" + tm + "/" + ty
		date = mdate
	elif date.find(".") > -1:
		tday, tm, ty = date.split(".")
		mdate = tday + "/" + tm + "/" + ty
		date = mdate
	
	with open('data.csv', 'w') as file:
		write = csv.writer(file)
		write.writerow(["Serial Number","Name", "Amount", "Date", "Loan"])
		file.close()
	for data in totalData.each():
		for ld in loanDB.each():
			if ('all' == Name.get().lower()):
				with open('FullFile.csv', 'w') as file:
					write = csv.writer(file)
					write.writerow(["Serial Number","Name", "Amount", "Date", "Loan"])
					file.close()
				totalData = db.child('mainData').get()
				loanDB = db.child('loanData').get()
				for data in totalData.each():
					for ld in loanDB.each():
						with open('FullFile.csv', 'a') as files:
							write = csv.writer(files)
							if ld.val()['name'] == data.val()['name']:
								write.writerow([data.val()['serialNumber'],data.val()['name'], data.val()['amount'], data.val()['date'],ld.val()['principalAmount']])
								files.close()
							else:
								write.writerow(
									[data.val()['serialNumber'],data.val()['name'], data.val()['amount'], data.val()['date'], 'N/A'])
								files.close()
				os.system('FullFile.csv')
				return 0
			elif (data.val()['date'] == date or data.val()['name'] == Name.get() or data.val()[
				'amount'] == Amount.get()):
				with open('data.csv', 'a') as files:
					write = csv.writer(files)
					if ld.val()['name'] == data.val()['name']:
						write.writerow(
							[data.val()['serialNumber'],data.val()['name'], data.val()['amount'], data.val()['date'],
							 ld.val()['principalAmount']])
						files.close()
					else:
						write.writerow([data.val()['serialNumber'],data.val()['name'], data.val()['amount'], data.val()['date'], 'N/A'])
						files.close()
					sum += 1
	
	if sum > 0:
		os.system('data.csv')
	
	if sum == 0:
		alertMssg()

def succesMsg(heading,msg):
	tkinter.messagebox.showinfo(heading, msg)
	display()
	reset()

def alertMssg(heading,msg):
	tkinter.messagebox.showerror(heading, msg)
	display()
	reset()

def display():
	
	myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
										 database='ivs2')
	mycursor = myDataBase.cursor()
	mycursor.execute("select * from dataEntry ORDER BY serialNumber DESC")
	result = mycursor.fetchall()
	if len(result) != 0:
		display_data.delete(*display_data.get_children())
		for row in result:
			display_data.insert('', END, values=row)
	myDataBase.commit()
	myDataBase.close()


def delete():
	
	try:
		
		deleteData = 0
		totalIndividualData = db.child('registerUserExp').child(Name.get()).get()
	
		
		for data in totalIndividualData.each():
			if data.val()['name'] == Name.get() and data.val()['date'] == Date.get():
				db.child('registerUserExp').child(Name.get()).child(data.key()).remove()
				deleteData += 1
		allUserDataBase = db.child('mainData').get()
		for datas in allUserDataBase.each():
			if datas.val()['name'] == Name.get() and datas.val()['date'] == Date.get():
		
				db.child('mainData').child(datas.key()).remove()
				deleteData += 1
		myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs2')
		mycursor = myDataBase.cursor()
		
		mycursor.execute("delete from dataEntry where serialnumber=%s", (
			SerialNumber.get()
		))
		

		
		
		deleteData += 1
		myDataBase.commit()
		myDataBase.close()
		deleteData += 1
		if deleteData == 3:
			print(totta)
			succesMsg('Delete Info','Delete Success')
		if (deleteData <= 3):
			alertMssg('Delete Info','Delete Failure')
	except:
		try:
#					print(type(SerialNumber.get()))

			myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs2')
			mycursor = myDataBase.cursor()
			mycursor.execute("delete from dataEntry where name= %s and date = %s", (
				Name.get(),
				Date.get()
			))
			myDataBase.commit()
			myDataBase.close()
			deleteData += 1
			succesMsg('Delete Info','Delete Success')
		except Exception as e:
			print(e)
			print(SerialNumber.get())
			alertMssg('Delete Info',e)

def TrainInfo(ev):
	viewInfo = display_data.focus()
	learnData = display_data.item(viewInfo)
	row = learnData['values']
	SerialNumber.set(row[0])
	Name.set(row[1])
	Amount.set(row[2])
	Date.set(row[3])

def reset():
	entserial.delete(0, END)
	entName.delete(0, END)
	entamount.delete(0, END)
	entDate.delete(0, END)

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
		succesMsg('Sync Info','Data Synced')
	except Exception as e:
		print(e)
		alertMssg('Sync Info',e)

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
		succesMsg('Sync Info','Data Synced')
	except Exception as e:
		tkinter.messagebox.showerror('Sync Info', e)

# ==============================================================================================================================================================================================

y_scroll = Scrollbar(LeftFrame, orient=VERTICAL)
display_data = ttk.Treeview(LeftFrame, height=18, columns=('Serial Number', 'Name', 'Amount', 'Date'),
								 yscrollcommand=y_scroll.set)
y_scroll.pack(side=RIGHT, fill=Y)

display_data.heading("Serial Number", text="Serial Number")
display_data.heading("Name", text="NAME")
display_data.heading("Amount", text="AMOUNT")
display_data.heading("Date", text="DATE")

display_data['show'] = 'headings'

display_data.column("Serial Number", width=80)
display_data.column("Name", width=80)
display_data.column("Amount", width=80)
display_data.column("Date", width=80)

display_data.pack(fill=BOTH, expand=1)
display_data.bind("<ButtonRelease-1>", TrainInfo)
display()

# ==============================================================================================================================================================================================

btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="SYNC DOWN", bd=7, padx=18, pady=1,
						width=7, height=3, bg='pink', command=sync_off).grid(row=7, column=0, padx=1)
btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="UPDATE", bd=7, padx=18, pady=1, width=7,
						height=3, bg='pink', command=update).grid(row=2, column=0, padx=1)
btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="SAVE", bd=7, padx=18, pady=1, width=7,
						height=3, bg='pink', command=saveData).grid(row=1, column=0, padx=1)
btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="DELETE", bd=7, padx=18, pady=1, width=7,
						height=3, bg='pink', command=delete).grid(row=5, column=0, padx=1)
btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="SEARCH", bd=7, padx=18, pady=1, width=7,
						height=3, bg='pink', command=search).grid(row=4, column=0, padx=1)
btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="DISPLAY", bd=7, padx=18, pady=1,
						width=7, height=3, bg='pink', command=display).grid(row=3, column=0, padx=1)
btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="SYNC UP", bd=7, padx=18, pady=1,
						width=7, height=3, bg='pink', command=sync_on).grid(row=6, column=0, padx=1)


# ================================================================================================================================================================================================

# Main:

# if __name__ == '__main__':
root.mainloop()

