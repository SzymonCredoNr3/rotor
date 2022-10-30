import kivy

kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Rotor(BoxLayout):
    def __init__(self, **kwargs):
        super(Rotor, self ).__init__(**kwargs)
        self.add_widget(Button(text="<"))
        self.add_widget(Label(text="0*"))
        self.add_widget(Label(text=">"))

class MyApp(App):

    def build(self):
        self.root = root = Rotor()
        return root


if __name__ == '__main__':
    MyApp().run()

