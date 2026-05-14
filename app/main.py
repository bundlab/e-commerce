from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from app.screens.login import LoginScreen
from app.screens.dashboard import DashboardScreen
from app.screens.profile import ProfileScreen
from app.screens.settings import SettingsScreen


Builder.load_file("ui/login.kv")
Builder.load_file("ui/dashboard.kv")
Builder.load_file("ui/profile.kv")
Builder.load_file("ui/settings.kv")
Builder.load_file("ui/main.kv")

class EcommerceApp(App):

    def build(self):
        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(SettingsScreen(name="settings"))

        return sm


if __name__ == "__main__":
    EcommerceApp().run()
