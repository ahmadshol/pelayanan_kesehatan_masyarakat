from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.window import Window
import os

Window.size = (360,640)

class DataLansiaApp(App):
    def build(self):
        kv_file_path = os.path.join(os.path.dirname(__file__), 'kv','main.kv')
        Builder.load_file(kv_file_path)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title_layout = BoxLayout(size_hint_y=None, height=50)
        title_layout.add_widget(Label(text='Data Lansia', font_size='24sp', bold=True))
        layout.add_widget(title_layout)
        
        # Profile section
        profile_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=10)
        avatar = Image(source='avatar.png', size_hint_x=None, width=100)  # Replace with the path to your avatar image
        profile_layout.add_widget(avatar)
        
        name = Label(text='Rohmad Rafi', font_size='18sp', valign='middle')
        profile_layout.add_widget(name)
        
        layout.add_widget(profile_layout)
        
        # Data fields
        fields = ['Tinggi Badan', 'Berat Badan', 'Tekanan Darah', 'Kadar gula darah', 'Kolestrol', 'Riwayat Penyakit']
        for field in fields:
            field_layout = BoxLayout(size_hint_y=None, height=40)
            field_label = Label(text=field, font_size='16sp')
            field_layout.add_widget(field_label)
            layout.add_widget(field_layout)
        
        return layout

if __name__ == '__main__':
    DataLansiaApp().run()
