from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
import datetime as dt

root = Tk()
root.config(bg='midnight blue')
root.geometry("1000x700+290+55")
root.minsize(1000,700)
root.maxsize(1000,700)
root.title("IVS/Loan/LoanDetails")
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE, p1)
#---------------------------Functions--------------------------------#
def home():
    import Homepage
#-----------------------------------Heading Frame and Label---------------------------------#
Heading = Frame(root,bg='gold',borderwidth=4,relief=SUNKEN)
Heading.pack(fill=X)
Heading_Label = Label(Heading,text="------------LOAN DETAILS------------",font="Helvetica 18 bold",bg='gold',fg='black')
Heading_Label.pack()
#------------------------------------Time and Date Widgets----------------------------------#
def time_widget():
    string = strftime('%I:%M:%S %p')
    Time_Label.config(text=string)
    Time_Label.after(1000, time_widget)


Time_Label = Label(root, fg="gold", bg="midnight blue",
                   font="Helvetica 17 bold")
Time_Label.place(x=852, y=48)
time_widget()


date = Label(root, text=f"{dt.datetime.now():%A, %b/%d/%Y}", fg="gold", bg="midnight blue", font=(
    "Helvetica 15 underline"))
date.place(x=1, y=50)
#-----------------------------------------Tree View------------------------------------------#
tv_Frame = Frame(root, width=240, height=500,borderwidth=6,relief=SUNKEN)
tv_Frame.place(x=70,y=100)

y_scroll = Scrollbar(tv_Frame, orient=VERTICAL)
tree_v = ttk.Treeview(tv_Frame,height=25,selectmode="extended")
y_scroll.pack(side=RIGHT, fill=Y)
tree_v['columns'] = ("Name","Mobile No.","Principal Taken","Principal Left","Rate of Interest","Monthly Interest",
                     "Paid Interest","Date")

# ~~~~TreeView Styling~~~~
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font="Consolas 10 bold ",fieldbackground='gold')
style.configure("Treeview",fieldbackground="gold")
style.map('Treeview',background=[('selected','white')])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


tree_v.column('#0', width=0, stretch=NO)
tree_v.column('Name', anchor=CENTER, width=110)
tree_v.column('Mobile No.', anchor=CENTER, width=110)
tree_v.column('Principal Taken', anchor=CENTER, width=120)
tree_v.column('Principal Left', anchor=CENTER, width=110)
tree_v.column('Rate of Interest', anchor=CENTER, width=78)
tree_v.column('Monthly Interest', anchor=CENTER, width=125)
tree_v.column('Paid Interest', anchor=CENTER, width=100)
tree_v.column('Date', anchor=CENTER, width=90)

tree_v.heading('#0', anchor=CENTER,text='')
tree_v.heading('Name', anchor=CENTER, text="Name")
tree_v.heading('Mobile No.', anchor=CENTER, text="Mobile No.")
tree_v.heading('Principal Taken', anchor=CENTER, text="Principal Taken")
tree_v.heading('Principal Left', anchor=CENTER, text="Principal Left")
tree_v.heading('Rate of Interest', anchor=CENTER, text="Interest%")
tree_v.heading('Monthly Interest', anchor=CENTER, text="Monthly Interest")
tree_v.heading('Paid Interest', anchor=CENTER, text="Paid Interest")
tree_v.heading('Date', anchor=CENTER, text="Date")

tree_v.pack(fill=X)
#-----------------------------Footer Frame& buttons-----------------------------------#
footer = Frame(root,borderwidth=4,relief=RAISED)
footer.pack(side=BOTTOM,fill=X)
btn_syncup = Button(footer,text="Sync Up",font="Helvetica 12 bold",bg="gold")
btn_syncup.pack(side=LEFT,padx=40)
btn_syncdown = Button(footer,text="Sync Down",font="Helvetica 12 bold",bg="gold")
btn_syncdown.pack(side=RIGHT,padx=40)
btn_new = Button(footer,text="New",font="Helvetica 12 bold",bg="gold")
btn_new.pack(side=LEFT,padx= 135)
btn_update = Button(footer,text="Update",font="Helvetica 12 bold",bg="gold")
btn_update.pack(side=RIGHT,padx=135)
btn_back = Button(root,text="HOMEPAGE",font="Helvetica 12 bold",bg="gold",command=home)
btn_back.place(x=450,y=55)


root.mainloop()
