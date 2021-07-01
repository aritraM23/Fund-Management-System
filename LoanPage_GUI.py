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
from pyasn1.type.univ import Null
import pyrebase

firebaseConfig = {'apiKey': "AIzaSyDR-a5PGjXpXFjvJVS9Ep3FOKXnNy9BsZg",
    'authDomain': "fundmang-42ad8.firebaseapp.com",
    'projectId': "fundmang-42ad8",
    'storageBucket': "fundmang-42ad8.appspot.com",
    'messagingSenderId': "361815074904",
    'databaseURL':'https://fundmang-42ad8-default-rtdb.firebaseio.com',
    'appId': "1:361815074904:web:8504dfd52dbde0b186422d",
    'measurementId': "G-MVMXL8CJNK"
}

firebase=pyrebase.initialize_app(firebaseConfig)
db= firebase.database()

class LoanPage:
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("Loan Page")
        self.root.configure(bg="midnight blue")
        self.root.geometry("850x600+550+70")

        def check():
            name_entry = StringVar()
            mob_entry = StringVar()
            f1 = Frame(root, width=430, height=440, bg="gold", borderwidth=6,relief=SUNKEN)
            f1.place(x=30, y=80)
            l1 = Label(f1, text="Name:-", fg="black",
                       font="Helvetica 14 bold", bg="gold")
            l1.place(x=30, y=10)
            name = Entry(f1, textvariable=name_entry,
                         borderwidth=4, width=28, font="arial 12 bold",relief=SUNKEN)
            name.place(x=120, y=10)
            l2 = Label(f1, text="Mobile:-", fg="black",
                       font="Helvetica 14 bold", bg="gold")
            l2.place(x=30, y=50)
            mob = Entry(f1, textvariable=mob_entry, borderwidth=4,
                        width=28, font="Arial 12 bold",relief=SUNKEN)
            mob.place(x=120, y=50)
            b1 = Button(f1, text="Check", borderwidth=5, bg="midnight blue",
                        fg="gold", command=check, font="Helvetica 13 bold")
            b1.place(x=165, y=90)
            l8 = Label(f1, text="Name:-", fg="black",
                       font="Helvetica 14 bold", bg="gold")
            l8.place(x=70, y=140)
            l9 = Label(f1, text="Mobile:-", fg="black",
                       font="Helvetica 14 bold", bg="gold")
            l9.place(x=65, y=180)
            l3 = Label(f1, text="Shop Name:-", fg="black",
                       font="Helvetica 14 bold", bg="gold")
            l3.place(x=22,y=220)
            l4 = Label(f1, text="Address:-", fg="black",
                       font="Helvetica 14 bold", bg="gold")
            l4.place(x=49,y=260)
            l5 = Label(f1, text="Total Deposit:-", fg="black",
                       font="Helvetica 14 bold", bg="gold")
            l5.place(x=6,y=300)
        

        name_entry = StringVar()
        mob_entry = StringVar()
        p_entry=StringVar()
        int_entry=StringVar()
        mnths_entry=StringVar()
        date = StringVar()

        f3=Frame(root,width=430,height=50,bg="gold",borderwidth=3,relief=SUNKEN)
        f3.place(x=30,y=13)
        l3=Label(f3,text="--LOAN MANAGEMENT SYSTEM--",font="Arial 15 bold",bg="gold")
        l3.place(x=45,y=10)
        f1 = Frame(root, width=430, height=440, bg="gold", borderwidth=6,relief=SUNKEN)
        f1.place(x=30, y=80)
        l1 = Label(f1, text="Name:-", fg="black",
                   font="Helvetica 14 bold", bg="gold")
        l1.place(x=30, y=10)
        name = Entry(f1, textvariable=name_entry, borderwidth=4,
                     width=28, font="arial 12 bold",relief=SUNKEN)
        name.place(x=120, y=10)
        l2 = Label(f1, text="Mobile:-", fg="black",
                   font="Helvetica 14 bold", bg="gold")
        l2.place(x=30, y=50)
        mob = Entry(f1, textvariable=mob_entry, borderwidth=4,
                    width=28, font="Arial 12 bold",relief=SUNKEN)
        mob.place(x=120, y=50)
        b1 = Button(f1, text="Check", borderwidth=5, bg="midnight blue",
                    fg="gold", command=check, font="Helvetica 13 bold")
        b1.place(x=165, y=90)
        f2=Frame(root,width=320,height=560,bg="gold",borderwidth=6,relief=SUNKEN)
        f2.place(x=500,y=20)
        l4 = Label(f2, text="Principal:-", fg="black",
                   font="Helvetica 14 bold", bg="gold")
        l4.place(x=20, y=20)
        l5 = Label(f2, text="Interest Rate:-", fg="black",
                   font="Helvetica 14 bold", bg="gold")
        l5.place(x=8, y=50)
        l6 = Label(f2, text="Month:-", fg="black",
                   font="Helvetica 14 bold", bg="gold")
        l6.place(x=35, y=80)

        def addDataL():
            name = name_entry.get()
            amount = p_entry.get()
            roi = int_entry.get()
            months = mnths_entry.get()
            date = date.get()
            if(name != '' and amount != '' and roi != '' and months != ''):
                datas = {'Name' : name,'Amount': amount, 'ROI': roi, 'Months' : months, 'Date' : date}
                db.child('loanDemo').push(datas)

            else:
                tkinter.messagebox.showerror('Data insufficient!', ' Fill all entries to save!')

        def calculate():

            Lname = name_entry.get()
            Ldate = date.get()[:2]
            tD = db.child('registerUserExp').get()
            lD = db.child('loanDemo').get()
            print(Ldate)

            if Lname!='' and Ldate=='':
                
                count = 0
                totalD = 0

                for data in tD.each():
                    if(Lname == data.key()):
                        # print(data.key())
                        # break
                        try:
                            td1 = db.child('registerUserExp').child(Lname).get()
                            for nm in td1.each():
                                if nm.val()['name']==Lname:
                                    count += 1
                                    totalD += int(nm.val()['amount'])
                                    
                            print(totalD)
                            print(count)
                            
                        except:
                            tkinter.messagebox.showerror('Error!', 'Search query not found!')

            elif Lname!='' and Ldate!='':
                try:    
                    for data in tD.each():
                        if(Lname == data.key()):
                            td1 = db.child('registerUserExp').child(Lname).get()
                            try:
                                for ln in td1.each():
                                    if ln.val()['name']==Name.get() and int(ln.val()['date'][:2])>=int(Ldate):
                                        print(ln.val()['date'][:2])

                            except:
                                print(ln.val()['date'][:2] + "except")
                                continue

                            #todo : month problem in date sorting
                except:
                    print("jate bojha jaye")

        principal=Entry(f2,textvariable=p_entry,borderwidth=4,width=15,font="Arial 12 bold",relief=SUNKEN)
        principal.place(x=150,y=20)
        interest=Entry(f2,textvariable=int_entry,borderwidth=4,width=15,font="Arial 12 bold",relief=SUNKEN)
        interest.place(x=150,y=50)
        month=Entry(f2,textvariable=mnths_entry,borderwidth=4,width=15,font="Arial 12 bold",relief=SUNKEN)
        month.place(x=150,y=80)
        b2=Button(f2,text="Calculate",borderwidth=5,bg="midnight blue",
                    fg="gold",command=calculate,font="Helvetica 13 bold")
        b2.place(x=120,y=120)
        b3=Button(f2,text="Add",borderwidth=5,bg="midnight blue",fg="gold",command=addDataL,font="Helvetica 13 bold")
        b3.place(x=90,y=170)
        b4=Button(f2,text="History",borderwidth=5,bg="midnight blue",fg="gold",command=None,font="Helvetica 13 bold")
        b4.place(x=160,y=170)
        treev = ttk.Treeview(f2, selectmode ='browse')
        treev.place(x=60,y=260)
        # verscrlbr=ttk.Scrollbar(f2,command=treev.yview)
        # verscrlbr.place(x=100,y=240)


root = tkinter.Tk()
app = LoanPage(root)
root.mainloop()
