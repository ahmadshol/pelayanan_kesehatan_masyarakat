from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.label import Label
import os
from kivy.lang import Builder

Window.size = (360, 640)

class MyScreenManager(ScreenManager):
    pass

class LoginScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class HealthApp(App):
    def build(self):
        kv_file_path = os.path.join(os.path.dirname(__file__), 'kv','login.kv')
        Builder.load_file(kv_file_path)
        return LoginScreen

if __name__ == '__main__':
    HealthApp().run()
