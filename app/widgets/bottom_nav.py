from kivy.uix.boxlayout import BoxLayout

class BottomNav(BoxLayout):

    def go_home(self):
        self.parent.manager.current = "dashboard"

    def go_profile(self):
        self.parent.manager.current = "profile"
