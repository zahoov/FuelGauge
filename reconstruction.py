import kivy
import time
import random
import threading

from functools import partial
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, ListProperty
from kivy.clock import Clock

'''
The conversion factor is used to convert the raw numerical data into degrees to move the needle
default is 1.8 which works for a 0-100 slider. cf = conversion_factor
'''
cf = 1.8


class FuelGaugeLayout(Screen):
    conversion_factor = cf
    pass

class ScreenSaver(Screen):
    pass

class FuelInjectionLayout(Screen):
    conversion_factor = cf
    pass
class Change_Screen():
    name = 'third'
    ss = ScreenSaver(name=name)
    self.add_widget(ss)
    self.current = name


class MyScreenManager(ScreenManager):


    Clock.schedule_once(Change_Screen, 1)
    #delay = NumericProperty(5)






root_widget = Builder.load_string('''
MyScreenManager:
	FuelGaugeLayout:
	FuelInjectionLayout:
	ScreenSaver:

<FuelGaugeLayout>:
    name: 'first'
    BoxLayout:
	    orientation: 'vertical'

		#Slider:
		#	id: slider_dash
		#	size_hint_y: None
		#	min: 0
		#	max: 100
		#	value: 50
		#	opacity: 50

		Label:
			id: slider_dash
		    value: 50
			size_hint_y: None
			text: 'H2 Fuel Gauge'
			font_size: self.parent.width * 0.1

		Scatter:
			center: self.parent.center
			size: self.parent.width, self.parent.height
			do_rotation: False
			do_scale: False
			do_translation: False

			Image:
				id: gauge_dash
				source: 'cadran.png'
				size: self.parent.width, self.parent.height
				center: self.parent.center
			Scatter:
				do_rotation: False
				do_scale: False
				do_translation: False
				size: self.parent.width, self.parent.height
				canvas.before:
					Rotate:
						origin: root.width / 2, gauge_dash.height * 0.19
						angle: 90 - (slider_dash.value * root.conversion_factor)

				Image:
					id: needle_dash
					source: 'needle.png'
					size: self.parent.width, self.parent.height

		BoxLayout:
			orientation: 'horizontal'
			size_hint_y: None
			Button:
				font_size: self.parent.width * 0.14
				text: 'Back'
			Label:
				text: 'One'
			Button:
				font_size: self.parent.width * 0.14
				text: 'Next'
				on_release: app.root.current = 'second'

<FuelInjectionLayout>:
	name: 'second'
	BoxLayout:
		orientation: 'vertical'

		Slider:
			id: slider2_dash
			size_hint_y: None
			min: 0
			max: 100
			value: 50

		#Label:
		#	id: slider_dash
		#	value: 50
		#	size_hint_y: None
		#	text: 'H2 Fuel Gauge'
		#	font_size: self.parent.width * 0.1

		Scatter:
			center: self.parent.center
			size: self.parent.width, self.parent.height
			do_rotation: False
			do_scale: False
			do_translation: False

			Image:
				id: gauge_dash
				source: 'cadran.png'
				size: self.parent.width, self.parent.height
				center: self.parent.center
			Scatter:
				do_rotation: False
				do_scale: False
				do_translation: False
				size: self.parent.width, self.parent.height
				canvas.before:
					Rotate:
						origin: root.width / 2, gauge_dash.height * 0.19
						angle: 90 - (slider2_dash.value * root.conversion_factor)

				Image:
					id: needle_dash
					source: 'needle.png'
					size: self.parent.width, self.parent.height

		BoxLayout:
			orientation: 'horizontal'
			size_hint_y: None
			Button:
				font_size: self.parent.width * 0.14
				text: 'Back'
			Label:
				text: '%s' % int(slider2_dash.value)
				font_size: self.parent.width * 0.14
			Button:
				font_size: self.parent.width * 0.14
				text: 'Next'
				on_release: app.root.change_screen()
				

<ScreenSaver>:
    name: 'third'
    BoxLayout:
        orientation: 'vertical'
        Label:
            size_hint: None, None
            text: 'Hi'
        Label:
            text: 'Wow'

''')




class FuelGaugeApp(App):

    def build(self):

        return root_widget


FuelGaugeApp().run()
