from tkinter import *
def New():
    root.destroy()
    import RegisterPage
def Login():
    root.destroy()
    import Homepage

root = Tk()
root.geometry("500x450")
root.maxsize(500,450)
root.minsize(500,450)
root.configure(bg='midnight blue')
root.title("Login/Register/IVS")
    
user_entry = StringVar()
pass_entry = StringVar()
    
f1 = Frame(root,bg='gold',borderwidth=10,relief=RAISED,width=500,height=55)
f1.pack(side=TOP,fill =X)
l1 = Label(f1,text="---INVENTORY MANAGEMENT SYSTEM---",bg='gold',fg='black',font="Helvetica 12 bold").pack(fill=X)
    
l2 = Label(root,bg='midnight blue',fg='gold',font="Helvetica 11 bold",text="Username:-")
l2.place(x=100,y=150)
l3 = Label(root,bg='midnight blue',fg='gold',font="Helvetica 11 bold",text="Password :-")
l3.place(x=100,y=190)
    
username = Entry(root,width=30,textvariable=user_entry,borderwidth=4,relief=SUNKEN)
username.place(x=190,y=150)
password = Entry(root,width=30,textvariable=pass_entry,show="*",borderwidth=4,relief=SUNKEN)
password.place(x=190,y=190)

b1 = Button(root,text="Login",bg='gold',fg='black',font="Helvetica 11 bold",relief=SUNKEN,command=Login)
b1.place(x=220,y=230)
b2 = Button(root,text="New/Register Here",bg='gold',fg='black',font="Helvetica 10 bold",relief=SUNKEN,command=New)
b2.place(x=365,y=50)


root.mainloop()
