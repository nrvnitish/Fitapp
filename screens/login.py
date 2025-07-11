from kivy.uix.screenmanager import Screen

class LoginScreen(Screen):
    def do_login(self):
        self.ids.status.text = "Logged in!"
        self.manager.current = "home"
