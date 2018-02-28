from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout


class RootWidget(FloatLayout):
    pass


class RootScreen(ScreenManager):
    pass


class ImageScreen(Screen):
    pass


class ImageButton(ButtonBehavior, Image):
    pass
    # def on_press(self):
    #     print ('pressed')

Builder.load_string("""
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
<RootScreen>:
    transition: FadeTransition()
    RootWidget:
    ImageScreen:

<RootWidget>:
    name: "start"
    ImageButton:
        source:'button.jpg'
        size_hint: .2, .2
        on_release: root.manager.current = "image"

<ImageScreen>:
    name: "image"
    FloatLayout:
        Button:
            text: "Image!"
            size_hint: 0.4, 0.3
            pos_hint: {'center_x':.5, 'center_y':.5}
            font_size: 70
            on_release: root.manager.current  = "start"


""")


class AssignmentApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    AssignmentApp().run()
