from time import strftime
from tkinter import *
from datetime import datetime

def Loan():
    hp.destroy()
    import LoanPage


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = "Time:- "+string)
    lbl.after(1000, time)

hp = Tk()
hp.geometry("450x400")
hp.maxsize(450,400)
hp.configure(bg='midnight blue')
hp.title("HOMEPAGE/IVS")

bal_var = StringVar()

f1 = Frame(hp, bg='gold', borderwidth=8, relief=SUNKEN)
f1.pack(side=TOP, fill="x")
# Shop's Name
l1 = Label(f1, text=f"", bg='midnight blue', fg='gold', font="Helvetica 10 bold", padx=10)
l1.pack(fill="x")

lbl = Label(hp,bg='midnight blue',fg='gold',font="Helvetica 13 bold")
lbl.place(x=290,y=40)
time()

lbl4 = Label(hp, text=f"Date:- {datetime.now():%a, %b %d %Y}", fg="gold", bg="midnight blue", font=("helvetica 13 bold"))
lbl4.place(x=4,y=42)
lbl3 = Label(hp,text="Total Balance:-",fg='gold',bg='midnight blue',font="Helvetica 12 bold")
lbl3.place(x=47,y=160)

Bal_entry = Entry(hp,borderwidth=4,relief=SUNKEN,textvariable=bal_var,width=25,bg='gold')
Bal_entry.place(x=170,y=160)

b1 = Button(hp,bg='gold',fg='black',text="DATA ENTRY",borderwidth=5,font="Helvetica 10 bold")
b1.place(x=170,y=200)
b2 = Button(hp,bg='gold',fg='black',text="LOAN",borderwidth=5,font="Helvetica 10 bold",command=Loan)
b2.place(x=278,y=200)


hp.mainloop()