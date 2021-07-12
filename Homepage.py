from tkinter import*
from time import strftime
import datetime as dt

root = Tk()
root.geometry("550x450+600+90")
root.config(bg="midnight blue")
root.title("HomePage")
root.maxsize(550,450)
root.minsize(550,450)

def Time():
    string = strftime('%H:%M:%S %p')
    Time_Label.config(text=string)
    Time_Label.after(1000, Time)


Time_Label = Label(root, fg="black", bg="gold",
                   font="Devanagari 15 bold", borderwidth=4, relief=SUNKEN)
Time_Label.place(x=426, y=2)
Time()

def srch():
    balance=Label(root,fg='gold',bg='midnight blue',font="Devanagari 15 bold",text="Balance:-")
    balance.place(x=100,y=175)
    Loan=Label(root,fg='gold',bg='midnight blue',font="Devanagari 15 bold",text="Loan:-")
    Loan.place(x=320,y=175)

date = Label(root, text=f"{dt.datetime.now():%a, %b/%d/%Y}", bg="gold", fg="black", font=(
    "helvetica 15 bold"), borderwidth=4, relief=SUNKEN)
date.place(x=1, y=2)

name=StringVar()
name.set("Enter Customer Name Here")
customer_name=Entry(root,justify=CENTER,borderwidth=4,textvariable=name,font="Helvetica 12 bold",width=30)
customer_name.place(x=140,y=80)

Check=Button(root,text="Search",bg='gold',font="Helvetica 11 bold",borderwidth=4,relief=RAISED,command=srch)
Check.place(x=353,y=125)

accounts=Button(root,text="Accounts",bg='gold',font="Helvetica 11 bold",borderwidth=4,relief=SUNKEN)
accounts.place(x=180,y=240)
loan=Button(root,text="Loan",bg='gold',font="Helvetica 11 bold",borderwidth=4,relief=SUNKEN)
loan.place(x=320,y=240)

Treasury=Label(root,bg='gold',fg='black',font="Helvetica 13 bold",text="Treasury:-")
Treasury.place(x=70,y=350)

root.mainloop()
