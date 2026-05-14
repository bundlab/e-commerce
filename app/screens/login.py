from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):

    def login(self):
        self.manager.current = "dashboard"