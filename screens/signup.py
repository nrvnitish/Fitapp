from kivy.uix.screenmanager import Screen

class SignupScreen(Screen):
    def do_signup(self):
        self.manager.current = "login"
