from kivy.app import App
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.datatables import MDDataTable
import pyrebase

firebaseConfig = {}


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
 
class SecondWindow(Screen):
    def __init__(self, **kwargs):

        super(SecondWindow, self).__init__(**kwargs)

        self.add_widget(Label(text='Money Management System', bold = True, font_name = 'Times', font_size = 40, size_hint = (.15, .05), pos_hint={'x': 0.25, 'y': .9}))

        self.add_widget(Label(text='', bold = True ,font_size = 20 ,size_hint = (.15, .05), pos_hint={'x': 0.01, 'y': .70}))
        self.Name = TextInput(multiline=False, size_hint=(.50, .05), pos_hint={'x': 0.20, 'y': .70})
        self.add_widget(self.Name)

        self.add_widget(Label(text='Loan Amount', bold = True, font_size = 20 ,size_hint = (.15, .05), pos_hint={'x': 0.01, 'y': .60}))
        self.Amount = TextInput(multiline=False, size_hint=(.50, .05), pos_hint={'x': 0.20, 'y': .60})
        self.add_widget(self.Amount)

        self.add_widget(Label(text='Interest Rate', bold = True, font_size = 20 ,size_hint = (.15, .05), pos_hint={'x': 0.01, 'y': .50}))
        self.Amount = TextInput(multiline=False, size_hint=(.50, .05), pos_hint={'x': 0.20, 'y': .50})
        self.add_widget(self.Amount)

        self.add_widget(Label(text='Date',  bold = True,  font_size = 20 ,size_hint = (.15, .05), pos_hint={'x': 0.01, 'y': .40}))
        self.Date = TextInput(multiline=False, size_hint=(.50, .05), pos_hint={'x': 0.20, 'y': .40})
        self.add_widget(self.Date)

        self.btn1 = Button(text = 'Accounts',bold = True, font_size = 22, size_hint = (0.20,0.10), pos_hint = {'center_x':0.9,'center_y':0.10})
        self.btn2 = Button(text= "Save", font_size=22,bold = True, size_hint = (0.20,0.10), pos_hint = {'center_x':0.9,'center_y':0.90})
        self.btn3 = Button(text= "Update", font_size= 22,bold = True, size_hint = (0.20,0.10), pos_hint = {'center_x':0.9,'center_y':0.75})
        self.btn4 = Button(text= "Delete", font_size= 22, bold = True,size_hint = (0.20,0.10), pos_hint = {'center_x':0.9, 'center_y':0.60})
        self.btn5 = Button(text= "Display", font_size= 22,bold = True, size_hint = (0.20,0.10), pos_hint = {'center_x':0.9, 'center_y':0.45})
        self.btn6 = Button(text= "Search", font_size= 22,bold = True, size_hint = (0.20,0.10), pos_hint = {'center_x':0.9, 'center_y':0.30})

        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)
        self.add_widget(self.btn4)
        self.add_widget(self.btn5)
        self.add_widget(self.btn6)

        self.btn1.bind(on_press = self.screen_transition1)

    def screen_transition1(self, *args):
        self.manager.current = 'Accounts'

class FirstWindow(Screen,App):
    def __init__(self, **kwargs):

        super(FirstWindow, self).__init__(**kwargs)
        
        self.add_widget(Label(text='Money Management System', bold = True, font_name = 'Times', font_size = 40, size_hint = (.15, .05), pos_hint={'x': 0.25, 'y': .9}))

        self.add_widget(Label(text='Name', bold = True ,font_size = 20 ,size_hint = (.15, .05), pos_hint={'x': 0.0, 'y': .70}))
        self.Name = TextInput(multiline=False, size_hint=(.50, .05), pos_hint={'x': 0.20, 'y': .70})
        self.add_widget(self.Name)

        self.add_widget(Label(text='Amount', bold = True, font_size = 20 ,size_hint = (.15, .05), pos_hint={'x': 0.0, 'y': .60}))
        self.Amount = TextInput(multiline=False, size_hint=(.50, .05), pos_hint={'x': 0.20, 'y': .60})
        self.add_widget(self.Amount)

        self.add_widget(Label(text='Date',  bold = True,  font_size = 20 ,size_hint = (.15, .05), pos_hint={'x': 0.0, 'y': .50}))
        self.Date = TextInput(multiline=False, size_hint=(.50, .05), pos_hint={'x': 0.20, 'y': .50})
        self.add_widget(self.Date)

        self.btn1 = Button(text = 'Loans',bold = True, font_size = 22, size_hint = (0.20,0.10), pos_hint = {'center_x':0.9,'center_y':0.10})
        self.btn2 = Button(text= "Save", font_size=22,bold = True, size_hint = (0.20,0.10), pos_hint = {'center_x':0.9,'center_y':0.90})
        self.btn3 = Button(text= "Update", font_size= 22,bold = True, size_hint = (0.20,0.10), pos_hint = {'center_x':0.9,'center_y':0.75})
        self.btn4 = Button(text= "Delete", font_size= 22, bold = True,size_hint = (0.20,0.10), pos_hint = {'center_x':0.9, 'center_y':0.60})
        self.btn5 = Button(text= "Display", font_size= 22,bold = True, size_hint = (0.20,0.10), pos_hint = {'center_x':0.9, 'center_y':0.45})
        self.btn6 = Button(text= "Search", font_size= 22,bold = True, size_hint = (0.20,0.10), pos_hint = {'center_x':0.9, 'center_y':0.30})

        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)
        self.add_widget(self.btn4)
        self.add_widget(self.btn5)
        self.add_widget(self.btn6)


        self.btn1.bind(on_press = self.screen_transition)
        self.btn2.bind(on_press = self.saveData)
        self.btn3.bind(on_press = self.update)
        self.btn6.bind(on_press = self.search)
        self.btn4.bind(on_press = self.delete)
        
    def screen_transition(self, *args):
        self.manager.current = 'Loans'

    def saveData(self, instance):
        name = self.Name.text
        amount = self.Amount.text
        date = self.Date.text
        
        datas = {'name': name, 'amount': amount, 'date': date}
        db.child('mainData').push(datas)

    def update(self, instance):
		firebase = pyrebase.initialize_app(firebaseConfig)
		db = firebase.database()
		totalData = db.child('mainData').get()
		for data in totalData.each():
			if data.val()['name'] == self.Name.text and data.val()['date'] == self.Name.date:
				db.child('mainData').child(data.key()).update(
					{'name': self.Name.text, 'amount': self.Amount.text, 'date': self.Date.text})
		print('Done')

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

    def delete(self,instance):
		firebase = pyrebase.initialize_app(firebaseConfig)
		db = firebase.database()
		totalData = db.child('mainData').get()
		for data in totalData.each():
			if data.val()['name'] == self.name.text and data.val()['date'] == self.name.date:
				db.child('mainData').child(data.key()).remove()
 

class MoneyMS(App):
    def build(self):
        sm = WindowManager(transition = FadeTransition())
        sm.add_widget(FirstWindow(name='Accounts'))
        sm.add_widget(SecondWindow(name='Loans'))
        return sm

if __name__=='__main__':
    MoneyMS().run()