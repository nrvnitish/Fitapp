from kivy.uix.screenmanager import Screen

class BMIScreen(Screen):
    def calculate_bmi(self):
        height = float(self.ids.height.text)/100
        weight = float(self.ids.weight.text)
        bmi = weight / (height ** 2)
        self.ids.result.text = f"Your BMI is {bmi:.2f}"
