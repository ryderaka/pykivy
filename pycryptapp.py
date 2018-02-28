# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty

kv_str = """
MyScreenManager:
    BRANCH:
        name: 'branch'
    S1:
        name: 'screen1'
    S2:
        name: 'screen2'
    S3:
        name: 'screen3'
    S4:
        name: 'screen4'
    FINAL_SCREEN:
        id: final
        name: 'final_screen'

<BRANCH>
    FloatLayout:
    Button:
        text: 'Text'
        color: 1.0, 0.6, 0.0, 1
        font_size: 25
        size_hint_x: 0.85
        size_hint_y: 0.20
        pos_hint: {'x': 0.08, 'y': 0.71}
        background_color: (0.749, 0.764, 0.035, 1.0)
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'screen1'
    Button:
        text: 'Image'
        color: 1.0, 0.6, 0.0, 1
        font_size: 25
        size_hint_x: 0.85
        size_hint_y: 0.20
        pos_hint: {'x': 0.08, 'y': 0.49}
        background_color: (0.125, 0.337, 0.533, 1.0)
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'screen2'
    Button:
        text: 'Docs'
        color: 1.0, 0.6, 0.0, 1
        font_size: 25
        size_hint_x: 0.85
        size_hint_y: 0.20
        pos_hint: {'x': 0.08, 'y': 0.27}
        background_color: (0.317, 0.474, 0.207, 1.0)

        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'screen3'
    Button:
        text: 'More...'
        color: 1.0, 0.6, 0.0, 1
        font_size: 25
        size_hint_x: 0.85
        size_hint_y: 0.20
        pos_hint: {'x': 0.08, 'y': 0.05}
        background_color: (0.576, 0.133, 0.101, 1.0)
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'screen4'

<S1>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'All about Text'
            color: 1, 1, 1, 1
        Button:
            text: 'Back'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.10
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = root.manager.previous()
                root.manager.ids.final.previous = root.name
<S2>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'All about Images'
            color: 1, 1, 1, 1
        Button:
            text: 'Back'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.10
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'branch'
                root.manager.ids.final.previous = root.name
<S3>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'All about Documents'
            color: 1, 1, 1, 1
        Button:
            text: 'Back'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.10
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'branch'
                root.manager.ids.final.previous = root.name

<S4>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'Coming Soon...'
            color: 1, 1, 1, 1
        Button:
            text: 'Back'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.10
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'branch'
                root.manager.ids.final.previous = root.name

<FINAL_SCREEN>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'Final Screen'
            color: 1, 1, 1, 1
        Button:
            text: 'Back'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = root.manager.previous()

"""


class MyScreenManager(ScreenManager):
    pass


# Branch Screen, takes you to S1, S2, or S3
class BRANCH(Screen):
    pass


class S1(Screen):
    pass


class S2(Screen):
    pass


class S3(Screen):
    pass


class S4(Screen):
    pass


class FINAL_SCREEN(Screen):
    previous = StringProperty()


class MainApp(App):
    def build(self):
        return Builder.load_string(kv_str)

if __name__ == '__main__':
    MainApp().run()
