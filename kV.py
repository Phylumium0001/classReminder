from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image

class ButtonApp(App):
    def build(self):
        return Image()
        return Button()
        
    def on_press_button(self):
        print('You pressed on the button!!!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()