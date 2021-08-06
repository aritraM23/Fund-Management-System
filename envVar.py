firebaseConfig = {
    'apiKey': "AIzaSyDTMWv-92WG5xZ1NvcVb7WlE0mjPAiosY4",
    'authDomain': "ivslive.firebaseapp.com",
    'projectId': "ivslive",
    'storageBucket': "ivslive.appspot.com",
    'messagingSenderId': "846488367861",
    'appId': "1:846488367861:web:581efb46cf0210326a4bbc",
	'databaseURL' : "https://ivslive-default-rtdb.firebaseio.com/",
    'measurementId': "G-RBWZWSHQSQ"
  }
import mysql.connector

myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
                                     database='ivs2')
mycursor = myDataBase.cursor()
