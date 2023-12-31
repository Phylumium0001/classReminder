from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)

        self.cols = 1
        
        self.inside = GridLayout()
        self.inside.cols =2

        self.inside.add_widget(Label(text='First Name: '))
        self.firstName = TextInput(multiline=False)
        self.inside.add_widget(self.firstName)

        self.inside.add_widget(Label(text='Last Name: '))
        self.lastname = TextInput(multiline = False)
        self.inside.add_widget(self.lastname)

        self.add_widget(self.inside)

        self.add_widget(Button(text='Submit'))

class Myapp(App):
    def build(self):
        return MyGrid()
    
if __name__ == '__main__':
    app = Myapp()
    app.run()