from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class NameLabelsApp(App):
    """ Main program - Kivy app to demo dynamic widget creation """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        self.name_list= ['Bob', 'Ryan', 'Sam', 'Jack']

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Name Labels"
        self.root = Builder.load_file('name_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for name in self.name_list:
            temp_label = Butt(text=name)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_label)

    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        # update status text
        name = instance.text
        self.status_text = "{}'s number is {}".format(name, self.phonebook[name])

    def clear_all(self):
        """
        Clear all of the widgets that are children of the "entriesBox" layout widget
        :return:
        """
        self.root.ids.entriesBox.clear_widgets()

NameLabelsApp().run()
