from kivy.config import Config
import os
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image


# Set the window size
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

class HomeApp(Screen):
    pass

class ClickableImage(ButtonBehavior, Image):
    pass

class AdminApp(App):
    def build(self):
        # Ensure the path to the kv file is correct
        kv_file_path = os.path.join(os.path.dirname(__file__), 'kv','admin.kv')
        Builder.load_file(kv_file_path)
        return HomeApp()

if __name__ == '__main__':
    AdminApp().run()
