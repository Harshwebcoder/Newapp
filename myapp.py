from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class myapp(App):
	def build(self):
		layout = BoxLayout(orientation="vertical")
		button = Button(text="click me")
		btn2 = Button(text="click here")
		layout.add_widget(button)
		layout.add_widget(btn2)
		return layout
		
myapp().run()