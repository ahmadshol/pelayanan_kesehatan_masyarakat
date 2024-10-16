from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.core.window import Window
import os
from kivy.uix.popup import Popup

Window.size = (360, 640)

class RegistrationScreen(BoxLayout):
    pass

class RegistrationApp(App):
    def build(self):
        kv_file_path = os.path.join(os.path.dirname(__file__), 'kv','registrasi.kv')
        Builder.load_file(kv_file_path)
        return RegistrationScreen()
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
    RegistrationApp().run()
