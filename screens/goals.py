from kivy.uix.screenmanager import Screen

class GoalScreen(Screen):
    def save_goals(self):
        self.ids.status.text = "Goals saved!"
