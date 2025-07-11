from kivy.uix.screenmanager import Screen

class RewardScreen(Screen):
    def on_pre_enter(self):
        self.ids.week_box.text = "🎁 Weekly Surprise: Tap to claim!"
        self.ids.month_box.text = "🎉 Monthly Treat: Tap to claim!"

    def claim_week(self):
        self.ids.week_box.text = "✅ Claimed this week!"

    def claim_month(self):
        self.ids.month_box.text = "✅ Monthly treat claimed!"
