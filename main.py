from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):                   # Main Grid Layout
    def __init__(self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols = 1                       # Main Grid Layout Config

        self.inside = GridLayout()       # Inside Grid Item
        self.inside.cols=2               # Inside Grid Item Config

        self.inside.add_widget(Label(text='First Name'))
        self.firstname = TextInput(multiline=False)
        self.inside.add_widget(self.firstname)

        self.inside.add_widget(Label(text='Last Name'))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text='Email '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)      # Adding the inside grid as the first item of the main grid

        self.submit = Button(text='Submit', font_size=20, pos_hint={'center_x':.1, 'center_y':.2})
        self.submit.bind(on_press=self.pressed) # Binding button to the pressed function
        self.add_widget(self.submit)

    def pressed(self, instance):
        firstName = self.firstname.text
        lastName = self.lastname.text
        email = self.email.text

        print(f'Welcome Mr. {lastName}')
        self.firstname.text = ''
        self.lastname.text = ''
        self.email.text = ''

    
class MainApp(App):
    def build(self):
        return MyGrid()
    

if __name__ == '__main__':
    app = MainApp()
    app.run()

