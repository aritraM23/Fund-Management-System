from tkinter import *

root = Tk()
root.geometry("550x450+600+90")
root.maxsize(550, 450)
root.minsize(550, 450)
root.configure(bg='midnight blue')
root.title("Register Customer")

name_entry = StringVar()
sur_entry = StringVar()
mob_entry = StringVar()
add_entry = StringVar()

f1 = Frame(root, bg='gold', borderwidth=10,
           relief=RAISED, width=500, height=55)
f1.pack(side=TOP, fill=X)
l1 = Label(f1, text="---Enter New Customer Details---", bg='gold',
           fg='black', font="Helvetica 12 bold").pack(fill=X)

name_label = Label(root, bg='midnight blue', fg='gold',
                   font="Helvetica 11 bold", text="Name:-")
name_label.place(x=151, y=135)
surname_label = Label(root, bg='midnight blue', fg='gold',
                      font="Helvetica 11 bold", text="Surname:-")
surname_label.place(x=129, y=175)
mob_label = Label(root, bg='midnight blue', fg='gold',
                  font="Helvetica 11 bold", text="Mobile no.:-")
mob_label.place(x=119, y=215)
adress = Label(root, bg='midnight blue', fg='gold',
               font="Helvetica 11 bold", text="Address:-")
adress.place(x=134, y=255)


name = Entry(root, width=27, textvariable=name_entry,
             borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
name.place(x=230, y=131)
surname = Entry(root, width=27, textvariable=sur_entry,
                borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
surname.place(x=230, y=171)
mobile = Entry(root, width=27, textvariable=mob_entry,
               borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
mobile.place(x=230, y=211)
address = Entry(root, width=27, textvariable=add_entry,
                borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
address.place(x=230, y=251)

submit_button = Button(root, text="Submit", bg='gold', fg='black',
                       font="Helvetica 11 bold", relief=SUNKEN, command=None)
submit_button.place(x=290, y=320)


root.mainloop()
