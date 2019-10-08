from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class PassFail(App):
    def build(self):
        Window.size = (300, 150)
        self.title = "Pass or Fail"
        self.root = Builder.load_file('pass_fail.kv')
        return self.root

    def handle_score(self):
        score = int(self.root.ids.input_score.text)
        if 0 <= score <= 49:
            self.root.ids.output_label.text = "Fail"
        elif 50 <= score <= 64:
            self.root.ids.output_label.text = "Pass"
        elif 65 <= score <= 74:
            self.root.ids.output_label.text = "Credit"
        elif 75 <= score <= 84:
            self.root.ids.output_label.text = "Distinction"
        elif 85 <= score <= 100:
            self.root.ids.output_label.text = "High Distinction"
        else:
            self.root.ids.output_label.text = "ERROR - Score must \n between 0 and 100"

    def press_clear(self):
        self.root.ids.output_label.text = ''


PassFail().run()