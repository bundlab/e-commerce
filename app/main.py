from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.profile import ProfileScreen
from screens.settings import SettingsScreen
from kivy.lang import Builder

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
