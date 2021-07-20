#todo bug bix in update function of firebase subdatabase

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

# import indiv
from PIL.ImageTk import PhotoImage

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
        self.root.geometry("883x750+330+0")
        self.root.maxsize(883,750)

        # tabControl = ttk.Notebook(root)
        # tab1 = ttk.Frame(tabControl)
        # tab2 = ttk.Frame(tabControl)

        # tabControl.add(tab1, text = 'ACCOUNTS')
        # tabControl.add(tab2, text = 'LOANS')
        # tabControl.pack(expand = 1, fill ="both")


        #clock function for live clock 
        QName = StringVar()  
        self.sumDep = 0
        def times():
            current_time=time.strftime("%H:%M:%S")
            self.clock.config(text=current_time)
            self.clock.after(200,times)

        self.btnState = False

        
        def switch():
            global btnState
            if self.btnState is True:
                for x in range(300):
                    self.navRoot.place(x = -x, y = 0)
                    TitleFrame.update()

                self.btnState = False

            else:

                for x in range(-300,0):
                    self.navRoot.place(x = x, y = 0)
                    TitleFrame.update()

                self.btnState = True
                
        def export():
            with open('FullFile.csv', 'w') as file:
                write = csv.writer(file)
                write.writerow(["Name", "Amount", "Date"])
                file.close()
            totalData = db.child('mainData').get()
            for data in totalData.each():
                with open('FullFile.csv', 'a') as files:
                    print('Inside this')
                    write = csv.writer(files)
                    write.writerow([data.val()['name'], data.val()['amount'], data.val()['date']])
                    files.close()
            os.system('FullFile.csv')
            return 0

        def ind_import():

            def s_byname():
                name = QName.get()
                self.sumDep = 0
                totalData = db.child('registerUserExp').child(name).get()
                
                for data in totalData.each():
                    self.sumDep+=int(data.val()['amount'])
                
                self.deposit.config(text = str(self.sumDep))
                #return sumDep

            
            self.ind = Toplevel(root)
            self.ind.geometry("578x340+330+0")
            self.ind.title(50*titlespace+"Money Management System")
            #self.ind.maxsize("570x250")
            #self.ind.resizable(False)
            
            mainFrame= Frame(self.ind,bd=10,width=500,height=370,relief=RIDGE,bg='midnight blue')
            mainFrame.grid()

            # self.labelMain = Label(self.ind, bd=7, width=500, height=400, bg='midnight blue')
            # self.labelMain.grid(row = 0, column = 0)
            topFrame = Frame(mainFrame,bd=10,width=500,height=370,relief=RIDGE,bg='midnight blue' )
            topFrame.grid(row = 1, column = 0)

            indtitleFrame = Frame(mainFrame,bd=10,width=500,height=70, bg='midnight blue')
            indtitleFrame.grid(row = 0, column= 0)

            self.indtitle=Label(indtitleFrame, font=('Arial',18,'bold'), fg= 'gold', text="Import Individual Data by Name:",bd=7, bg = 'midnight blue')
            self.indtitle.grid(row=0,column=1,padx=70)

            
            self.indEntry = Entry(topFrame, font =('arial',13,'bold'), bd = 13 , width = 50,justify='left',  textvariable = QName)
            self.indEntry.grid(row = 0, column=0, padx = 5)

            Label(topFrame, font=('Arial',18,'bold'), text=" ",bd=3, bg = 'midnight blue').grid(row=1,column=0,padx=70)

            Button(topFrame,font=('arial', 13, 'bold'), text="IMPORT", bd=5, padx=10,pady=1,width=5,height=2,bg = 'gold',command=s_byname).grid(row=2,column=0,padx=1)

            self.output = Label(topFrame, font =('arial',13,'bold'), bd = 13 , width = 50,justify='left',bg= 'midnight blue', fg = 'gold',  text = "Total Output:")
            self.output.grid(row = 3, column=0, padx = 5)
            
            self.deposit = Label(topFrame, font =('arial',13,'bold'), bd = 13 , width = 50,justify='left', bg = 'midnight blue', fg = 'gold', text = str(self.sumDep))
            self.deposit.grid(row = 4, column=0, padx = 5)
            # self.root.maxsize(460,350)
            # self.root.destroy()
            # import indiv
            # self.root.destroy()
            # indiv.gui(tkinter.Tk())

        def about():
            pass
             
