import csv
from functools import partial
import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os
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


firebase=pyrebase.initialize_app(firebaseConfig)
db= firebase.database()


class gui:

    def __init__(self,root):
        self.root = root
        titlespace=" "
        self.root.title(100*titlespace+"Money Management System")
        self.root.geometry("850x750+330+0")
        self.root.resizable(width=False,height=False)

        # tabControl = ttk.Notebook(root)
        # tab1 = ttk.Frame(tabControl)
        # tab2 = ttk.Frame(tabControl)

        # tabControl.add(tab1, text = 'ACCOUNTS')
        # tabControl.add(tab2, text = 'LOANS')
        # tabControl.pack(expand = 1, fill ="both")

        
###################################################################################################################################
        MainFrame= Frame(self.root,bd=10,width=770,height=700,relief=RIDGE,bg='skyblue1')
        MainFrame.grid()

        TitleFrame= Frame(MainFrame,bd=7,width=770,height=100,relief=RIDGE)
        TitleFrame.grid(row=0,column=0)
        TopFrame3= Frame(MainFrame,bd=5,width=770,height=500,relief=RIDGE)
        TopFrame3.grid(row=1,column=0)
        
        LeftFrame = Frame(TopFrame3, bd=5, width=700, height=500, relief=RIDGE,padx=2, bg='skyblue1')
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=700, height=180, relief=RIDGE, padx=2,pady=9 )
        LeftFrame1.pack(side=TOP)

        RightFrame = Frame(TopFrame3, bd=5, width=50, height=100, relief=RIDGE,padx=2, bg='skyblue1')
        RightFrame.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame, bd=5, width=40, height=90, relief=RIDGE, padx=12,pady=4)
        RightFrame1a.pack(side=TOP)

        self.lbltitle=Label(TitleFrame, font=('Arial',33,'bold'), text="Money Management System",bd=7)
        self.lbltitle.grid(row=0,column=0,padx=130)
        
        Name = StringVar()
        Amount = StringVar()
        Date = StringVar()
#===============================================================================================================================================================================================
#Input Fields:

        self.lblname = Label(LeftFrame1, font =('arial',12,'bold'), text = 'Name' , bd = 13 )
        self.lblname.grid(row = 0, column=0, sticky = W,padx = 5)

        self.entname = Entry(LeftFrame1, font =('arial',12,'bold'), bd = 13 , width = 44, justify='left', textvariable = Name)
        self.entname.grid(row = 0, column=1, sticky = W,padx = 5)
        
        self.lblamount = Label(LeftFrame1, font =('arial',12,'bold'), text = 'Amount' , bd = 13 )
        self.lblamount.grid(row = 1, column=0, sticky = W,padx = 5)

        self.entamount = Entry(LeftFrame1, font =('arial',12,'bold'), bd = 13 , width = 44, justify='left', textvariable = Amount)
        self.entamount.grid(row = 1, column=1, sticky = W,padx = 5)

        self.lblDate = Label(LeftFrame1, font =('arial',12,'bold'), text = 'Date' , bd = 13 )
        self.lblDate.grid(row = 2, column=0, sticky = W,padx = 5)

        self.entDate = Entry(LeftFrame1, font =('arial',12,'bold'), bd = 13 , width = 44, justify='left', textvariable = Date)
        self.entDate.grid(row = 2, column=1, sticky = W,padx = 5)


#===============================================================================================================================================================================================
# The functions: 
    
        def exit():
            Exit = tkinter.messagebox.askyesno("Funds Man Sys", "Confirm if you want to exit?")
            if Exit>0:
                root.destroy()
                return

        def saveData():
            #function to save
            name = Name.get()
            amount = Amount.get()
            date = Date.get()
            
            datas = {'name': name, 'amount': amount, 'date': date}
            db.child('mainData').push(datas)

        def update():
            #function to update
            totalData = db.child('mainData').get()
            for data in totalData.each():
                if data.val()['name'] == Name.get() and data.val()['date'] == Date.get():
                    db.child('mainData').child(data.key()).update(
                        {'name': Name.get(), 'amount': Amount.get(), 'date': Date.get()})        
            tkinter.messagebox.showinfo("Funds Manager", "Updated Successfully")

        def search():
            #function to search
            totalData = db.child('mainData').get()
            with open('data.csv', 'w') as file:
                write = csv.writer(file)
                write.writerow(["Name", "Amount", "Date"])
                file.close()
            for data in totalData.each():
                print(data.val())
                if (data.val()['date'] == Date.get() or data.val()['name'] == Name.get() or data.val()['amount'] == Amount.get()):
                    with open('data.csv', 'a') as files:
                        write = csv.writer(files)
                        write.writerow([data.val()['name'], data.val()['amount'], data.val()['date']])
                        files.close()
            os.system('data.csv')

            #tkinter.messagebox.showinfo("Search Error","Data not found!")



        def display():
            result = db.child('mainData').get()
            for data in result.each():
                if len(data.val())!=0:
                    #self.display_data.delete(*self.display_data.get_children())
                    for row in data.val():
                        self.display_data.insert('', END, values = row)

        def delete():
            #function to delete 
            totalData = db.child('mainData').get()
            for data in totalData.each():
                if data.val()['name'] == Name.get() and data.val()['date'] == Date.get():
                    db.child('mainData').child(data.key()).remove()
    
        def TrainInfo(ev):
            viewInfo = self.display_data.focus()
            learnData = self.display_data.item(viewInfo)
            row = learnData['values']
            Name.set(row[0])
            Amount.set(row[1])
            Date.set(row[2])

        def reset():
            self.entname.delete(0, END)
            self.entamount.delete(0, END)
            self.entDate.delete(0, END)
#==============================================================================================================================================================================================
        y_scroll = Scrollbar(LeftFrame, orient= VERTICAL)
        self.display_data = ttk.Treeview(LeftFrame, height= 15, columns= ('Name', 'Amount', 'Date'), yscrollcommand= y_scroll.set)
        y_scroll.pack(side = RIGHT, fill= Y)

        self.display_data.heading("Name", text= "NAME")
        self.display_data.heading("Amount", text= "AMOUNT")
        self.display_data.heading("Date", text= "DATE")

        self.display_data['show'] = 'headings'

        self.display_data.column("Name", width= 80)
        self.display_data.column("Amount", width=80)
        self.display_data.column("Date", width=80)

        self.display_data.pack(fill=BOTH, expand =1)
        self.display_data.bind("<ButtonRelease-1>",TrainInfo)
        display()
#==============================================================================================================================================================================================

        self.btnAddNew=Button(RightFrame1a,font=('arial', 13, 'bold'), text="EXIT", bd=4, padx=18,pady=1,width=7,height=3,command=exit).grid(row=7,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13, 'bold'), text="UPDATE", bd=4, padx=18,pady=1,width=7,height=3,command=update).grid(row=2,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13, 'bold'), text="SAVE", bd=4, padx=18,pady=1,width=7,height=3,command=saveData).grid(row=1,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13, 'bold'), text="DELETE", bd=4, padx=18,pady=1,width=7,height=3,command=delete).grid(row=5,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13, 'bold'), text="SEARCH", bd=4, padx=18,pady=1,width=7,height=3,command=search).grid(row=4,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13 , 'bold'), text="DISPLAY", bd=4, padx=18,pady=1,width=7,height=3,command=display).grid(row=3,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13 , 'bold'), text="RESET", bd=4, padx=18,pady=1,width=7,height=3,command=reset).grid(row=6,column=0,padx=1)


#Main:

if __name__ == '__main__':
    root=tkinter.Tk()
    application = gui(root)
    root.mainloop()
