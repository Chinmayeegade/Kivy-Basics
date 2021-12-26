import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
class GL(GridLayout):
    pass
class GridLayoutApp(App):
    pass
GridLayoutApp().run()

"""
Alternative Code:
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
class GL(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 3
        self.cols = 3
        b1 = Button(text="A")
        b2 = Label(text="B")
        b3 = Button(text="C")
        b4 = Label(text="D")
        b5 = Button(text="E")
        b6 = Label(text="F")
        b7 = Button(text="G")
        b8 = Label(text="H")
        b9 = Button(text="I")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        self.add_widget(b4)
        self.add_widget(b5)
        self.add_widget(b6)
        self.add_widget(b7)
        self.add_widget(b8)
        self.add_widget(b9)
class MyApp(App):
    pass
MyApp().run()

#Introduce the main interface in the .kv file for the programme to function.
"""