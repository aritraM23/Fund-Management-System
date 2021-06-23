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

class loan:

    def __init__(self, root):

        self.root = root
        titlespace=" "
        self.root.title(100*titlespace+"Money Management System")
        self.root.geometry("900x750+330+0")
        self.root.maxsize(900,750)

        #clock function for live clock   
        def times():
            current_time=time.strftime("%H:%M:%S")
            self.clock.config(text=current_time)
            self.clock.after(200,times)

##################################################################################################################################
        
        MainFrame= Frame(self.root,bd=10,width=770,height=700,relief=RIDGE,bg='midnight blue')
        MainFrame.grid()

        TitleFrame= Frame(MainFrame,bd=7,width=770,height=100, bg='midnight blue')
        TitleFrame.grid(row=0,column=0)
        TopFrame3= Frame(MainFrame,bd=5,width=770,height=500, bg = 'gold')
        TopFrame3.grid(row=1,column=0)
        
        LeftFrame = Frame(TopFrame3, bd=5, width=350, height=500, padx=2,pady=0, bg='midnight blue')
        LeftFrame.pack(side=LEFT, expand = True, fill = 'both')
        LeftFrame1 = Frame(LeftFrame, bd=5, width=340, height=180, padx=2,pady=0, bg = 'gold' )
        LeftFrame1.pack(side=TOP, expand = True, fill = 'both')

        RightFrame = Frame(TopFrame3, bd=5, width=450, height=740, relief=RIDGE,padx=2, bg='midnight blue')
        RightFrame.pack(side=RIGHT,expand = True, fill = 'both')
        RightFrame1a = Frame(RightFrame, bd=5, width=430, height=700, padx=12,pady=4, bg = 'midnight blue' )
        RightFrame1a.pack(side=TOP, expand = True, fill = 'both')

        self.lbltitle=Label(TitleFrame, font=('Arial',33,'bold'), fg= 'gold', text="Loan Management System",bd=7, bg = 'midnight blue')
        self.lbltitle.grid(row=0,column=1,padx=70)

        #label for clock display
        self.clock=Label(TitleFrame,font=("times",15,"bold"),bg="midnight blue",fg='gold')
        self.clock.grid(row=0,column=0,padx=0, pady = 0)
        times()
##################################################################################################################################################################################
        Months = StringVar()
        AmountL = StringVar()
        Interest = StringVar()

        self.lblamount = Label(RightFrame1a, font =('arial',13,'bold'), text = 'Amount' , bd = 13 , bg= 'midnight blue', fg = 'gold')
        self.lblamount.grid(row = 0, column=0, sticky = W,padx = 4)

        self.entamount = Entry(RightFrame1a, font =('arial',13,'bold'), bd = 10 , width = 20, justify='left', textvariable = AmountL)
        self.entamount.grid(row = 0, column=1, sticky = W,padx = 4)
        
        self.lblroi = Label(RightFrame1a, font =('arial',13,'bold'), text = 'Rate of\nInterest' , bd = 13 ,bg= 'midnight blue', fg = 'gold' )
        self.lblroi.grid(row = 1, column=0, sticky = W,padx = 4)

        self.entroi = Entry(RightFrame1a, font =('arial',13,'bold'), bd = 10 , width = 20, justify='left', textvariable = Interest)
        self.entroi.grid(row = 1, column=1, sticky = W,padx = 4)

        self.lblmonth = Label(RightFrame1a, font =('arial',13,'bold'), text = 'Months' , bd = 13 ,bg= 'midnight blue', fg = 'gold')
        self.lblmonth.grid(row = 2, column=0, sticky = W,padx = 4)

        self.entmonth = Entry(RightFrame1a, font =('arial',13,'bold'), bd = 10 , width = 20, justify='left', textvariable = Months)
        self.entmonth.grid(row = 2, column=1, sticky = W,padx = 4)

##################################################################################################################################################################################
        
        Name = StringVar()
        Phone = StringVar()
        ShopName = StringVar()

        self.lblname = Label(LeftFrame1, font =('arial',13,'bold'), text = 'Name' , bd = 13 , bg = 'gold', fg = 'midnight blue')
        self.lblname.grid(row = 0, column=0, sticky = W,padx = 4)

        self.entname = Entry(LeftFrame1, font =('arial',13,'bold'), bd = 13 , width = 26, justify='left', textvariable = Name)
        self.entname.grid(row = 0, column=1, sticky = W,padx = 4)

        self.lblphone = Label(LeftFrame1, font =('arial',13,'bold'), text = 'Phone' , bd = 13 , bg = 'gold', fg = 'midnight blue')
        self.lblphone.grid(row = 1, column=0, sticky = W,padx = 4)

        self.entphone = Entry(LeftFrame1, font =('arial',13,'bold'), bd = 13 , width = 26, justify='left', textvariable = Phone)
        self.entphone.grid(row = 1, column=1, sticky = W,padx = 4)

        self.lblsn = Label(LeftFrame1, font =('arial',13,'bold'), text = 'Shop Name' , bd = 13 , bg = 'gold', fg = 'midnight blue')
        self.lblsn.grid(row = 2, column=0, sticky = W,padx = 4)

        self.entsn = Entry(LeftFrame1, font =('arial',13,'bold'), bd = 13 , width = 26, justify='left', textvariable = ShopName)
        self.entsn.grid(row = 2, column=1, sticky = W,padx = 4)

##################################################################################################################################################################################

        def addDataL():
            amount = AmountL.get()
            roi = Interest.get()
            months = Months.get()
            if(amount != '' and roi != '' and months != ''):
                datas = {'Amount': amount, 'ROI': roi, 'Months' : months}
                db.child('loanDemo').push(datas)

            else:
                tkinter.messagebox.showerror('Data insufficient!', ' Fill all entries to save!')

        def calculate():
            pass

        def display():
            pass

###################################################################################################################################################################################

        self.btnAddNew=Button(RightFrame1a,font=('arial', 10, 'bold'), text="ADD", bd=6, padx=10,pady=1,width=7,height=1, bg = 'gold',fg = 'midnight blue', command=addDataL).grid(row=0,column=2,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 10, 'bold'), text="CALCULATE", bd=6, padx=10,pady=1,width=7,height=1, bg = 'gold',fg = 'midnight blue', command=calculate).grid(row=1,column=2,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 10, 'bold'), text="DISPLAY", bd=6, padx=10,pady=1,width=7,height=1, bg = 'gold',fg = 'midnight blue', command=display).grid(row=2,column=2,padx=1)

###################################################################################################################################################################################

if __name__ == '__main__':
    root=tkinter.Tk()
    application = loan(root)
    root.mainloop()
