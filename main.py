from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock

class SmritiApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        self.status_label = MDLabel(text="স্মৃতি AI প্রস্তুত!", halign="center", font_style="H5", theme_text_color="Custom", text_color=(0, 1, 0.8, 1))
        mic_btn = MDFloatingActionButton(icon="microphone", pos_hint={"center_x": .5}, on_release=self.process_command)
        layout.add_widget(self.status_label)
        layout.add_widget(mic_btn)
        screen.add_widget(layout)
        return screen
    def process_command(self, instance):
        self.status_label.text = "শুনছি..."
        Clock.schedule_once(self.reset_status, 3)
    def reset_status(self, dt):
        self.status_label.text = "স্মৃতি রেডি বস!"

if __name__ == '__main__':
    SmritiApp().run()
