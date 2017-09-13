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

    # def handle_calculate(self, value):



Miles_to_KilometresApp().run()