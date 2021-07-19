from tkinter import*

root = Tk()
root.geometry("550x450+600+90")
root.maxsize(550, 450)
root.minsize(550, 450)
root.configure(bg='midnight blue')
root.title("Loan Window")


def depo():
    root.destroy()
    import LoanExisting


def Loan():
    root.destroy()
    import RegisterCustomer


def bal():
    bal_lab=Label(root,bg='midnight blue', fg='gold',
                   font="Helvetica 12 bold", text="Balance:-")
    bal_lab.place(x=80,y=238)
    download=Button(root,text="Download Balance Sheet", bg='gold', fg='black',
                       font="Helvetica 11 bold",borderwidth=2, relief=SUNKEN, command=None)
    download.place(x=240,y=235)
    newLoan=Button(root,text="New Loan", bg='gold', fg='black',
                       font="Helvetica 11 bold",borderwidth=2, relief=SUNKEN, command=Loan)
    newLoan.place(x=120,y=295)
    deposit=Button(root,text="Deposit on Existing Loan", bg='gold', fg='black',
                       font="Helvetica 11 bold",borderwidth=2, relief=SUNKEN, command=depo)
    deposit.place(x=247,y=295)

top_frame=Frame(root, bg='gold', borderwidth=10,
           relief=RAISED, width=500, height=55)
top_frame.pack(side=TOP, fill=X)

heading=Label(top_frame,bg='gold',fg='black',font="Arial 12 bold",text="---Loan Window---")
heading.pack()

name_lab=Label(root, bg='midnight blue', fg='gold',
                   font="Helvetica 12 bold", text="Name:-")
name_lab.place(x=120,y=100)
name_entry=StringVar()
name = Entry(root, width=27, textvariable=name_entry,
             borderwidth=5, relief=SUNKEN, font="Helvetica 11 bold")
name.place(x=200,y=98)

mob_lab=Label(root, bg='midnight blue', fg='gold',
                   font="Helvetica 12 bold", text="Mobile No.:-")
mob_lab.place(x=90,y=140)
mob_entry=StringVar()
mob = Entry(root, width=27, textvariable=mob_entry,
             borderwidth=5, relief=SUNKEN, font="Helvetica 11 bold")
mob.place(x=200,y=138)

Check=Button(root,text="Check",bg='gold',font="Helvetica 11 bold",borderwidth=4,relief=RAISED,command=bal)
Check.place(x=245,y=185)

root.mainloop()