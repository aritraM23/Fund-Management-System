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

firebase = pyrebase.initialize_app(fc)
db = firebase.database()

root = Tk()
root.geometry("1100x700+290+55")
root.minsize(1100, 700)
root.maxsize(1100, 700)
root.configure(bg='navy')
root.title("Registration Page/IVS")
p1 = PhotoImage(file='[DIGICURE MAIN LOGO].png')
root.iconphoto(FALSE, p1)


def signUp():
        user_name = user_entry.get()
        password = pass_entry.get()
        confirm = cpass_entry.get()
        if (password == confirm):

            myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
                                                 database='ivs2')
            mycursor= myDataBase.cursor()
            dataentry ='Insert into loginManager (username,passward) values(%s,%s)'
            datas= [(user_name,password)]
            mycursor.executemany(dataentry,datas)
            myDataBase.commit()
            myDataBase.close()
            tkinter.messagebox.showinfo('Done','Welcome')
            root.destroy()
        else:
            tkinter.messagebox.showerror('Error','The two passwords must be same!!')
            quit()


def back():
    root.destroy()
    import LoginPage

#------ get data ------#


user_entry = StringVar()
pass_entry = StringVar()
cpass_entry = StringVar()
#------Heading-------#

head_frame = Frame(root, bg='DarkGoldenrod1', borderwidth=10, relief=RAISED)
head_frame.pack(side=TOP, fill=X)
heading = Label(head_frame, text="----REGISTRATION PAGE----", bg='DarkGoldenrod1', fg='black',
                font="Consolas 20 bold").pack()

#-----Entries--------#

main_frame = Frame(root, bg='DarkGoldenrod1', borderwidth=3, width=600, height=400)
main_frame.place(x=250, y=170)
userName = Label(main_frame, text='Username:-', bg='DarkGoldenrod1', fg='black',
                 font="Helvetica 19 bold")
userName.place(x=100, y=30)
userName_entry = Entry(main_frame, borderwidth=3, font="Helvetica 19 bold", width=22,
                       textvariable='user_entry', relief=SUNKEN)
userName_entry.place(x=255, y=30)
password = Label(main_frame, text='New Password:-', bg='DarkGoldenrod1', fg='black',
                        font="Helvetica 19 bold")
password.place(x=45, y=100)
password_entry = Entry(main_frame, borderwidth=3, font="Helvetica 19 bold", width=22, textvariable='pass_entry')
password_entry.place(x=255, y=100)
cpassword = Label(main_frame, text='Confirm Password:-', bg='DarkGoldenrod1', fg='black',
                        font="Helvetica 19 bold")
cpassword.place(x=5, y=170)
cpassword_entry = Entry(main_frame, borderwidth=3, font="Helvetica 19 bold", width=22, textvariable='cpass_entry')
cpassword_entry.place(x=255, y=170)
#------Buttons------#
reg_btn = Button(main_frame, borderwidth=3, width=7, text="Register", bg='navy',
                 fg='DarkGoldenrod1', relief=RIDGE, font="Helvetica 16 bold", command=signUp)
reg_btn.place(x=170, y=250)
quit_btn = Button(main_frame, borderwidth=3, width=7, text="Quit", bg='navy',
                  fg='DarkGoldenrod1', relief=RIDGE, font="Helvetica 16 bold", command=root.destroy)
quit_btn.place(x=320, y=250)
back_btn = Button(root, text='Back', font="Helvetica 16 bold", borderwidth=4, relief=RIDGE,
                  command=back, fg='black', bg='DarkGoldenrod1')
back_btn.place(x=2, y=58)
root.mainloop()
