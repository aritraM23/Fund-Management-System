from tkinter import *

root = Tk()
root.config(bg='midnight blue')
root.geometry("580x470+500+130")
root.maxsize(580, 470)
root.minsize(580, 470)
root.title("NewLoan Page")

Top_Frame = Frame(root,borderwidth=6,bg='gold',relief=RAISED)
Top_Frame.pack(fill=X)
Top_Label = Label(Top_Frame,text="---New Loan Data Entry---",bg='gold',font="Helvetica 14 bold")
Top_Label.pack()
#--------------------All labels----------------------------------#
name = Label(root,text="Name:",font="Helvetica 12 bold",bg="midnight blue",fg='gold')
mobile = Label(root,text="Mobile No.:",font="Helvetica 12 bold",bg="midnight blue",fg='gold')
address = Label(root,text="Address:",font="Helvetica 12 bold",bg="midnight blue",fg='gold')
shop = Label(root,text="Shop Name:",font="Helvetica 12 bold",bg="midnight blue",fg='gold')
date = Label(root,text="Date(DD/MM/YYYY):",font="Helvetica 12 bold",bg="midnight blue",fg='gold')
principal = Label(root,text="Principal taken:",font="Helvetica 12 bold",bg="midnight blue",fg='gold')
interest = Label(root,text="Interest:",font="Helvetica 12 bold",bg="midnight blue",fg='gold')

name.place(x=145,y=80)
mobile.place(x=110,y=120)
address.place(x=125,y=160)
shop.place(x=102,y=200)
date.place(x=50,y=240)
principal.place(x=80,y=280)
interest.place(x=135,y=320)
#-----------------------------------------------------#
#-------------------Entry Fields----------------------#
name_entry = Entry(root,borderwidth=4,relief=SUNKEN,font="Arial 11 bold",width=30)
mobile_entry = Entry(root,borderwidth=4,relief=SUNKEN,font="Arial 11 bold",width=30)
address_entry = Entry(root,borderwidth=4,relief=SUNKEN,font="Arial 11 bold",width=30)
shop_entry = Entry(root,borderwidth=4,relief=SUNKEN,font="Arial 11 bold",width=30)
date_entry = Entry(root,borderwidth=4,relief=SUNKEN,font="Arial 11 bold",width=30)
principal_entry = Entry(root,borderwidth=4,relief=SUNKEN,font="Arial 11 bold",width=30)
interest_entry = Entry(root,borderwidth=4,relief=SUNKEN,font="Arial 11 bold",width=30)

name_entry.place(x=215,y=80)
mobile_entry.place(x=215,y=120)
address_entry.place(x=215,y=160)
shop_entry.place(x=215,y=200)
date_entry.place(x=215,y=240)
principal_entry.place(x=215,y=280)
interest_entry.place(x=215,y=320)
#-------------------------------------------------------------------------#
#-----------Button-----------------------------------#
add_btn = Button(root,text="Add",font="Arial 12 bold",bg="gold",fg="black")
add_btn.place(x=270,y=370)
root.mainloop()
