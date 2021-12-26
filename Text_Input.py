#The following code produces a grid of 2 elements:
#1)Input Box: Text can be entered
#2)Label: The entered text will be displayed on clicking the enter key

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
class TI(GridLayout):
    my_text = StringProperty("0")
    text_input_str = StringProperty("")
    def on_text_validate(self,widget):
        self.text_input_str = widget.text
class Text_InputApp(App):
    pass
Text_InputApp().run()