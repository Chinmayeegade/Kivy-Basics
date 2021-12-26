#The following code produces a grid of 3 elements:
#1)Switch: Can be Set to ON or OFF position
#2)Slider : Can only be moved up/down when the switch is ON
#3)Box Layout: (a) Label: Displays the value of the slider
              # (b) Progrss Bar: Progesses according to the Slider Value

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
class SSPB(GridLayout):
    def switch_active(self,widget):
        pass
    def on_slider_value(self,widget):
        pass
class Switch_Slider_ProgressBarApp(App):
    pass
Switch_Slider_ProgressBarApp().run()