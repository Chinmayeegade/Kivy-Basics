#Anchor Layout is used to define the position if another layout embedded within it
#The embedded layout can be at the right-bottom/right-top/right-center/left-bottom/left-top/left-center/center-bottom/center-top/center-center
#File:main.py
import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
class AL(AnchorLayout):
    pass
class AnchorLayoutApp(App):
    pass
AnchorLayoutApp().run()