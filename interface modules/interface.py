from tkinter import *

class Window(Tk):

	def __init__(self):
		Tk.__init__(self)
		self.wm_state('zoomed')
		self.columns = {}

	def add_column(self, attributes=False):
		index = len(self.columns)
		self.columns[index] = Frame(self)
		self.columns[index].pack(side=LEFT, anchor=N, padx=10, pady=10)

	def add_widget_to(self, widget, column_num, tag=False, attributes=False):
		widget_ = widget(self.columns[column_num])
		widget_.pack(anchor=W)
		if tag: setattr(widget_, 'tag', tag)
		if attributes:
			for attribute, value in attributes.items():
				eval('widget_.config(' + attribute + '=' + "'" + value + "')")

w = Window()
w.add_column()
w.add_column()
w.add_widget_to(Label, 0, attributes={'text': 'first name'})
w.add_widget_to(Entry, 0, attributes={'bg': 'yellow'})
w.add_widget_to(Label, 0, attributes={'text': 'last name'})
w.add_widget_to(Entry, 0, attributes={'bg': 'red'})
w.mainloop()