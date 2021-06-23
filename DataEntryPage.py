from tkinter import *
field1 = 'Shop Name', 'Proprietor', 'Address', 'Mobile Number'
def new():
    reg.destroy()
    import RegisterPage

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


reg=Tk()
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
b1 = Button(fr3, text='Submit', bg='gold', fg='black', font="Helvetica 10 bold", borderwidth=8, relief=SUNKEN)
b1.pack(side=LEFT,padx=5)
b2 = Button(fr3, text='Quit', bg='gold', fg='black', command=reg.quit, font="Helvetica 10 bold", borderwidth=8, relief=SUNKEN)
b2.pack(side=LEFT,padx=5)
b3 = Button(reg,text="back",command=new,borderwidth=4,bg='gold',fg='black',relief=SUNKEN,font="Helvetica 10 bold")
b3.place(x=1,y=370)
reg.mainloop()