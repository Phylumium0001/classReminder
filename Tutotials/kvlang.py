from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyApp(App):
    def build(self):
        return MyGrid()

class MyGrid(Widget):
     firstName = ObjectProperty(None)
     lastName = ObjectProperty(None)
     email = ObjectProperty(None)

     def btn(self):
        print(f' Welcome {self.firstName.text} {self.lastName.text}, \n Email :{self.email.text}')
        self.firstName.text = '' 
        self.lastName.text = '' 
        self.email.text = '' 


if __name__ == '__main__':
    app = MyApp()
    app.run()

