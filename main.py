import kivy

kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Rotor(BoxLayout):
    def __init__(self, **kwargs):
        super(Rotor, self ).__init__(**kwargs)
        x = 1
        button1 = Button(text="<")
        button1.bind(on_press=self._button_action)
        self.add_widget(button1)

        self.main_label = Label(text="0°")
        self.add_widget(self.main_label)

        button2 = Button(text=">")
        button2.bind(on_press=self._button_action)

        self.add_widget(button2)
    def _button_action(self, instanse: Button):
        """
            on click action of all buttons, change the value of number in this.main_label
        """
        if instanse.text == "<":
            diraction = -1
        else:
            diraction = 1
        print("diala" + str(diraction))

class MyApp(App):

    def build(self):
        self.root = root = Rotor()
        return root


if __name__ == '__main__':
    MyApp().run()

