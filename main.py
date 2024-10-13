from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


Window.size = (320, 640)

# Mendefinisikan kelas untuk setiap Screen
class LoginScreen(Screen):
    pass

class HomeApp(Screen):
    pass

class LoginSecondScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        kv_file_path = os.path.join(os.path.dirname(__file__), 'kv','main.kv')
        Builder.load_file(kv_file_path)
        return MyScreenManager()

if __name__ == '__main__':
    MyApp().run()
