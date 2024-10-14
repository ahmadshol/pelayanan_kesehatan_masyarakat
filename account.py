from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import os
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

Window.size = (360, 640)

class AccountScreen(Screen):
    pass

class AccountApp(App):
    def build(self):
        kv_file_path = os.path.join(os.path.dirname(__file__), 'kv','main.kv')
        Builder.load_file(kv_file_path)
        return AccountScreen()

if __name__ == '__main__':
    AccountApp().run()
