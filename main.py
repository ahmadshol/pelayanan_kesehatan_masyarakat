from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("pelayanan.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

Window.size = (320, 640)

# Mendefinisikan kelas untuk setiap Screen
class BoxRounded(BoxLayout):
    pass

class ClickableImage(ButtonBehavior, Image):
    pass

class LoginScreen(Screen):
    pass

class HomeApp(Screen):
    pass

class LoginSecondScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class RegistrationScreen(Screen):
    pass

class AccountScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        # List of kv file names
        kv_files = ['main.kv', 'home.kv','login.kv','registrasi.kv','account.kv']
        # Load all kv files
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
                self.root.current = 'page_one'  # switch to admin home
            else:
                self.root.current = 'home'  # switch to user home
        else:
            popup = Popup(title='Error',
                          content=Label(text='Invalid login credentials'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            
    def register(self, name, email, password, role):
        # Save to Firestore
        doc_ref = db.collection("users").document(email)
        doc_ref.set({
            "name": name,
            "email": email,
            "password": password,
            "role": role
        })
        popup = Popup(title='Registration Successful',
                      content=Label(text=f'Registration successful for {role}'),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    MyApp().run()
