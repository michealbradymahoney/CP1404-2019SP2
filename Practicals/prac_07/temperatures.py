from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class TempConvertor(App):
    def build(self):
        Window.size = (640, 150)
        self.title = "Temperature Converter"
        self.root = Builder.load_file('temperatures.kv')
        return self.root

    def handle_celsius(self):
        celsius = int(self.root.ids.input_temp.text)
        fahrenheit = celsius * 9.0 / 5 + 32
        self.root.ids.output_label.text = str(fahrenheit)

    def handle_fahrenheit(self):
        fahrenheit = int(self.root.ids.input_temp.text)
        celsius = 5 / 9 * (fahrenheit - 32)
        self.root.ids.output_label.text = str(celsius)

    def press_clear(self):
        self.root.ids.output_label.text = ''
        self.root.ids.input_temp.text = ''

TempConvertor().run()
