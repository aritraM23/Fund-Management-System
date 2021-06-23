from time import strftime
from tkinter import *

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = "Time:- "+string)
    lbl.after(1000, time)

hp = Tk()
hp.geometry("450x400")
hp.maxsize(450,400)
hp.configure(bg='midnight blue')
hp.title("HOMEPAGE/IVS")

date_var = StringVar()
bal_var = StringVar()


f1 = Frame(hp, bg='gold', borderwidth=8, relief=SUNKEN)
f1.pack(side=TOP, fill="x")
l1 = Label(f1, text=f"", bg='midnight blue', fg='gold', font="Helvetica 10 bold", padx=10)
l1.pack(fill="x")

lbl = Label(hp,bg='midnight blue',fg='gold',font="Helvetica 13 bold")
lbl.place(x=290,y=40)
time()

lbl2 = Label(hp,text="Enter Date:-",fg='gold',bg='midnight blue',font="Helvetica 12 bold")
lbl2.place(x=70,y=120)
lbl3 = Label(hp,text="Total Balance:-",fg='gold',bg='midnight blue',font="Helvetica 12 bold")
lbl3.place(x=47,y=160)

Date_entry = Entry(hp,borderwidth=4,relief=SUNKEN,textvariable=date_var,width=25,bg='gold')
Bal_entry = Entry(hp,borderwidth=4,relief=SUNKEN,textvariable=bal_var,width=25,bg='gold')
Date_entry.place(x=170,y=120)
Bal_entry.place(x=170,y=160)

b1 = Button(hp,bg='gold',fg='black',text="DATA ENTRY",borderwidth=5,font="Helvetica 10 bold")
b1.place(x=120,y=200)
b2 = Button(hp,bg='gold',fg='black',text="LOAN",borderwidth=5,font="Helvetica 10 bold")
b2.place(x=235,y=200)


hp.mainloop()