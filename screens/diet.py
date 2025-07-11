from kivy.uix.screenmanager import Screen

class DietScreen(Screen):
    diet_items = []

    def add_diet_item(self):
        item = self.ids.new_diet.text
        if item:
            self.diet_items.append(item)
            self.ids.diet_list.text = "\n".join(self.diet_items)
            self.ids.new_diet.text = ""
