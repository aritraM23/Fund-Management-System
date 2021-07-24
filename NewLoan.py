import tkinter.messagebox
from tkinter import *
import math
import pyrebase
import mysql.connector

root = Tk()
root.config(bg='midnight blue')
root.geometry("580x470+500+130")
root.maxsize(580, 470)
root.minsize(580, 470)
root.title("NewLoan Page")

Top_Frame = Frame(root, borderwidth=6, bg='gold', relief=RAISED)
Top_Frame.pack(fill=X)
Top_Label = Label(Top_Frame, text="---New Loan Data Entry---", bg='gold', font="Helvetica 14 bold")
Top_Label.pack()
# ----------------------------------configs------------------------------------------------#
firebaseConfig = {'apiKey': "AIzaSyDR-a5PGjXpXFjvJVS9Ep3FOKXnNy9BsZg",
                  'authDomain': "fundmang-42ad8.firebaseapp.com",
                  'projectId': "fundmang-42ad8",
                  'storageBucket': "fundmang-42ad8.appspot.com",
                  'messagingSenderId': "361815074904",
                  'databaseURL': 'https://fundmang-42ad8-default-rtdb.firebaseio.com',
                  'appId': "1:361815074904:web:8504dfd52dbde0b186422d",
                  'measurementId': "G-MVMXL8CJNK"
                  }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# -----------------------------------All labels----------------------------------------#
name = Label(root, text="Name:", font="Helvetica 12 bold", bg="midnight blue", fg='gold')
mobile = Label(root, text="Mobile No.:", font="Helvetica 12 bold", bg="midnight blue", fg='gold')
address = Label(root, text="Address:", font="Helvetica 12 bold", bg="midnight blue", fg='gold')
shop = Label(root, text="Shop Name:", font="Helvetica 12 bold", bg="midnight blue", fg='gold')
date = Label(root, text="Date(DD/MM/YYYY):", font="Helvetica 12 bold", bg="midnight blue", fg='gold')
principal = Label(root, text="Principal taken:", font="Helvetica 12 bold", bg="midnight blue", fg='gold')
interest = Label(root, text="Interest:", font="Helvetica 12 bold", bg="midnight blue", fg='gold')

name.place(x=145, y=80)
mobile.place(x=110, y=120)
address.place(x=125, y=160)
shop.place(x=102, y=200)
date.place(x=50, y=240)
principal.place(x=80, y=280)
interest.place(x=135, y=320)


# ------------------------FUNCTIONS-----------------------------#

def add_data():
    name = name_entry.get()
    mobileNumber = mobile_entry.get()
    address = address_entry.get()
    shopName = shop_entry.get()
    date = date_entry.get()
    principalAmount = principal_entry.get()
    interestPercent = interest_entry.get()
    principlePaid = 0
    interestPaid = 0
    principalLeft = principalAmount
    interestLeft = (int(principalAmount) * int(interestPercent)) / 100
    interestPaidTillDate = 0
    updatedLoanDate = date

    try:
        if (name != '' and mobileNumber != '' and principalAmount != '' and interestPercent != ''):
            datas = {'name': name, 'mobileNumber': mobileNumber, 'address': address, 'shopName': shopName, 'date': date,
                     'principalAmount': principalAmount,
                     'interestPercent': interestPercent, 'priciplePaid': principlePaid, 'interestPaid': interestPaid,
                     'principalLeft': principalLeft, 'interestLeft': interestLeft,  'interestPaidTillDate' : interestPaidTillDate, 'lastPaidDate':updatedLoanDate}
            db.child('loanData').push(datas)

            myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
                                                 database='ivsLoan')
            mycursor = myDataBase.cursor()
            dataCollection = 'Insert into loanentry (name ,mobileNumber ,address ,shopName ,date ,pricipalAmount ,interestPercent ,principlePaid ,interestPaid, principleLeft , interestLeft, interestPaidTillDate,dateGiven) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            datas = [(name, mobileNumber, address, shopName, date, principalAmount, interestPercent, principlePaid,
                      interestPaid, principalLeft, interestLeft, interestPaidTillDate,updatedLoanDate)]

            mycursor.executemany(dataCollection, datas)
            myDataBase.commit()
            myDataBase.close()
            tkinter.messagebox.showinfo('Success', f'{name} loan information is saved securely')
    except:
        tkinter.messagebox.showinfo('Offline',
                                    'You are offline your data will be saved offline. Later please Sync Up to sync the databases')
        myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
                                             database='ivsLoan')
        mycursor = myDataBase.cursor()
        dataCollection = 'Insert into loanEntry (name ,mobileNumber ,address ,shopName ,date ,pricipalAmount ,interestPercent ,principlePaid ,interestPaid, principleLeft , interestLeft, InterestPaidTillDate, dateGiven) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        datas = [(name, mobileNumber, address, shopName, date, principalAmount, interestPercent, principlePaid,
                  interestPaid, interestPaidTillDate,updatedLoanDate)]

        mycursor.executemany(dataCollection, datas)
        myDataBase.commit()
        myDataBase.close()
        tkinter.messagebox.showinfo('Success', f'{name} loan information is saved offline. Please sync database later')


# -------------------Entry Fields----------------------#
name_entry = Entry(root, borderwidth=4, relief=SUNKEN, font="Arial 11 bold", width=30)
mobile_entry = Entry(root, borderwidth=4, relief=SUNKEN, font="Arial 11 bold", width=30)
address_entry = Entry(root, borderwidth=4, relief=SUNKEN, font="Arial 11 bold", width=30)
shop_entry = Entry(root, borderwidth=4, relief=SUNKEN, font="Arial 11 bold", width=30)
date_entry = Entry(root, borderwidth=4, relief=SUNKEN, font="Arial 11 bold", width=30)
principal_entry = Entry(root, borderwidth=4, relief=SUNKEN, font="Arial 11 bold", width=30)
interest_entry = Entry(root, borderwidth=4, relief=SUNKEN, font="Arial 11 bold", width=30)

name_entry.place(x=215, y=80)
mobile_entry.place(x=215, y=120)
address_entry.place(x=215, y=160)
shop_entry.place(x=215, y=200)
date_entry.place(x=215, y=240)
principal_entry.place(x=215, y=280)
interest_entry.place(x=215, y=320)
# -------------------------------------------------------------------------#
# --------------------------------Button-----------------------------------#
add_btn = Button(root, text="Add", font="Arial 12 bold", bg="gold", fg="black", command=add_data)
add_btn.place(x=270, y=370)
root.mainloop()
