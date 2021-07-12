from tkinter import *

root = Tk()
root.geometry("550x450+600+90")
root.maxsize(550, 450)
root.minsize(550, 450)
root.configure(bg='midnight blue')
root.title("Deposit on Existing Loan")

name_entry = StringVar()
mob_entry = StringVar()
p_entry = StringVar()
i_entry = StringVar()

f1 = Frame(root, bg='gold', borderwidth=10,
           relief=RAISED, width=500, height=55)
f1.pack(side=TOP, fill=X)
l1 = Label(f1, text="----Deposit Loan----", bg='gold',
           fg='black', font="Helvetica 12 bold").pack(fill=X)

name_label = Label(root, bg='midnight blue', fg='gold',
                   font="Helvetica 11 bold", text="Name")
name_label.place(x=165, y=135)
mob_label = Label(root, bg='midnight blue', fg='gold',
                      font="Helvetica 11 bold", text="Mobile No.")
mob_label.place(x=129, y=175)
principal_label = Label(root, bg='midnight blue', fg='gold',
               font="Helvetica 11 bold", text="Principal Given")
principal_label.place(x=94, y=215)
interest_label = Label(root, bg='midnight blue', fg='gold',
               font="Helvetica 11 bold", text="Interest Given")
interest_label.place(x=102, y=255)


name = Entry(root, width=27, textvariable=name_entry,
             borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
name.place(x=230, y=131)
mobile = Entry(root, width=27, textvariable=mob_entry,
                borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
mobile.place(x=230, y=171)
principal = Entry(root, width=27, textvariable=p_entry,
                borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
principal.place(x=230, y=211)
interest = Entry(root, width=27, textvariable=i_entry,
                borderwidth=8, relief=SUNKEN, font="Helvetica 11 bold")
interest.place(x=230, y=251)

submit_button = Button(root, text="Add", bg='gold', fg='black',
                       font="Helvetica 11 bold", relief=SUNKEN, command=None)
submit_button.place(x=425, y=310)


root.mainloop()
