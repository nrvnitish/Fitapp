from kivy.uix.screenmanager import Screen

class TrackerScreen(Screen):
    def save_tracker(self):
        self.ids.status.text = "Saved!"
        self.ids.progress.text = "Well done today!"
