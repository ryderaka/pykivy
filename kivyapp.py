# Created by thoughtchimp on 05/02/18
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
# from kivy.uix.image import Image


class Painter(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]


class MainScreen(Screen):
    # wimg = Image(source='mylogo.png')
    pass


class AnotherScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main2.kv")


class MainApp(App):

    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()







# class Widgets(Widget):
#     pass
#
# class TutorialApp(App):
#     def build(self):
#         return FloatLayout()


# class DrawInput(Widget):
#
#     def on_touch_down(self, touch):
#         print(touch)
#         with self.canvas:
#             touch.ud["line"] = Line(points=(touch.x, touch.y))
#
#     def on_touch_move(self, touch):
#         print(touch)
#         touch.ud["line"].points += (touch.x, touch.y)
#
#     def on_touch_up(self, touch):
#         print("RELEASED!",touch)
#
#
# class SimpleKivy4(App):
#
#     def build(self):
#         return DrawInput()
#
# if __name__ == "__main__":
#     SimpleKivy4().run()





# class TutorialApp(App):
#     def build(self):
#         return Label()


# class TutorialApp(App):
#     def build(self):
#         f = FloatLayout()
#         s = Scatter()
#         l = Label(text = "Hello!", font_size=150)
#         f.add_widget(s)
#         s.add_widget(l)
#         return f

# if __name__ == "__main__":
#     TutorialApp().run()
