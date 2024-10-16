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
from firebase_admin import credentials, firestore, auth
from kivy.graphics import Color, RoundedRectangle

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

class AdminScreen(Screen):
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
        try:
            # Attempt to retrieve user from Firebase Authentication
            user = auth.get_user_by_email(email)

            # Here you should authenticate the user with the password (handled by Firebase Client SDK)
            # This example assumes the user already exists and has been authenticated

            # Fetch the user's role from Firestore
            doc_ref = db.collection("users").document(user.uid)
            doc = doc_ref.get()
            if doc.exists:
                role = doc.to_dict().get("role")
                if role == "admin":
                    self.root.current = 'login'  # switch to admin home
                else:
                    self.root.current = 'home'  # switch to user home
            else:
                popup = Popup(title='Error',
                              content=Label(text='User role not found'),
                              size_hint=(None, None), size=(400, 200))
                popup.open()
        except firebase_admin.exceptions.FirebaseError as e:
            popup = Popup(title='Error',
                          content=Label(text=f'Authentication failed: {e}'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
        except Exception as e:
            popup = Popup(title='Error',
                          content=Label(text=str(e)),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            
    def register(self, name, email, password, role):
        try:
            # Create user in Firebase Authentication
            user = auth.create_user(
                email=email,
                password=password
            )

            # Save user data to Firestore
            doc_ref = db.collection("users").document(user.uid)
            doc_ref.set({
                "name": name,
                "email": email,
                "role": role
            })

            popup = Popup(title='Registration Successful',
                          content=Label(text=f'Registration successful for {role}'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
        except Exception as e:
            popup = Popup(title='Registration Failed',
                          content=Label(text=str(e)),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            
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

    def goto_home(self, email):
        print(f"Account clicked: {email}")  # Debug print for account click
        self.manager.current = 'home'

if __name__ == '__main__':
    MyApp().run()
