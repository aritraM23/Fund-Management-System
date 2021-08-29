import mysql.connector
myDatabase =  mysql.connector.connect(host='localhost',user='root',passwd='12345',database='ivs2')
myCursor = myDatabase.cursor()
#
# myCursor.execute('Create table loginManager(username varchar(200),passward varchar(200))')
# myDatabase.commit()
# myDatabase.close()
#
# myCursor.execute('Create table ivsLoan2 (name varchar(200),mobileNumber varchar(200), address varchar(200), shopName varchar (200), date varchar (200), principalAmount float(10,2),          interestPercent float (10,2), principlePaid float(10,2), interestPaid float(10,2), principleLeft float(10,2)\
#           , interestLeft float(10,2), InterestPaidTillDate float(10,2), dateGiven varchar(200))')
# myDatabase.commit()
# myDatabase.close()