from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.lang import Builder
import os
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("pelayanan.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

Window.size = (360, 640)

class MyScreenManager(ScreenManager):
    pass

class LoginScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class HealthApp(App):
    def build(self):
        kv_files = ['login.kv']  # List more .kv files as needed
        for kv_file in kv_files:
            kv_file_path = os.path.join(os.path.dirname(__file__), 'kv', kv_file)
            Builder.load_file(kv_file_path)
        return MyScreenManager()

    def login(self, email, password):
        # Save to Firestore
        doc_ref = db.collection("users").document(email)
        doc_ref.set({
            "email": email,
            "password": password
        })

        # Check role
        doc = doc_ref.get()
        if doc.exists:
            role = doc.to_dict().get("role")
            if role == "admin":
                self.root.current = 'admin_home'  # switch to admin home
            else:
                self.root.current = 'user_home'  # switch to user home
        else:
            popup = Popup(title='Error',
                          content=Label(text='Invalid login credentials'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()

if __name__ == '__main__':
    HealthApp().run()
