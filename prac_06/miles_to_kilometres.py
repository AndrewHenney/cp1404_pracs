from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class Miles_to_KilometresApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = int(value) * 1.60934
        except ValueError:
            result = 0.0
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value, number):
        try:
            result = int(value) + number
        except ValueError:
            result = number

        self.root.ids.input_number.text = str(result)



Miles_to_KilometresApp().run()