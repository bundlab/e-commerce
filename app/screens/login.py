from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):

    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        if username == "admin":
            self.manager.current = "dashboard"
