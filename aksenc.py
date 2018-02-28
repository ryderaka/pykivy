# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.image import Image
#from kivy.graphics import BorderImage
from kivy.graphics import Color, Rectangle
#from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior


class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.source = 'button.jpg'


class RootScreen(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class ImageScreen(Screen):
    pass


class KivyText(App):
    def build(self):
        return RootScreen()

if __name__ == "__main__":
    KivyText().run()
