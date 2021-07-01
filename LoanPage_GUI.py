from tkinter import *
import tkinter
from tkinter import ttk


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
        principal=Entry(f2,textvariable=p_entry,borderwidth=4,width=15,font="Arial 12 bold",relief=SUNKEN)
        principal.place(x=150,y=20)
        interest=Entry(f2,textvariable=int_entry,borderwidth=4,width=15,font="Arial 12 bold",relief=SUNKEN)
        interest.place(x=150,y=50)
        month=Entry(f2,textvariable=mnths_entry,borderwidth=4,width=15,font="Arial 12 bold",relief=SUNKEN)
        month.place(x=150,y=80)
        b2=Button(f2,text="Calculate",borderwidth=5,bg="midnight blue",
                    fg="gold",command=None,font="Helvetica 13 bold")
        b2.place(x=120,y=120)
        b3=Button(f2,text="Add",borderwidth=5,bg="midnight blue",fg="gold",command=None,font="Helvetica 13 bold")
        b3.place(x=90,y=170)
        b4=Button(f2,text="History",borderwidth=5,bg="midnight blue",fg="gold",command=None,font="Helvetica 13 bold")
        b4.place(x=160,y=170)
        treev = ttk.Treeview(f2, selectmode ='browse')
        treev.place(x=60,y=260)
        # verscrlbr=ttk.Scrollbar(f2,command=treev.yview)
        # verscrlbr.place(x=100,y=240)

if __name__=='__main__':
    root = tkinter.Tk()
    app = LoanPage(root)
    root.mainloop()
