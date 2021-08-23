import tkinter.messagebox
from tkinter import *
import math
import pyrebase
import mysql.connector
from PIL.ImageTk import PhotoImage
from envVar import firebaseConfig as fc
# from envVar import mycursor,myDataBase

myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="mancunian@2002",database='ivsLoan')
mycursor = myDataBase.cursor()

root = Tk()
root.config(bg='midnight blue')
root.geometry("580x470+500+130")
root.maxsize(580, 470)
root.minsize(580, 470)
root.title("NewLoan Page")
p1 = PhotoImage(master=root,file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE, p1)


Top_Frame = Frame(root, borderwidth=6, bg='gold', relief=RAISED)
Top_Frame.pack(fill=X)
Top_Label = Label(Top_Frame, text="---New Loan Data Entry---", bg='gold', font="Helvetica 14 bold")
Top_Label.pack()
# ----------------------------------configs------------------------------------------------#

firebase = pyrebase.initialize_app(fc)
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
amount = 0

def treasure(pAmount):
    global amount
    interest = 0
    princi = 0
    totalDB = db.child('mainData').get()
    loanDb = db.child('loanData').get()
    for data in totalDB.each():
        amount += int(data.val()['amount'])

    print(amount)
    try:
        for ld in loanDb.each():
            interest += int(ld.val()['interestPaidTillDate'])
        amount += interest
        print(amount)
        for ld in loanDb.each():
            princi += int(ld.val()['principalLeft'])

        amount -= princi 
        # if(amount<=0):
        #     tkinter.messagebox.showerror('Balance Exhausted!!', "No Balance Left. Loan Can't be Provided!")
        #     amount += princi
        amount -= pAmount
        if(amount<=0):
            tkinter.messagebox.showerror("Insufficient Balance!!", "Loan Can't be Provided!")
            back()
            return 0
            

    except:
        amount -= pAmount
        if(amount<=0):
            tkinter.messagebox.showerror("Insufficient Balance!!", "Loan Can't be Provided!")
            back()
            return 0
            

    print(amount)
    # print(amount)
    return amount



def back():
    import _thread
    _thread.exit_thread()

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

    val = treasure(int(principalAmount))
    if(val==0):
        return 0
        
    try:
        if (name != '' and mobileNumber != '' and principalAmount != '' and interestPercent != ''):
            datas = {'name': name, 'mobileNumber': mobileNumber, 'address': address, 'shopName': shopName, 'date': date,
                     'principalAmount': principalAmount,
                     'interestPercent': interestPercent, 'priciplePaid': principlePaid, 'interestPaid': interestPaid,
                     'principalLeft': principalLeft, 'interestLeft': interestLeft,  'interestPaidTillDate' : interestPaidTillDate, 'lastPaidDate':updatedLoanDate}
            db.child('loanData').push(datas)

            myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="mancunian@2002",
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
        myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="mancunian@2002",
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

Back = Button(root, text="Back", bg='gold', font="Helvetica 11 bold", borderwidth=4, relief=RAISED, command=back)
Back.place(x=20, y=50)

root.mainloop()