###################################################################################################################################
        MainFrame= Frame(self.root,bd=10,width=770,height=700,relief=RIDGE,bg='midnight blue')
        MainFrame.grid()

        TitleFrame= Frame(MainFrame,bd=7,width=770,height=100, bg='midnight blue')
        TitleFrame.grid(row=0,column=0)
        TopFrame3= Frame(MainFrame,bd=5,width=770,height=500, bg = 'gold')
        TopFrame3.grid(row=1,column=0)
        
        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=500, padx=2,pady=0, bg='midnight blue')
        LeftFrame.pack(side=LEFT, expand = True, fill = 'both')
        LeftFrame1 = Frame(LeftFrame, bd=5, width=770, height=180, padx=2,pady=0, bg = 'gold' )
        LeftFrame1.pack(side=TOP, expand = True, fill = 'both')

        RightFrame = Frame(TopFrame3, bd=5, width=50, height=100, relief=RIDGE,padx=2, bg='midnight blue')
        RightFrame.pack(side=RIGHT,expand = True, fill = 'both')
        RightFrame1a = Frame(RightFrame, bd=5, width=40, height=90, padx=12,pady=4, bg = 'midnight blue' )
        RightFrame1a.pack(side=TOP, expand = True, fill = 'both')

        self.lbltitle=Label(TitleFrame, font=('Arial',33,'bold'), fg= 'gold', text="Money Management System",bd=7, bg = 'midnight blue')
        self.lbltitle.grid(row=0,column=1,padx=70)
        
        Name = StringVar()
        Amount = StringVar()
        Date = StringVar()
#===============================================================================================================================================================================================
#Input Fields:

        self.lblname = Label(LeftFrame1, font =('arial',13,'bold'), text = 'Name' , bd = 13 , bg = 'gold')
        self.lblname.grid(row = 1, column=0, sticky = W,padx = 5)

        self.entname = Entry(LeftFrame1, font =('arial',13,'bold'), bd = 13 , width = 50, justify='left', textvariable = Name)
        self.entname.grid(row = 1, column=1, sticky = W,padx = 5)
        
        self.lblamount = Label(LeftFrame1, font =('arial',13,'bold'), text = 'Amount' , bd = 13 , bg = 'gold' )
        self.lblamount.grid(row = 2, column=0, sticky = W,padx = 5)

        self.entamount = Entry(LeftFrame1, font =('arial',13,'bold'), bd = 13 , width = 50, justify='left', textvariable = Amount)
        self.entamount.grid(row = 2, column=1, sticky = W,padx = 5)

        self.lblDate = Label(LeftFrame1, font =('arial',13,'bold'), text = 'Date' , bd = 13 , bg = 'gold')
        self.lblDate.grid(row = 3, column=0, sticky = W,padx = 5)

        self.entDate = Entry(LeftFrame1, font =('arial',13,'bold'), bd = 13 , width = 50,  justify='left', textvariable = Date)
        self.entDate.grid(row = 3, column=1, sticky = W,padx = 5)

        #label for clock display
        self.clock=Label(TitleFrame,font=("times",15,"bold"),bg="midnight blue",fg='gold')
        self.clock.grid(row=0,column=2,padx=0, pady = 0)
        times()
