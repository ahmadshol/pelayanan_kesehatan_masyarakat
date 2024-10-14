from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.core.window import Window
import os

Window.size = (360, 640)

class RegistrationScreen(BoxLayout):
    pass

class RegistrationApp(App):
    def build(self):
        kv_file_path = os.path.join(os.path.dirname(__file__), 'kv','main.kv')
        Builder.load_file(kv_file_path)
        return RegistrationScreen()

if __name__ == '__main__':
    RegistrationApp().run()
