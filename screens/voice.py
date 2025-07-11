from kivy.uix.screenmanager import Screen

class VoiceScreen(Screen):
    def recognize_command(self):
        self.ids.voice_output.text = "Voice recognized: Start workout"
