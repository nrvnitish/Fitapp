from kivy.uix.screenmanager import Screen

class WorkoutScreen(Screen):
    workouts = []

    def add_workout(self):
        w = self.ids.new_workout.text
        if w:
            self.workouts.append(w)
            self.ids.workout_list.text = "\n".join(self.workouts)
            self.ids.new_workout.text = ""
