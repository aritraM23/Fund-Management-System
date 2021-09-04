firebaseConfig = {
	    'apiKey': "AIzaSyDR-a5PGjXpXFjvJVS9Ep3FOKXnNy9BsZg",
	  'authDomain': "fundmang-42ad8.firebaseapp.com",
	  'databaseURL': "https://fundmang-42ad8-default-rtdb.firebaseio.com",
	  'projectId': "fundmang-42ad8",
	  'storageBucket': "fundmang-42ad8.appspot.com",
	  'messagingSenderId': "361815074904",
	  'appId': "1:361815074904:web:8504dfd52dbde0b186422d",
	  'measurementId': "G-MVMXL8CJNK"
  }

import mysql.connector

myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
                                     database='ivs2')
mycursor = myDataBase.cursor()
