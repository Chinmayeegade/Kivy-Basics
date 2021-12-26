#To display and image in a kivy GUI, the image file must be saved within the project file in the form of a .png or .jpg file

import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
class Images(AnchorLayout):
    pass
class ImageApp(App):
    pass
ImageApp().run()
