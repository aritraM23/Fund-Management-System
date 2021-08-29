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
root.state('zoomed')
root.config(bg="navy")
root.resizable(0,0)
root.title("Loan Window")
p1 = PhotoImage(master=root,file='[DIGICURE MAIN LOGO].png')
root.iconphoto(False,p1)


name_entry = StringVar()
mob_entry = StringVar()
import _thread
def back():
    _thread.exit_thread()
def displayLoan():
    _thread.start_new_thread(displayL, (1,3))
def displayL(j,k):
    import LoanTreeView

def new():
    _thread.start_new_thread(newLoanPage, (1,2))
def newLoanPage(l,a):
    import NewLoan
def depo():
    _thread.start_new_thread(newDepo, (11,2))
def newDepo(a,b):
    import Loan_RepayPage

def updateText(data):
    #update the drop down list
    # Clear the listbox
    try:
        my_list.delete(0, END)
    
        # Add toppings to listbox
        for item in data:
            my_list.insert(END, item)
    except :
        pass
def fillout(event):
    # Delete whatever is in the entry box
    try:
        name.delete(0, END)
    
        # Add clicked list item to entry box
        name.insert(0, my_list.get(ANCHOR))
    except :pass
def check(event):
    # grab what was typed
    try:
        typed = name_entry.get()
    
        if typed == '':
            data = listVal
        else:
            data = []
            for item in listVal:
                if typed.lower() in item.lower():
                    data.append(item)
    
        # update our listbox with selected items
        updateText(data)
    except :pass
    
def export():
    with open('LoanFile.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(
            ["Name", "Loan Amount", "Interest", "Principal Paid",
             "Interest Paid", "Principal left", "Interest left",
             "InterestPaidTotal","Date","Last Paid Date" ])
        file.close()
    totalData = db.child('loanData').get()
    for data in totalData.each():
        
        if data.val()['name'] == name_entry.get() or data.val()['mobileNumber'] == (mob_entry.get()):
            with open('LoanFile.csv', 'a') as files:
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
                balData = db.child('mainData').get()
                for var in balData.each():
                    if var.val()['name'] == name_entry.get():
                        balance += int(var.val()['amount'])
                    else:
                        balance += 0
                break
    except:
        tkinter.messagebox.showinfo("Search Mismatch", "No such Name in Directory!!")
    bal_lab = Label(mainFrame, fg='black', bg='DarkGoldenrod1', font="Orbitron-Bold 25 bold",
                    text="Balance:-" + " "+str(balance))
    bal_lab.place(x=92, y=440)
    download = Button(mainFrame, text="Download\n"
    "Balance Sheet", bg='DarkGoldenrod1', fg='black', font="Orbitron-bold 25 bold",
                      borderwidth=4, relief=SUNKEN, command=export)
    download.place(x=410, y=405)


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
top_frame = Frame(root, bg='DarkGoldenrod1', borderwidth=10, relief=RAISED,
                  width=500, height=55)
top_frame.pack(side=TOP, fill=X)
heading = Label(top_frame, bg='DarkGoldenrod1', fg='black',
                font="Orbitron-Bold 30 bold", text="--------Loan Window--------")
heading.pack()
#---------------------ENTRY STUFFS--------------------------#
mainFrame = Frame(root, bg='DarkGoldenrod1', borderwidth=8,
                  relief=SUNKEN, width=800, height=650)
mainFrame.place(x=207, y=125)
name_lab = Label(mainFrame, fg='black', bg='DarkGoldenrod1',
                 font="Constantia 28 bold", text="Name:-")
name_lab.place(x=75, y=94)
name = Entry(mainFrame, width=25, textvariable=name_entry,
             borderwidth=5, relief=SUNKEN,justify=CENTER, font="Consolas 27 bold")
name.place(x=240, y=94)
my_list = Listbox(mainFrame, font =('arial', 24, 'bold'),height = 3, width=28, justify='left')
my_list.place(x = 242, y=148)

listVal = []

def getNameList():
    listVal = []
    listname = db.child('loanData').get()
    try:
        for each in listname.each():
            listVal.append(each.val()['name'])
    
        listVal = list(set(listVal))
        return listVal
    except :
        pass
listVal = getNameList()

updateText(listVal)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
name.bind("<KeyRelease>", check)

mob_lab = Label(mainFrame, fg='black', bg='DarkGoldenrod1', font="Constantia 27 bold",
                justify=CENTER , text="Mobile No.:-")
mob_lab.place(x=15, y=290)
mob = Entry(mainFrame, width=25, textvariable=mob_entry,borderwidth=5, relief=SUNKEN, font="Consolas 27 bold")
mob.place(x=240, y=290)

#----Buttons Frame along with Buttons---------#
btn_frame = Frame(root,bg='DarkGoldenrod1',width= 800,height=800,borderwidth=3,relief=RAISED)
btn_frame.place(x=1140,y=170)
Check = Button(btn_frame, text="CHECK", bg='DarkGoldenrod1', font="Orbitron-bold 25 bold",
               width=10,borderwidth=4, relief=RAISED, command=bal)
Check.pack()
Display = Button(btn_frame, text="DISPLAY", bg='DarkGoldenrod1', font="Orbitron-bold 25 bold", borderwidth=4,
                 relief=RAISED, command=displayLoan,width=10)
Display.pack()
Back = Button(btn_frame, text="BACK", bg='DarkGoldenrod1', font="Orbitron-bold 25 bold",
              borderwidth=4, relief=RAISED, command=back,width=10)
Back.pack()
Sync_Up = Button(btn_frame, text="SYNC UP", bg='DarkGoldenrod1', font="Orbitron-bold 25 bold",
              borderwidth=4, relief=RAISED, command=sync_up,width=10)
Sync_Up.pack()
Sync_Down = Button(btn_frame, text="SYNC DOWN", bg='DarkGoldenrod1', font="Orbitron-bold 25 bold",
              borderwidth=4, relief=RAISED, command=sync_down,width=10)
Sync_Down.pack()
newLoan = Button(btn_frame, text="NEW LOAN", bg='DarkGoldenrod1', fg='black', font="Orbitron-bold 25 bold", borderwidth=4,
                     relief=RAISED, command=new,width=10)
newLoan.pack()
deposit = Button(btn_frame, text="DEPOSIT", bg='DarkGoldenrod1', fg='black', font="Orbitron-bold 25 bold",
                     borderwidth=4, relief=RAISED, command=depo,width=10)
deposit.pack()
#---------------------------------------------------------------------------------------------#
root.mainloop()
