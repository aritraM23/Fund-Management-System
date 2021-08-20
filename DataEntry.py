import csv
from functools import partial
import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os
from time import strftime
from datetime import datetime
import time
import pyrebase
import mysql.connector
from PIL.ImageTk import PhotoImage
from envVar import firebaseConfig as fc


firebase=pyrebase.initialize_app(fc)
db= firebase.database()

def back():
    root.destroy()
    import LoginPage

root=Tk()
root.geometry("1100x700+290+55")
root.minsize(1100, 700)
root.maxsize(1100, 700)
root.configure(bg='navy')
root.title("Registration Page")
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE, p1)


#---Entry Format----#
shop = StringVar()
pro = StringVar()
address = StringVar()
mob = StringVar()
#--Heading--#
head_frame = Frame(root, bg='DarkGoldenRod1', borderwidth=10, relief=RAISED, width=500, height=55)
head_frame.pack(side=TOP, fill=X)
heading = Label(head_frame, text="----Please Fill The Details Below----", bg='DarkGoldenRod1', fg='black', font="Helvetica 20 bold")
heading.pack()
#---Main Content---#
main_frame = Frame(root, bg='DarkGoldenrod1', borderwidth=8, relief=SUNKEN, width=520, height=285)
main_frame.place(x=300, y=155)
shopName = Label(main_frame, fg='black', bg='DarkGoldenRod1', font="Consolas 20 bold", text="Shop Name:-")
shopName.place(x=10, y=25)
shopEntry = Entry(main_frame, borderwidth=4, relief=RIDGE, font="Helvetica 18 bold", width=20)
shopEntry.place(x=210, y=25)
propName = Label(main_frame, fg='black', bg='DarkGoldenRod1', font="Consolas 20 bold", text="Proprietor:-")
propName.place(x=10, y=85)
propEntry = Entry(main_frame, borderwidth=4, relief=RIDGE, font="Helvetica 18 bold", width=20)
propEntry.place(x=210, y=85)
address = Label(main_frame, fg='black', bg='DarkGoldenRod1', font="Consolas 20 bold", text="Address:-")
address.place(x=10, y=145)
addEntry = Entry(main_frame, borderwidth=4, relief=RIDGE, font="Helvetica 18 bold", width=20)
addEntry.place(x=210, y=145)
mobile = Label(main_frame, fg='black', bg='DarkGoldenRod1', font="Consolas 20 bold", text="Mobile No.:-")
mobile.place(x=10, y=205)
mobEntry = Entry(main_frame, borderwidth=4, relief=RIDGE, font="Helvetica 18 bold", width=20)
mobEntry.place(x=210, y=205)

Reg_btn_frame = Frame(root, borderwidth=6, relief=SUNKEN, bg="DarkGoldenrod1")
Reg_btn_frame.place(x=490, y=490)
Reg_btn = Button(Reg_btn_frame, text="Register", bg="navy", borderwidth=4, relief=RIDGE,
                 font="Arial 18 bold", fg='DarkGoldenrod1', command=None)
Reg_btn.pack()

back_btn_frame = Frame(root, borderwidth=4, relief=SUNKEN, bg="DarkGoldenrod1")
back_btn_frame.place(x=1, y=55)
back_btn = Button(back_btn_frame, text="Back", bg="navy", borderwidth=2, relief=RIDGE,
                 font="Arial 18 bold", fg='DarkGoldenrod1', command=back).pack()

root.mainloop()
