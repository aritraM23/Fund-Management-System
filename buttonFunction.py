
#todo signUPFunction
def signUp(self, instance):
		firebase = pyrebase.initialize_app(firebaseConfig)
		auth = firebase.auth()
		name = self.name.text
		password = self.password.text
		confirm_password = self.confirm_password.text
		if password==confirm_password:
	    		auth.create_user_with_email_and_password(name, password)
    			print('Done')

#todo signInFunction
def signIn(self, instance):
	firebase = pyrebase.initialize_app(firebaseConfig)
	auth = firebase.auth()
	name = self.name.text
	
	password = self.password.text
	auth.sign_in_with_email_and_password(name, password)
	print('Done SognIN')

#todo saveDataFunction
def saveData(self, instance):
	name = self.name.text
	amount = self.amount.text
	date = self.date.text
	
	datas = {'name': name, 'amount': amount, 'date': date}
	db.child('mainData').push(datas)
	
#todo upDateFunction
def update(self, instance):
		firebase = pyrebase.initialize_app(firebaseConfig)
		db = firebase.database()
		totalData = db.child('mainData').get()
		for data in totalData.each():
			if data.val()['name'] == self.name.text and data.val()['date'] == self.name.date:
				db.child('mainData').child(data.key()).update(
					{'name': self.name.text, 'amount': self.amount.text, 'date': self.date.text})
		print('Done')

#todo deleteFunction
def delete(self,instance):
		firebase = pyrebase.initialize_app(firebaseConfig)
		db = firebase.database()
		totalData = db.child('mainData').get()
		for data in totalData.each():
			if data.val()['name'] == self.name.text and data.val()['date'] == self.name.date:
				db.child('mainData').child(data.key()).remove()

#todo updateFunction
def search(self, instance):
		firebase = pyrebase.initialize_app(firebaseConfig)
		db = firebase.database()
		totalData = db.child('testDataBase').get()
		with open('data.csv', 'a') as file:
			write = csv.writer(file)
			write.writerow(["Name", "Amount", "Date"])
			file.close()
		for data in totalData.each():
			if (data.val()['date'] == self.date.text or data.val()['name'] == self.name.text or data.val()['amount'] == self.amount.text):
				with open('data.csv', 'a') as files:
					write = csv.writer(files)
					write.writerow([data.val()['name'], data.val()['amount'], data.val()['date']])
					files.close()
		os.system('data.csv')