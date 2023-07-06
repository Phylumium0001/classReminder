from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ProgApp(App):
    def build(self):
        layout = BoxLayout(padding=1)
        label = Label(
            text='Hello',
            size_hint=(.5,.5),
            pos_hint={
                'center_x':.0,
                'center_y': .5
            },
            color=[1,0,0,1]
        )

        layout.add_widget(label)
        # return label

        img = Image(
            source='classReminder/img/wp2027195-straw-hats-wallpapers.jpg',
            size_hint=(1,1),
            pos_hint= {
                'center_x':0,
                'center_y':.5
            }
        )
        layout.add_widget(img)
        # return img

        btn = Button(
            text='Dont Push My Button !!!',
            size_hint = (.2,.05),
            pos_hint={
                'center_y':0.5,
                'center_x':0
            },
        )
        btn.bind(on_press=self.on_press_button)

        layout.add_widget(btn)
        # return btn
        return layout
    
    def on_press_button(self,instance):
        print('You pressed a button!!')


if __name__ == '__main__':
    app = ProgApp()
    app.run()