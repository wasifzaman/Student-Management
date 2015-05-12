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

	def add_widget_to(self, widget, column_num, tag=False, attributes=False, **kwargs):
		widget_ = widget(self.columns[column_num], **kwargs)
		widget_.frame.pack(anchor=W)
		if tag: setattr(widget_, 'tag', tag)
		if attributes:
			for attribute, value in attributes.items():
				eval('widget_.config(' + attribute + '=' + "'" + value + "')")
		return widget_

	def find_all_tagged_widgets(self):
		tagged_widgets = []
		find_all(self, tagged_widgets, DefaultEntry)
		for widget in tagged_widgets:
			if not hasattr(widget, 'tag'): tagged_widgets.remove(widget)
		return tagged_widgets

	def generate_data_table(self):
		#all widgets will have stringvar
		tagged_widgets = self.find_all_tagged_widgets()
		data_table = {}
		
		for widget in tagged_widgets:
			if hasattr(widget, 'is_valid'):
				widget.validate()
			data_table[widget.tag] = widget.stringvar.get()

		return data_table

	def clear_all_widgets(self):
		tagged_widgets = self.find_all_tagged_widgets()
		for widget in tagged_widgets:
			widget.stringvar.set('')

	def allocate_data(self, data_table):
		tagged_widgets = self.find_all_tagged_widgets()

		for widget in tagged_widgets:
			widget.stringvar.set(data_table[widget.tag])

def find_all(root, output, type_):
	if len(root.winfo_children()) == 0:
		return
	else:
		for child in root.winfo_children():
			find_all(child, output, type_)
			if type_ == 'all' or type(child) == type_:
				output.append(child)


from widgets import *
w = Window()
w.add_column()
w.add_column()
w.add_widget_to(DefaultLabel, 0, attributes={'text': 'first name*'})
init_focus = w.add_widget_to(DefaultEntry, 0, limit_to='.2f', tag='last')
w.add_widget_to(DefaultLabel, 0, attributes={'text': 'last name*'})
w.add_widget_to(DefaultEntry, 0, tag='first', limit_to='int')
w.add_widget_to(DefaultButton, 0, exec_func=w.generate_data_table, bg='teal', fg='white', hover_bg='pink', attributes={'text': 'click me'})
#w.allocate_data({'first': 'John', 'last': 'Smith'})
#print(w.generate_data_table())
#w.clear_all_widgets()
init_focus.focus()
w.mainloop()