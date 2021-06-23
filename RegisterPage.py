from tkinter import *

def New():
    root.destroy()
    import DataEntryPage
def back():
    root.destroy()
    import FirstPage

root = Tk()
root.geometry("550x550")
root.maxsize(550, 550)
root.minsize(550, 550)
root.configure(bg='midnight blue')
root.title("Registration Page/IVS")

user_entry = StringVar()
pass_entry = StringVar()
cpass_entry = StringVar()

f1 = Frame(root, bg='gold', borderwidth=10, relief=RAISED, width=500, height=55)
f1.pack(side=TOP, fill=X)
l1 = Label(f1, text="Please Fill The Details Below", bg='gold', fg='black', font="Helvetica 12 bold").pack(fill=X)

l2 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="New Username:-")
l2.place(x=100, y=150)
l3 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="New Password :-")
l3.place(x=100, y=190)
l4 = Label(root, bg='midnight blue', fg='gold', font="Helvetica 11 bold", text="Confirm Password :-")
l4.place(x=75, y=230)

username = Entry(root, width=30, textvariable=user_entry, borderwidth=8, relief=SUNKEN)
username.place(x=230, y=148)
password = Entry(root, width=30, textvariable=pass_entry, borderwidth=8, relief=SUNKEN)
password.place(x=230, y=188)
C_password = Entry(root, width=30, textvariable=cpass_entry, borderwidth=8, relief=SUNKEN)
C_password.place(x=230, y=228)

b1 = Button(root, text="Register", bg='gold', fg='black', font="Helvetica 11 bold", relief=SUNKEN,command=New)
b1.place(x=190, y=270)
b2 = Button(root, text="Quit", bg='gold', fg='black', font="Helvetica 11 bold", relief=SUNKEN,command=root.destroy)
b2.place(x=300, y=270)
b3 = Button(root, text="Back", bg='gold', fg='black', font="Helvetica 11 bold", relief=SUNKEN,command=back)
b3.place(x=2,y=45)

root.mainloop()