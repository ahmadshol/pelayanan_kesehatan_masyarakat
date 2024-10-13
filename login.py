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
# Main Screen Logic
class MainScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

# Main App Class
class HealthApp(App):
    def build(self):
        sm = ScreenManager()
        # Load the .kv file
        kv_file_path = os.path.join(os.path.dirname(__file__), 'kv', 'main.kv')
        print(f"Loading KV file from {kv_file_path}")  # Debugging line
        Builder.load_file(kv_file_path)
        # Add screens after loading the kv file
        return sm

if __name__ == '__main__':
    HealthApp().run()
