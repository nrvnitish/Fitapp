from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.login import LoginScreen
from screens.signup import SignupScreen
from screens.home import HomeScreen
from screens.bmi import BMIScreen
from screens.workout import WorkoutScreen
from screens.diet import DietScreen
from screens.goals import GoalScreen
from screens.progress import ProgressScreen
from screens.tracker import TrackerScreen
from screens.voice import VoiceScreen
from screens.rewards import RewardScreen
from screens.graph_screen import GraphScreen

class FitnessApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignupScreen(name="signup"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(BMIScreen(name="bmi"))
        sm.add_widget(WorkoutScreen(name="workout"))
        sm.add_widget(DietScreen(name="diet"))
        sm.add_widget(GoalScreen(name="goals"))
        sm.add_widget(ProgressScreen(name="progress"))
        sm.add_widget(TrackerScreen(name="tracker"))
        sm.add_widget(VoiceScreen(name="voice"))
        sm.add_widget(RewardScreen(name="rewards"))
        sm.add_widget(GraphScreen(name="graph"))
        return sm

if __name__ == "__main__":
    FitnessApp().run()
