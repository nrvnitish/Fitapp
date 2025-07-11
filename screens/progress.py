from kivy.uix.screenmanager import Screen

class ProgressScreen(Screen):
    def save_progress(self):
        self.ids.status.text = "Progress saved!"
        self.ids.progress_result.text = "Keep going strong! 💪"
