# Created by thoughtchimp on 15/02/18
# -*- coding: utf-8 -*-
class ScreenButton(Button):
    screenmanager = ObjectProperty()
    def on_press(self, *args):
        super(ScreenButton, self).on_press(*args)
        self.screenmanager.current = 'whatever'

sm = ScreenManager()

sc1 = Screen(name='firstscreen')
sc1.add_widget(ScreenButton(screenmanager=sm))

sc2 = Screen(name='whatever')
sc2.add_widget(Label(text='another screen'))

sm.add_widget(sc1)
sm.add_widget(sc2)