#===============================================================================================================================================================================================

    #nav bar
        self.navIcon = PhotoImage(file = "navbar.png")
        self.closeIcon = PhotoImage(file = "exit.png")

        self.nvbarbtn = Button(TitleFrame, image = self.navIcon,  width=24,height=24, bd = 0, padx = 1, command= switch ).grid(row= 0, column= 0, padx = 0, pady = 0 )
        self.navRoot = Frame(root, bg = 'gold', height= 500, width = 200)
        self.navRoot.place(x = -300, y = 0)

        Label(self.navRoot, text = "Menu", font = 'arial 10 bold', bg = 'midnight blue', fg = 'gold', height = 3, width= 200, padx = 0).place(x= 0 , y=0)

        self.y = 80

        self.options = ["Export All", "Import Individual", "About" ]
        self.methods = [ export , ind_import, about ]
        
        self.navExp = Button(self.navRoot, text="Export All", font="arial 13", bg="gold", fg='midnight blue', activebackground="white", activeforeground="black", bd=0, command = export ).place(x=25, y=self.y)
        self.y += 40

        self.navInd = Button(self.navRoot, text="Import Individual", font="arial 13", bg="gold", fg='midnight blue', activebackground="white", activeforeground="black", bd=0, command = ind_import ).place(x=25, y=self.y)
        self.y += 40

        self.navAbt = Button(self.navRoot, text="About", font="arial 13", bg="gold", fg='midnight blue', activebackground="white", activeforeground="black", bd=0, command = about ).place(x=25, y=self.y)

        self.closeBtn = Button(self.navRoot, image = self.closeIcon,  width=22,height=22, relief= RIDGE, bd = 0, padx = 1, command= switch )
        self.closeBtn.place(x= 150, y = 20)
        
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
            if(date.find("-")>-1 ):
                tday, tm, ty = date.split("-")
                mdate = tday+"/"+tm+"/"+ty
                date = mdate
            elif date.find(".")>-1:
                tday, tm, ty = date.split(".")
                mdate = tday+"/"+tm+"/"+ty
                date = mdate
            try:
                if (Name.get()!='' and Date.get()!='' and Amount.get()!=''):
                    datas = {'name': name, 'amount': amount, 'date': date}
                    db.child('mainData').push(datas)
                    db.child('registerUserExp').child(name).push(datas)
                    myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs')
                    mycursor = myDataBase.cursor()
                    dataCollection = 'Insert into dataEntry (name,amount,date) values (%s,%s,%s)'
                    datas = [(name,amount,date)]
    
                    mycursor.executemany(dataCollection, datas)
                    myDataBase.commit()
                    myDataBase.close()
                    display()
                    reset()
                    sync()
                else:
                    reset()
                    tkinter.messagebox.showerror('Error', 'Insert Data In All Fields')

            except:
                myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs')
                mycursor = myDataBase.cursor()
                dataCollection = 'Insert into dataEntry (name,amount,date) values (%s,%s,%s)'
                datas = [(name, amount, date)]
    
                mycursor.executemany(dataCollection, datas)
                myDataBase.commit()
                myDataBase.close()
                display()
                reset()
                sync()
                
                
        def update():
            try:
                totalMainData = db.child('mainData').get()
                totalIndividualData = db.child('registerUserExp').child(Name.get()).get()
                for data in totalMainData.each():
                    for indi in totalIndividualData.each():
                            date = Date.get()
                            if(date.find("-")>-1 ):
                                tday, tm, ty = date.split("-")
                                mdate = tday+"/"+tm+"/"+ty
                                date = mdate
                            elif date.find(".")>-1:
                                tday, tm, ty = date.split(".")
                                mdate = tday+"/"+tm+"/"+ty
                                date = mdate
            
                            if data.val()['name'] == Name.get() and data.val()['date'] == date:
                                db.child('mainData').child(data.key()).update({'name': Name.get(), 'amount': Amount.get(),
                                                                               'date': date})
                                db.child('registerUserExp').child(Name.get()).child(indi.key()).update({'name': Name.get(),
                                                                                'amount': Amount.get(), 'date': date})
                                myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs')
                                mycursor = myDataBase.cursor()
            
                                mycursor.execute(
                                    'update dataEntry set amount=%s where name=%s and date = %s', (
                                        Amount.get(),
                                        Name.get(),
                                        Date.get()
                                    ))
                                myDataBase.commit()
                                myDataBase.close()
                tkinter.messagebox.showinfo("Funds Manager", "Updated Successfully")
                display()
                reset()
            except :
                myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs')
                mycursor = myDataBase.cursor()
    
                mycursor.execute(
                    'update dataEntry set amount=%s where name=%s and date = %s', (
                        Amount.get(),
                        Name.get(),
                        Date.get()
                    ))
                myDataBase.commit()
                myDataBase.close()
                tkinter.messagebox.showinfo("Funds Manager", "Updated Successfully")
                display()
                reset()
                
        def search():
            self.sum = 0
            self.callAll = 'all'
            totalData = db.child('mainData').get()
            loanDB = db.child('loanDemo').get()

            date = Date.get()
            if(date.find("-")>-1 ):
                tday, tm, ty = date.split("-")
                mdate = tday+"/"+tm+"/"+ty
                date = mdate
            elif date.find(".")>-1:
                tday, tm, ty = date.split(".")
                mdate = tday+"/"+tm+"/"+ty
                date = mdate


            with open('data.csv', 'w') as file:
                write = csv.writer(file)
                write.writerow(["Name", "Amount", "Date", "Loan"])
                file.close()
            for data in totalData.each():
                for ld in loanDB.each():
                    if ('all'==Name.get().lower()):
                        with open('FullFile.csv', 'w') as file:
                            write = csv.writer(file)
                            write.writerow(["Name", "Amount", "Date", "Loan"])
                            file.close()
                        totalData = db.child('mainData').get()
                        loanDB = db.child('loanDemo').get()
                        for data in totalData.each():
                            for ld in loanDB.each():
                                with open('FullFile.csv', 'a') as files:
                                    write = csv.writer(files)
                                    if ld.val()['Name']==data.val()['name']:
                                        write.writerow([data.val()['name'], data.val()['amount'], data.val()['date'], ld.val()['Amount']])
                                        files.close()
                                    else:
                                        write.writerow([data.val()['name'], data.val()['amount'], data.val()['date'], 'N/A'])
                                        files.close()
                        os.system('FullFile.csv')
                        return 0
                    elif (data.val()['date'] == date or data.val()['name'] == Name.get() or data.val()['amount']==Amount.get()):
                        with open('data.csv', 'a') as files:
                            write = csv.writer(files)
                            if ld.val()['Name']==data.val()['name']:
                                write.writerow([data.val()['name'], data.val()['amount'], data.val()['date'], ld.val()['Amount']])
                                files.close()
                            else:
                                write.writerow([data.val()['name'], data.val()['amount'], data.val()['date'], 'N/A'])
                                files.close()
                            self.sum += 1
                    
                         
            if self.sum>0:
                os.system('data.csv')
            
            if self.sum==0:
                alertMssg()


        def alertMssg():
            tkinter.messagebox.showerror("Search Error","Data not found!")

        def display():
            myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs')
            mycursor = myDataBase.cursor()
            mycursor.execute("select * from dataEntry")
            result = mycursor.fetchall()
            if len(result) != 0:
                self.display_data.delete(*self.display_data.get_children())
                for row in result:
                    self.display_data.insert('', END, values=row)
            myDataBase.commit()
            myDataBase.close()

        def delete():
            #function to delete
            try:
                self.deleteData=0
                totalData = db.child('mainData').get()
                
                for data in totalData.each():
                    
                    if data.val()['name'] == Name.get() and data.val()['date'] == Date.get():
                        db.child('mainData').child(data.key()).remove()
                        db.child('registerUserExp').child(Name.get()).child(data.key()).remove()
                        myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs')
                        mycursor = myDataBase.cursor()
                        mycursor.execute("delete from dataEntry where name=%s", (
                            Name.get(),
                        ))
                        myDataBase.commit()
                        display()
                        myDataBase.close()
                        tkinter.messagebox.showinfo('Deleted', 'Deleted Successfully')
                        self.deleteData+=1
                    if Name.get()=='' :
                        tkinter.messagebox.showerror('Error', 'Enter Name')
                        self.deleteData+=1
                        break
                    if Date.get()=='':
                        tkinter.messagebox.showerror('Error', 'Enter Date')
                        self.deleteData += 1
                        break
                    reset()
                    display()
                if (self.deleteData==0):
                    reset()
                    display()
                    tkinter.messagebox.showerror('Error', 'No Data Found')
            except :
                self.deleteData = 0
                myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs')
                mycursor = myDataBase.cursor()
                mycursor.execute("delete from dataEntry where name=%s", (
                    Name.get(),
                ))
                myDataBase.commit()
                display()
                myDataBase.close()
                tkinter.messagebox.showinfo('Deleted', 'Deleted Successfully')
                self.deleteData += 1
              
                reset()
                display()
    
                if (self.deleteData == 0):
                    reset()
                    display()
                    tkinter.messagebox.showerror('Error', 'No Data Found')
                
    
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
        
        def sync():
            databaseChoice = input('Which one you need')
            if (databaseChoice == 'f'):
                totalData = db.child('mainData').get()
                for data in totalData.each():
                    myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs')
                    mycursor = myDataBase.cursor()
                    dataCollection = 'Insert into dataEntry (name,amount,date) values (%s,%s,%s)'
                    datas = [(data.val()['name'], data.val()['amount'], data.val()['date'])]
                    mycursor.executemany(dataCollection, datas)
                    myDataBase.commit()
                    myDataBase.close()
                tkinter.messagebox.showinfo('Success','Data Synced')
            
            else:
                myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345", database='ivs')
                mycursor = myDataBase.cursor()
                query ='Select * from dataEntry'
                mycursor.execute(query)
                totalEntries = mycursor.fetchall()
                print(totalEntries)
                for rows in totalEntries:
                    datas = {'name': rows[0], 'amount': rows[1], 'date': rows[2]}
                    db.child('mainData').push(datas)
                    db.child('registerUserExp').child(rows[0]).push(datas)
                tkinter.messagebox.showinfo('Success','Done')

        #==============================================================================================================================================================================================

        y_scroll = Scrollbar(LeftFrame, orient= VERTICAL)
        self.display_data = ttk.Treeview(LeftFrame, height= 18, columns= ('Name', 'Amount', 'Date'), yscrollcommand= y_scroll.set)
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

        self.btnAddNew=Button(RightFrame1a,font=('arial', 13, 'bold'), text="EXIT", bd=7, padx=18,pady=1,width=7,height=3,bg = 'gold',command=exit).grid(row=7,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13, 'bold'), text="UPDATE", bd=7, padx=18,pady=1,width=7,height=3, bg = 'gold',command=update).grid(row=2,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13, 'bold'), text="SAVE", bd=7, padx=18,pady=1,width=7,height=3, bg = 'gold',command=saveData).grid(row=1,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13, 'bold'), text="DELETE", bd=7, padx=18,pady=1,width=7,height=3, bg = 'gold',command=delete).grid(row=5,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13, 'bold'), text="SEARCH", bd=7, padx=18,pady=1,width=7,height=3, bg = 'gold',command=search).grid(row=4,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13 , 'bold'), text="DISPLAY", bd=7, padx=18,pady=1,width=7,height=3, bg = 'gold',command=display).grid(row=3,column=0,padx=1)
        self.btnAddNew=Button(RightFrame1a,font=('arial', 13 , 'bold'), text="RESET", bd=7, padx=18,pady=1,width=7,height=3, bg = 'gold',command=reset).grid(row=6,column=0,padx=1)

#================================================================================================================================================================================================

#Main:

# if __name__ == '__main__':
root=tkinter.Tk()
application = gui(root)
root.mainloop()
