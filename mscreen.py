# Created by thoughtchimp on 16/02/18
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
    FINAL_SCREEN:
        id: final
        name: 'final_screen'


<BRANCH>
    FloatLayout:
    Button:
        text: 'Screen-1'
        color: 1.0, 0.6, 0.0, 1
        font_size: 30
        size_hint_x: 0.50
        size_hint_y: 0.25
        pos_hint: {'x': 0.20, 'y': 0.75}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'screen1'
    Button:
        text: 'Screen-2'
        color: 1.0, 0.6, 0.0, 1
        font_size: 30
        size_hint_x: 0.50
        size_hint_y: 0.25
        pos_hint: {'x': 0.20, 'y': 0.40}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'screen2'
    Button:
        text: 'Screen-3'
        color: 1.0, 0.6, 0.0, 1
        font_size: 30
        size_hint_x: 0.50
        size_hint_y: 0.25
        pos_hint: {'x': 0.20, 'y': 0.05}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'screen3'
<S1>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'this is SCREEN-1'
            color: 1, 1, 1, 1
        Button:
            text: 'Forward'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'final_screen'
                root.manager.ids.final.previous = root.name
<S2>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'me este SCREEN-2'
            color: 1, 1, 1, 1
        Button:
            text: 'Onward'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'final_screen'
                root.manager.ids.final.previous = root.name
<S3>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'something SCREEN-3'
            color: 1, 1, 1, 1
        Button:
            text: 'Lets Go'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'final_screen'
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

class FINAL_SCREEN(Screen):
    previous = StringProperty()


class MAINApp(App):
    def build(self):
        return Builder.load_string(kv_str)

if __name__ == '__main__':
    MAINApp().run()