import kivy
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.button import Button
#Creating 100 buttons in a stacked sequence
#Using Scoll view to view all the buttons
class SL(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        var = dp(100)
        for i in range(0,500,5):
            x = Button(text=str(i+5) ,size_hint=(None, None), size=(var,var ))
            self.add_widget(x)
class Stack_ScrollApp(App):
    pass
Stack_ScrollApp().run()