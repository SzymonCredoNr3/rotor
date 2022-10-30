import kivy

kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Rotor(BoxLayout):
    def __init__(self, **kwargs):
        super(Rotor, self ).__init__(**kwargs)
        self.degree = 0
        button1 = Button(text="<")
        button1.bind(on_press=self._button_action)
        self.add_widget(button1)

        main_label = self.main_label = Label(text=f"{self.degree}°")

        self.add_widget(main_label)

        button2 = Button(text=">")
        button2.bind(on_press=self._button_action)

        self.add_widget(button2)
    def _button_action(self, instance: Button):
        """
            on click action of all buttons, change the value of number in this.main_label
        """
        if instance.text == "<":
            direction = -1
        else:
            direction = 1
        self.degree += direction
        # loop adding degrees
        if self.degree == 361:
            self.degree = 1
        if self.degree == -1:
            self.degree = 359
        self.main_label.text = f"{self.degree}°"

class MyApp(App):
    def build(self):
        self.root = root = Rotor()
        return root


if __name__ == '__main__':
    MyApp().run()

