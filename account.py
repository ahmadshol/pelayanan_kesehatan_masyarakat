from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import os
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import firebase_admin
from firebase_admin import credentials, firestore

Window.size = (360, 640)

# Initialize Firebase
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class ClickableBox(ButtonBehavior, BoxLayout):
    pass

class AccountScreen(Screen):
    def on_pre_enter(self):
        self.ids.accounts_box.clear_widgets()
        users_ref = db.collection("users")
        docs = users_ref.stream()

        for doc in docs:
            user_data = doc.to_dict()
            clickable_box = ClickableBox()
            clickable_box.orientation = 'horizontal'
            clickable_box.spacing = 10
            clickable_box.padding = 10
            clickable_box.size_hint_y = None
            clickable_box.height = 70
            clickable_box.canvas.before.clear()
            with clickable_box.canvas.before:
                Color(rgba=(0.9, 0.9, 0.9, 1))
                RoundedRectangle(size=clickable_box.size, pos=clickable_box.pos, radius=[10, 10, 10, 10])
            
            image = Image(source='img/avatar.png', size_hint=(None, None), size=(50, 50))
            clickable_box.add_widget(image)
            
            box = BoxLayout(orientation='vertical', spacing=5)
            name_label = Label(text=user_data.get('name'), font_size='18sp', bold=True, size_hint_y=None, height=30, color=(0, 0, 0, 1))
            email_label = Label(text=user_data.get('email'), font_size='14sp', size_hint_y=None, height=30, color=(0, 0, 0, 1))
            box.add_widget(name_label)
            box.add_widget(email_label)
            clickable_box.add_widget(box)
            
            self.ids.accounts_box.add_widget(clickable_box)

class AccountApp(App):
    def build(self):
        kv_file_path = os.path.join(os.path.dirname(__file__), 'kv', 'account.kv')
        Builder.load_file(kv_file_path)
        return AccountScreen()

if __name__ == '__main__':
    AccountApp().run()
