from kivy.uix.screenmanager import Screen
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

class GraphScreen(Screen):
    def on_enter(self):
        self.ids.graph_layout.clear_widgets()

        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        steps = [3500, 4200, 5000, 4700, 5300, 6000, 5800]
        weight = [72, 71.5, 71.2, 71.1, 70.9, 70.5, 70.3]

        fig, ax1 = plt.subplots()
        ax1.set_xlabel('Days')
        ax1.set_ylabel('Steps', color='blue')
        ax1.plot(days, steps, marker='o', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')

        ax2 = ax1.twinx()
        ax2.set_ylabel('Weight (kg)', color='green')
        ax2.plot(days, weight, marker='s', color='green')
        ax2.tick_params(axis='y', labelcolor='green')

        fig.tight_layout()
        self.ids.graph_layout.add_widget(FigureCanvasKivyAgg(fig))
