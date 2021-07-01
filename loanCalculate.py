import pyrebase
import pandas as pd

firebase_config = {
'apiKey': "AIzaSyDR-a5PGjXpXFjvJVS9Ep3FOKXnNy9BsZg",
    'authDomain': "fundmang-42ad8.firebaseapp.com",
    'projectId': "fundmang-42ad8",
    'storageBucket': "fundmang-42ad8.appspot.com",
    'messagingSenderId': "361815074904",
    'databaseURL':'https://fundmang-42ad8-default-rtdb.firebaseio.com',
    'appId': "1:361815074904:web:8504dfd52dbde0b186422d",
    'measurementId': "G-MVMXL8CJNK"
}
sum = 0
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()
name = input('Enter Name: ')
totalData = db.child('registerUserExp').child(name).get()
for data in totalData.each():
	sum+=int(data.val()['amount'])
print(sum)