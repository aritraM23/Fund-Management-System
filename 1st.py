from tkinter import *
field1 = 'Shop Name', 'Proprietor', 'Address', 'Mobile Number'
field2 = 'Time','Date','Total Balance'
field3 = 'Username','Password','Confirm Password'
def reg2():
    reg=Toplevel(root)
    reg.geometry("450x400")
    reg.configure(bg='midnight blue')
    reg.title("Registration Page")
    fr1 = Frame(reg, bg='gold', borderwidth=4, relief=SUNKEN)
    fr1.pack(side=TOP, fill="x")
    lab1 = Label(fr1, text="PLEASE FILL THE BELOW DETAILS", bg='gold', fg='black', font="Helvetica 11 bold")
    lab1.pack(pady=4, fill="x")

    ents = makeform(reg, field1)
    fr3 = Frame(reg, bg='midnight blue')
    fr3.pack(side=TOP)
    b1 = Button(fr3, text='Submit', bg='gold', fg='black', font="Helvetica 10 bold")
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(fr3, text='Quit', bg='gold', fg='black', command=reg.quit, font="Helvetica 10 bold")
    b2.pack(side=LEFT, padx=5, pady=5)

def Register():
    reg=Toplevel(root)
    reg.geometry("450x400")
    reg.configure(bg='midnight blue')
    reg.title("Registration Page")
    fr1 = Frame(reg, bg='gold', borderwidth=4, relief=SUNKEN)
    fr1.pack(side=TOP, fill="x")
    lab1 = Label(fr1, text="PLEASE FILL THE BELOW DETAILS", bg='gold', fg='black', font="Helvetica 11 bold")
    lab1.pack( fill="x")

    ents = makeform(reg, field3)
    fr3 = Frame(reg, bg='midnight blue')
    fr3.pack(side=TOP)
    b1 = Button(fr3, text='Register', bg='gold', fg='black', font="Helvetica 10 bold", command=Register)
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(fr3, text='Quit', bg='gold', fg='black', command=reg.quit, font="Helvetica 10 bold")
    b2.pack(side=LEFT, padx=5, pady=5)

def Homepage():
    hp=Toplevel(root)
    hp.geometry("450x400")
    hp.configure(bg='midnight blue')
    hp.title("HOMEPAGE/IVS")
    Shopname=username_verify.get()
    f1=Frame(hp,bg='gold',borderwidth=8,relief=SUNKEN)
    f1.pack(side=TOP,fill="x")
    l1=Label(f1,text=f"{Shopname}",bg='midnight blue',fg='gold',font="Helvetica 14 bold",padx=10)
    l1.pack(fill="x")
    ntry=makeform(hp,field2)
    fr3 = Frame(hp,bg='midnight blue')
    fr3.pack(side=TOP)
    b1 = Button(fr3, text='Data Entry',bg='gold',fg='black',font="Helvetica 10 bold")
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(fr3, text='Loan',bg='gold',fg='black',font="Helvetica 10 bold")
    b2.pack(side=LEFT, padx=5, pady=5)

def fetch(entries: object):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text))

def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor='w', font="Helvetica 10 bold",bg='midnight blue',fg='gold')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT,fill="x")
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries

def Signup():
    Signup_screen = Toplevel(root)
    Signup_screen.configure(bg='midnight blue')
    Signup_screen.title("SignUp")
    Signup_screen.geometry("600x500")
    fr1 = Frame(Signup_screen, bg='gold', borderwidth=4, relief=SUNKEN)
    fr1.pack(side=TOP, fill="x")
    lab1 = Label(fr1, text="PLEASE FILL THE BELOW DETAILS", bg='gold', fg='black', font="Arial 10 bold")
    lab1.pack(pady=4, fill="x")

    ents = makeform(Signup_screen, field3)
    fr3 = Frame(Signup_screen,bg='midnight blue')
    fr3.pack(side=TOP)
    b1 = Button(fr3, text='Register',bg='gold',fg='black',font="Helvetica 10 bold",command=reg2)
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(fr3, text='Quit',bg='gold',fg='black', command=Signup_screen.quit,font="Helvetica 10 bold")
    b2.pack(side=LEFT, padx=5, pady=5)

if __name__ == '__main__':
    root = Tk()
    root.geometry("350x300")
    root.title("Login/Signup Page/IVS")
    root.configure(bg='midnight blue')
    f1 = Frame(root, bg='white', borderwidth=8, relief=RAISED)
    f1.pack(side=TOP, fill="x")
    l1 = Label(f1, text="--INVENTORY MANAGEMENT SYSTEM--", font="Helvetica 10 bold", fg='black', bg='gold').pack(fill="x")

    username_verify = StringVar()
    password_verify = StringVar()
    Label(root, text="Username:-", font="Helvetica 11 bold",bg='midnight blue',fg='gold').pack()
    username_login_entry = Entry(root, textvariable=username_verify, relief=SUNKEN, width=30)
    username_login_entry.pack()
    Label(root, text="",bg='midnight blue').pack()
    Label(root, text="Password:-", font="Helvetica 11 bold",bg='midnight blue',fg='gold').pack()
    password__login_entry = Entry(root, textvariable=password_verify, show='*', relief=SUNKEN, width=30)
    password__login_entry.pack()
    Label(root, text="",bg='midnight blue').pack()

    f2 = Frame(root,bg='midnight blue')
    f2.pack(side=TOP, padx=100)
    b1 = Button(f2, text="Login", fg='black', bg='gold', relief=SUNKEN, padx=4, command=Homepage,font="Helvetica 10 bold").pack(side=LEFT, padx=6)
    b2 = Button(f2, text="SignUp", fg='black', bg='gold', relief=SUNKEN,font="Helvetica 10 bold", command=Signup).pack(side=LEFT, padx=6)
    root.mainloop()
