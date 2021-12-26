#The following code produces a grid of 3 elements:
#1)Toggle Button: Can be Set to ON or OFF position
#2)Button: Can only be clicked when the toggle button is ON
#3)Label: Displays the number of times the Button had be clicked

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty, StringProperty
class Enabling_Button_Click(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("0")
    text_input_str = StringProperty("")
    def on_button_clicked(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)
    def on_toggle_press(self,widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True
class Toggle_ClickApp(App):
    pass
Toggle_ClickApp().run()
