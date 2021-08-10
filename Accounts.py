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
import mysql.connector
from envVar import firebaseConfig as fc
from envVar import mycursor, myDataBase
from PIL.ImageTk import PhotoImage

firebase = pyrebase.initialize_app(fc)
db = firebase.database()


class gui:
	
	def __init__(self, root):
		self.root = root
		titlespace = " "
		self.root.title(100 * titlespace + "Money Management System")
		self.root.geometry("883x750+330+0")
		self.root.maxsize(883, 750)
		p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
		self.root.iconphoto(FALSE, p1)
		
		# clock function for live clock
		QName = StringVar()
		self.sumDep = 0
		
		def times():
			current_time = time.strftime("%I:%M:%S")
			self.clock.config(text=current_time)
			self.clock.after(200, times)
		
		self.btnState = False
		
		def switch():
			global btnState
			if self.btnState is True:
				for x in range(300):
					self.navRoot.place(x=-x, y=0)
					TitleFrame.update()
				
				self.btnState = False
			
			else:
				
				for x in range(-300, 0):
					self.navRoot.place(x=x, y=0)
					TitleFrame.update()
				
				self.btnState = True
		
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
				self.sumDep = 0
				totalData = db.child('registerUserExp').child(name).get()
				
				for data in totalData.each():
					self.sumDep += int(data.val()['amount'])
				
				self.deposit.config(text=str(self.sumDep))
			
			# return sumDep
			
			self.ind = Toplevel(root)
			self.ind.geometry("578x340+330+0")
			self.ind.title(50 * titlespace + "Money Management System")
			# self.ind.maxsize("570x250")
			# self.ind.resizable(False)
			
			mainFrame = Frame(self.ind, bd=10, width=500, height=370, relief=RIDGE, bg='black')
			mainFrame.grid()
			
			# self.labelMain = Label(self.ind, bd=7, width=500, height=400, bg='black')
			# self.labelMain.grid(row = 0, column = 0)
			topFrame = Frame(mainFrame, bd=10, width=500, height=370, relief=RIDGE, bg='black')
			topFrame.grid(row=1, column=0)
			
			indtitleFrame = Frame(mainFrame, bd=10, width=500, height=70, bg='black')
			indtitleFrame.grid(row=0, column=0)
			
			self.indtitle = Label(indtitleFrame, font=('Arial', 18, 'bold'), fg='pink',
								  text="Import Individual Data by Name:", bd=7, bg='black')
			self.indtitle.grid(row=0, column=1, padx=70)
			
			self.indEntry = Entry(topFrame, font=('arial', 13, 'bold'), bd=13, width=50, justify='left',
								  textvariable=QName)
			self.indEntry.grid(row=0, column=0, padx=5)
			
			Label(topFrame, font=('Arial', 18, 'bold'), text=" ", bd=3, bg='black').grid(row=1, column=0,
																						 padx=70)
			
			Button(topFrame, font=('arial', 13, 'bold'), text="IMPORT", bd=5, padx=10, pady=1, width=5, height=2,
				   bg='pink', command=s_byname).grid(row=2, column=0, padx=1)
			
			self.output = Label(topFrame, font=('arial', 13, 'bold'), bd=13, width=50, justify='left',
								bg='black', fg='pink', text="Total Output:")
			self.output.grid(row=3, column=0, padx=5)
			
			self.deposit = Label(topFrame, font=('arial', 13, 'bold'), bd=13, width=50, justify='left',
								 bg='black', fg='pink', text=str(self.sumDep))
			self.deposit.grid(row=4, column=0, padx=5)
		
		# self.root.maxsize(460,350)
		# self.root.destroy()
		# import indiv
		# self.root.destroy()
		# indiv.gui(tkinter.Tk())
		
		def about():
			pass
		
		def back():
			self.root.destroy()
			import Homepage
		
		###################################################################################################################################
		MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg='black')
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
		
		self.lbltitle = Label(TitleFrame, font=('Arial', 33, 'bold'), fg='pink', text="Money Management System", bd=7,
							  bg='black')
		self.lbltitle.grid(row=0, column=1, padx=70)
		
		SerialNumber = StringVar()
		Name = StringVar()
		Amount = StringVar()
		Date = StringVar()
		
		# ===============================================================================================================================================================================================
		
		def updateText(data):
			# update the drop down list
			# Clear the listbox
			try:
				self.my_list.delete(0, END)
				
				# Add toppings to listbox
				for item in data:
					self.my_list.insert(END, item)
			except:
				pass
		def fillout(event):
			# Delete whatever is in the entry box
			try:
				self.entName.delete(0, END)
				
				# Add clicked list item to entry box
				self.entName.insert(0, self.my_list.get(ANCHOR))
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
		
		self.lblserial = Label(LeftFrame1, font=('arial', 13, 'bold'), text='Serial Number', bd=13, bg='pink')
		self.lblserial.grid(row=1, column=0, sticky=W, padx=2)
		
		self.entserial = Entry(LeftFrame1, font=('arial', 13, 'bold'), bd=6, width=50, justify='left',
							   textvariable=SerialNumber)
		self.entserial.grid(row=1, column=1, sticky=W, padx=2)
		
		self.lblname = Label(LeftFrame1, font=('arial', 13, 'bold'), text='Name', bd=13, bg='pink')
		self.lblname.grid(row=2, column=0, sticky=W, padx=2)
		
		self.entName = Entry(LeftFrame1, font=('arial', 13, 'bold'), bd=6, width=50, justify='left', textvariable=Name)
		self.entName.grid(row=2, column=1, sticky=W, padx=2)
		
		self.my_list = Listbox(LeftFrame1, font=('arial', 13, 'bold'), height=3, width=51, justify='left')
		self.my_list.grid(row=3, column=1, sticky=W, padx=2)
		
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
		# self.entName['values'] = listVal
		# self.entName.current()
		listVal = getNameList()
		
		# Add the toppings to our list
		updateText(listVal)
		
		# Create a binding on the listbox onclick
		self.my_list.bind("<<ListboxSelect>>", fillout)
		
		# Create a binding on the entry box
		self.entName.bind("<KeyRelease>", check)
		
		# self.entname = Entry(LeftFrame1, font=('arial', 13, 'bold'), bd=6, width=50, justify='left', textvariable=Name)
		# self.entname.grid(row=2, column=1, sticky=W, padx=2)
		
		self.lblamount = Label(LeftFrame1, font=('arial', 13, 'bold'), text='Amount', bd=13, bg='pink')
		self.lblamount.grid(row=4, column=0, sticky=W, padx=2)
		
		self.entamount = Entry(LeftFrame1, font=('arial', 13, 'bold'), bd=6, width=50, justify='left',
							   textvariable=Amount)
		self.entamount.grid(row=4, column=1, sticky=W, padx=2)
		
		self.lblDate = Label(LeftFrame1, font=('arial', 13, 'bold'), text='Date', bd=13, bg='pink')
		self.lblDate.grid(row=5, column=0, sticky=W, padx=2)
		
		self.entDate = Entry(LeftFrame1, font=('arial', 13, 'bold'), bd=6, width=50, justify='left', textvariable=Date)
		self.entDate.grid(row=5, column=1, sticky=W, padx=2)
		
		# label for clock display
		self.clock = Label(TitleFrame, font=("times", 15, "bold"), bg="black", fg='pink')
		self.clock.grid(row=0, column=2, padx=0, pady=0)
		times()
		# ===============================================================================================================================================================================================
		
		# nav bar
		self.navIcon = PhotoImage(file='navbar.png')
		self.closeIcon = PhotoImage(file='exit.png')
		
		self.nvbarbtn = Button(TitleFrame, image=self.navIcon, width=24, height=24, bd=0, padx=1, command=switch).grid(
			row=0, column=0, padx=0, pady=0)
		self.navRoot = Frame(root, bg='pink', height=500, width=200)
		self.navRoot.place(x=-300, y=0)
		
		Label(self.navRoot, text="Menu", font='arial 10 bold', bg='black', fg='pink', height=3, width=200,
			  padx=0).place(x=0, y=0)
		
		self.y = 80
		
		self.options = ["Export All", "Import Individual", "About"]
		self.methods = [export, ind_import, about, back]
		
		self.navExp = Button(self.navRoot, text="Export All", font="arial 13", bg="pink", fg='black',
							 activebackground="pink", activeforeground="black", bd=0, command=export).place(x=25,
																											y=self.y)
		self.y += 40
		
		self.navInd = Button(self.navRoot, text="Import Individual", font="arial 13", bg="pink", fg='black',
							 activebackground="pink", activeforeground="black", bd=0, command=ind_import).place(x=25,
																												y=self.y)
		self.y += 40
		
		self.navAbt = Button(self.navRoot, text="Back", font="arial 13", bg="pink", fg='black',
							 activebackground="pink", activeforeground="black", bd=0, command=back).place(x=25,
																										  y=self.y)
		
		self.closeBtn = Button(self.navRoot, image=self.closeIcon, width=22, height=22, relief=RIDGE, bd=0, padx=1,
							   command=switch)
		self.closeBtn.place(x=150, y=20)
		
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
					datas = {'Serial Number': serialNumber, 'name': name, 'amount': amount, 'date': date}
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
					
					# 
					# print('Yes or no')
					# q=input('')
					# if q =='y':
					# 	displayNameWise(name)
					# else:
					# 	alertMssg('Chadarmod','Fuk Off')
					display()
					reset()
				else:
					reset()
					tkinter.messagebox.showerror('Error', 'Insert Data In All Fields')
				
			except:
				
				dataCollection = 'Insert into dataEntry (serialNumber,name,amount,date) values (%s,%s,%s,%s)'
				datas = [(serialNumber, name, amount, date)]
				
				mycursor.executemany(dataCollection, datas)
				myDataBase.commit()
				myDataBase.close()
				display()
				reset()
		
		def update():
			try:
				self.tempData = 0
				totalMainData = db.child('mainData').get()
				totalIndividualData = db.child('registerUserExp').child(Name.get()).get()
				for data in totalMainData.each():
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
						
						if data.val()['name'] == Name.get() and data.val()['date'] == date:
							db.child('mainData').child(data.key()).update(
								{'Serial Number': SerialNumber.get(), 'name': Name.get(), 'amount': Amount.get(),
								 'date': date})
							db.child('registerUserExp').child(Name.get()).child(indi.key()).update(
								{'Serial Number': SerialNumber.get(),
								 'name': Name.get(),
								 'amount': Amount.get(),
								 'date': date})
							myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
																 database='ivs2')
							mycursor = myDataBase.cursor()
							
							mycursor.execute(
								'update dataEntry set amount=%s,name=%s,date=%s,serialNumber = "%s"', (
									Amount.get(),
									Name.get(),
									Date.get(),
									SerialNumber.get()
								))
							myDataBase.commit()
							myDataBase.close()
							self.tempData += 1
				
				if self.tempData > 0:
					succesMsg('Update Info', 'Data Updated' )
				else:
					alertMssg('Update Info', 'Problem Not Updated')
			
			except:
				self.tempData = 0
				mycursor.execute(
					'update dataEntry set amount=%s,name=%s,date=%s ,serialNumber = %s', (
						Amount.get(),
						Name.get(),
						Date.get(),
						SerialNumber.get()
					))
				myDataBase.commit()
				myDataBase.close()
				self.tempData += 1
				if self.tempData > 0:
					succesMsg('Update Info', 'Data Updated')
				else:
					alertMssg('Update Info', 'Problem Not Updated')
		
		def search():
			self.sum = 0
			self.callAll = 'all'
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
				write.writerow(["Name", "Amount", "Date", "Loan"])
				file.close()
			for data in totalData.each():
				for ld in loanDB.each():
					if ('all' == Name.get().lower()):
						with open('FullFile.csv', 'w') as file:
							write = csv.writer(file)
							write.writerow(["Name", "Amount", "Date", "Loan"])
							file.close()
						totalData = db.child('mainData').get()
						loanDB = db.child('loanData').get()
						for data, ld in totalData.each():
							for ld in loanDB.each():
								with open('FullFile.csv', 'a') as files:
									write = csv.writer(files)
									if ld.val()['name'] == data.val()['name']:
										write.writerow([data.val()['name'], data.val()['amount'], data.val()['date'],
														ld.val()['principalAmount']])
										files.close()
									else:
										write.writerow(
											[data.val()['name'], data.val()['amount'], data.val()['date'], 'N/A'])
										files.close()
						os.system('FullFile.csv')
						return 0
					elif (data.val()['date'] == date or data.val()['name'] == Name.get() or data.val()[
						'amount'] == Amount.get()):
						with open('data.csv', 'a') as files:
							write = csv.writer(files)
							if ld.val()['name'] == data.val()['name']:
								write.writerow(
									[data.val()['name'], data.val()['amount'], data.val()['date'],
									 ld.val()['principalAmount']])
								files.close()
							else:
								write.writerow([data.val()['name'], data.val()['amount'], data.val()['date'], 'N/A'])
								files.close()
							self.sum += 1
			
			if self.sum > 0:
				os.system('data.csv')
			
			if self.sum == 0:
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
			mycursor.execute("select * from dataEntry")
			result = mycursor.fetchall()
			if len(result) != 0:
				self.display_data.delete(*self.display_data.get_children())
				for row in result:
					self.display_data.insert('', END, values=row)
			myDataBase.commit()
			myDataBase.close()
		
		
		def delete():
			
			try:
				print(SerialNumber.get())
				self.deleteData = 0
				totalIndividualData = db.child('registerUserExp').child(Name.get()).get()
			
				
				for data in totalIndividualData.each():
					if data.val()['name'] == Name.get() and data.val()['date'] == Date.get():
						db.child('registerUserExp').child(Name.get()).child(data.key()).remove()
						self.deleteData += 1
				allUserDataBase = db.child('mainData').get()
				for datas in allUserDataBase.each():
					if datas.val()['name'] == Name.get() and datas.val()['date'] == Date.get():
						print(datas.val()['name'])
						db.child('mainData').child(datas.key()).remove()
						self.deleteData += 1
				myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs2')
				mycursor = myDataBase.cursor()
				
				mycursor.execute("delete from dataEntry where serialnumber=%s", (
					SerialNumber.get()
				))
				self.deleteData += 1
				myDataBase.commit()
				myDataBase.close()
				self.deleteData += 1
				if self.deleteData == 3:
					succesMsg('Delete Info','Delete Success')
				if (self.deleteData <= 3):
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
					self.deleteData += 1
					succesMsg('Delete Info','Delete Success')
				except Exception as e:
					print(e)
					print(SerialNumber.get())
					alertMssg('Delete Info',e)
		
		def TrainInfo(ev):
			viewInfo = self.display_data.focus()
			learnData = self.display_data.item(viewInfo)
			row = learnData['values']
			SerialNumber.set(row[0])
			Name.set(row[1])
			Amount.set(row[2])
			Date.set(row[3])
		
		def reset():
			self.entserial.delete(0, END)
			self.entName.delete(0, END)
			self.entamount.delete(0, END)
			self.entDate.delete(0, END)
		
		def sync_on():

			try:
				totalData = db.child('mainData').get()
				
				mycursor.execute('Delete From dataEntry')
				for data in totalData.each():
					dataCollection = 'Insert into dataEntry (serialNumber,name,amount,date) values (%s,%s,%s,%s)'
					datas = [(data.val()['Serial Number'],data.val()['name'], data.val()['amount'], data.val()['date'])]
					mycursor.executemany(dataCollection, datas)
					myDataBase.commit()
				myDataBase.close()
				succesMsg('Sync Info','Data Synced')
			except Exception as e:
				
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
		self.display_data = ttk.Treeview(LeftFrame, height=18, columns=('Serial Number', 'Name', 'Amount', 'Date'),
										 yscrollcommand=y_scroll.set)
		y_scroll.pack(side=RIGHT, fill=Y)
		
		self.display_data.heading("Serial Number", text="Serial Number")
		self.display_data.heading("Name", text="NAME")
		self.display_data.heading("Amount", text="AMOUNT")
		self.display_data.heading("Date", text="DATE")
		
		self.display_data['show'] = 'headings'
		
		self.display_data.column("Serial Number", width=80)
		self.display_data.column("Name", width=80)
		self.display_data.column("Amount", width=80)
		self.display_data.column("Date", width=80)
		
		self.display_data.pack(fill=BOTH, expand=1)
		self.display_data.bind("<ButtonRelease-1>", TrainInfo)
		display()
		
		# ==============================================================================================================================================================================================
		
		self.btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="SYNC DOWN", bd=7, padx=18, pady=1,
								width=7, height=3, bg='pink', command=sync_off).grid(row=7, column=0, padx=1)
		self.btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="UPDATE", bd=7, padx=18, pady=1, width=7,
								height=3, bg='pink', command=update).grid(row=2, column=0, padx=1)
		self.btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="SAVE", bd=7, padx=18, pady=1, width=7,
								height=3, bg='pink', command=saveData).grid(row=1, column=0, padx=1)
		self.btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="DELETE", bd=7, padx=18, pady=1, width=7,
								height=3, bg='pink', command=delete).grid(row=5, column=0, padx=1)
		self.btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="SEARCH", bd=7, padx=18, pady=1, width=7,
								height=3, bg='pink', command=search).grid(row=4, column=0, padx=1)
		self.btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="DISPLAY", bd=7, padx=18, pady=1,
								width=7, height=3, bg='pink', command=display).grid(row=3, column=0, padx=1)
		self.btnAddNew = Button(RightFrame1a, font=('arial', 13, 'bold'), text="SYNC UP", bd=7, padx=18, pady=1,
								width=7, height=3, bg='pink', command=sync_on).grid(row=6, column=0, padx=1)


# ================================================================================================================================================================================================

# Main:

# if __name__ == '__main__':


root = tkinter.Tk()
application = gui(root)
root.mainloop()
