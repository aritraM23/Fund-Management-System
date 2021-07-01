import tkinter.messagebox
from tkinter import *
from datetime import datetime
from time import strftime
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
root = Tk()
root.title("Management System")
root.configure(bg='midnight blue')
root.geometry("500x450+630+70")
root.maxsize(500,450)
root.minsize(500,450)
firebase=pyrebase.initialize_app(firebaseConfig)
db= firebase.database()


def signin(username,password):
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    name = username
    password = password
    auth.sign_in_with_email_and_password(name, password)

def account():
    import Accounts
    
def page1():
    def LoginPage():
        f1.destroy()
        l1.destroy()
        l2.destroy()
        l3.destroy()
        uname = username1.get()
        pwd = password1.get()
        try:
            signin(uname,pwd)
            username1.destroy()
            password1.destroy()
            b1.destroy()
            b2.destroy()

            def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text="Time:- " + string)
                lbl.after(1000, time)

            bal_var = StringVar()

            f9 = Frame(root, bg='gold', borderwidth=8, relief=SUNKEN)
            f9.pack(side=TOP, fill="x")
            l12 = Label(f9, text=f"", bg='midnight blue', fg='gold', font="Helvetica 10 bold", padx=10)
            l12.pack(fill="x")

            lbl = Label(root, bg='midnight blue', fg='gold', font="Helvetica 13 bold")
            lbl.place(x=338, y=43)
            time()

            lbl4 = Label(root, text=f"Date:- {datetime.now():%a, %b %d %Y}", fg="gold", bg="midnight blue",
                         font=("helvetica 13 bold"))
            lbl4.place(x=4, y=42)
            lbl3 = Label(root, text="Total Balance:-", fg='gold', bg='midnight blue', font="Helvetica 12 bold")
            lbl3.place(x=106, y=160)

            Bal_entry = Entry(root, borderwidth=4, relief=SUNKEN, textvariable=bal_var, width=25, bg='gold')
            Bal_entry.place(x=240, y=160)

            b10 = Button(root, bg='gold', fg='black', text="DATA ENTRY", borderwidth=5, font="Helvetica 10 bold",command=account)
            b10.place(x=170, y=200)
            b20 = Button(root, bg='gold', fg='black', text="LOAN", borderwidth=5, font="Helvetica 10 bold",
                         command=None)
            b20.place(x=295, y=200)
        except:
            tkinter.messagebox.showerror('Error', 'User not registered. Please Register at first')
            page1()
    def signUp(name,passwd,confirm):
        if (passwd==confirm):
            firebase = pyrebase.initialize_app(firebaseConfig)
            auth = firebase.auth()
            auth.create_user_with_email_and_password(name, passwd)
            tkinter.messagebox.showinfo('Success', "Register Successful")
        else:
            tkinter.messagebox.showerror('Error','Enter the exact password 2 times')
            quit()
    def page2():
        def page3():
            f2.destroy()
            l4.destroy()
            l5.destroy()
            l6.destroy()
            l7.destroy()
            registerName = username2.get()
            registerPassword = password2.get()
            confirmPassword = C_password2.get()
            try:
                signUp(registerName,registerPassword,confirmPassword)
                username2.destroy()
                password2.destroy()
                C_password2.destroy()
                b6.destroy()
                b4.destroy()
                b5.destroy()
                f3 = Frame(root, bg='gold', borderwidth=10, relief=RAISED, width=500, height=55)
                f3.pack(side=TOP, fill=X)
                l8 = Label(f3, text="Please Fill The Details Below", bg='gold', fg='black', font="Helvetica 12 bold")
                l8.pack(fill=X)
                l9 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Shop Name:-")
                l9.place(x=100, y=120)
                l10 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Proprietor:-")
                l10.place(x=108, y=160)
                l11 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Address:-")
                l11.place(x=123, y=200)
                l12 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Mobile No.:-")
                l12.place(x=106, y=240)

                shop = StringVar()
                pro = StringVar()
                address = StringVar()
                mob = StringVar()
                shopname = Entry(root, width=30, textvariable=shop, borderwidth=8, relief=SUNKEN)
                shopname.place(x=210, y=118)
                prop = Entry(root, width=30, textvariable=pro, borderwidth=8, relief=SUNKEN)
                prop.place(x=210, y=158)
                add = Entry(root, width=30, textvariable=address, borderwidth=8, relief=SUNKEN)
                add.place(x=210, y=198)
                mobile = Entry(root, width=30, textvariable=mob, borderwidth=8, relief=SUNKEN)
                mobile.place(x=210, y=238)

                def back2():
                    f3.destroy()
                    l8.destroy()
                    l9.destroy()
                    l10.destroy()
                    l11.destroy()
                    l12.destroy()
                    shopname.destroy()
                    prop.destroy()
                    add.destroy()
                    mobile.destroy()
                    b7.destroy()
                    b8.destroy()
                    b9.destroy()
    
                    page2()

                b7 = Button(root, text='Submit', bg='gold', fg='black', font="Helvetica 10 bold", borderwidth=8,
                            relief=SUNKEN)
                b7.place(x=190, y=290)
                b8 = Button(root, text='Quit', bg='gold', fg='black', command=root.quit, font="Helvetica 10 bold",
                            borderwidth=8, relief=SUNKEN)
                b8.place(x=280, y=290)
                b9 = Button(root, text="back", command=back2, borderwidth=4, bg='gold', fg='black', relief=SUNKEN,
                            font="Helvetica 10 bold")
                b9.place(x=1, y=418)

            except :
                tkinter.messagebox.showerror('Error','Unexpected Error Happened')
                page2()
            
        f1.destroy()
        l1.destroy()
        l2.destroy()
        l3.destroy()
        b1.destroy()
        b2.destroy()
        username1.destroy()
        password1.destroy()

        user_entry2 = StringVar()
        pass_entry2 = StringVar()
        cpass_entry = StringVar()
        f2 = Frame(root, bg='gold', borderwidth=10, relief=RAISED, width=500, height=55)
        f2.pack(side=TOP, fill=X)
        l4 = Label(f2, text="Please Fill The Details Below", bg='gold', fg='black', font="Helvetica 10 bold")
        l4.pack(fill=X)
        l5 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="New Username:-")
        l5.place(x=100, y=150)
        l6 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="New Password :-")
        l6.place(x=100, y=190)
        l7 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Confirm Password :-")
        l7.place(x=75, y=230)

        username2 = Entry(root, width=30, textvariable=user_entry2, borderwidth=8, relief=SUNKEN)
        username2.place(x=230, y=148)
        password2 = Entry(root, width=30, textvariable=pass_entry2, borderwidth=8, relief=SUNKEN)
        password2.place(x=230, y=188)
        C_password2 = Entry(root, width=30, textvariable=cpass_entry, borderwidth=8, relief=SUNKEN)
        C_password2.place(x=230, y=228)

        def back1():
            f2.destroy()
            l4.destroy()
            l5.destroy()
            l6.destroy()
            l7.destroy()
            username2.destroy()
            password2.destroy()
            C_password2.destroy()
            b6.destroy()
            b4.destroy()
            b5.destroy()
            page1()
        b6 = Button(root, text="Register", bg='gold', fg='black', font="Helvetica 11 bold", relief=SUNKEN,command=page3)
        b6.place(x=190, y=270)
        b4 = Button(root, text="Quit", bg='gold', fg='black', font="Helvetica 11 bold", relief=SUNKEN,
                    command=root.destroy)
        b4.place(x=300, y=270)
        b5 = Button(root, text="Back", bg='gold', fg='black', font="Helvetica 11 bold", relief=SUNKEN,command=back1)
        b5.place(x=2, y=43)
    user_entry = StringVar()
    pass_entry = StringVar()

    f1 = Frame(root, bg='gold', borderwidth=10, relief=RAISED, width=500, height=55)
    f1.pack(side=TOP, fill=X)
    l1 = Label(f1, text="---INVENTORY MANAGEMENT SYSTEM---", bg='gold', fg='black', font="Helvetica 12 bold")
    l1.pack(fill=X)
    l2 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Username:-")
    l2.place(x=100, y=150)
    l3 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Password :-")
    l3.place(x=100, y=190)

    username1 = Entry(root, width=30, textvariable=user_entry, borderwidth=4, relief=SUNKEN)
    username1.place(x=190, y=150)
    password1 = Entry(root, width=30, textvariable=pass_entry, show="*", borderwidth=4, relief=SUNKEN)
    password1.place(x=190, y=190)

    b1 = Button(root, text="Login", bg='gold', fg='black', font="Helvetica 11 bold", relief=SUNKEN,command=LoginPage)
    b1.place(x=220, y=230)
    b2 = Button(root, text="New/Register Here", bg='gold', fg='black', font="Helvetica 10 bold", relief=SUNKEN,command=page2,borderwidth=4)
    b2.place(x=363, y=45)

page1()
root.mainloop()
