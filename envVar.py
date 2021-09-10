firebaseConfig = {
  'apiKey': "AIzaSyDcV5glka3KVdIt3aafx-DYNyD08xSkcAk",
  'authDomain': "firstapp-695bf.firebaseapp.com",
  'databaseURL': "https://firstapp-695bf.firebaseio.com",
  'projectId': "firstapp-695bf",
  'storageBucket': "firstapp-695bf.appspot.com",
  'messagingSenderId': "358776218892",
  'appId': "1:358776218892:web:e75199b4fbc85e21cd9529",
  'measurementId': "G-Y6YLMC6JVM"
}
import mysql.connector

myDataBase = mysql.connector.connect(host="localhost", user="root", passwd="12345",
                                     database='ivs2')
mycursor = myDataBase.cursor()
