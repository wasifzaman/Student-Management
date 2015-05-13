from tkinter import *
from widgets import *

class Window(Tk):

	def __init__(self, child=False):
		if child:
			Toplevel.__init__(self)
			self.wm_state('normal')
			self.overrideredirect(1)
			self.withdraw()
		else:
			Tk.__init__(self)
			self.wm_state('zoomed')
		self.columns = {}

	def add_column(self, attributes=False):
		index = len(self.columns)
		self.columns[index] = Frame(self)
		self.columns[index].pack(side=LEFT, anchor=N, padx=10, pady=10)

	def add_widget_to(self, widget, column_num, tag=False, attributes=False, **kwargs):
		widget_ = widget(self.columns[column_num], **kwargs)
		widget_.frame.pack(anchor=W, padx=1, pady=1)
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

	def show_child_center(self):
		self.deiconify()
		screen_w = self.winfo_screenwidth()
		screen_h = self.winfo_screenheight()
		size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
		x = screen_w/2 - size[0]/2
		y = screen_h/2 - size[1]/2
		self.geometry("%dx%d+%d+%d" % (size + (x, y)))

def find_all(root, output, type_):
	if len(root.winfo_children()) == 0:
		return
	else:
		for child in root.winfo_children():
			find_all(child, output, type_)
			if type_ == 'all' or type(child) == type_:
				output.append(child)



from widgets import *
import sys, os
images = os.path.abspath(os.pardir) + '\images\\'
w = Window()
w.add_column()
w.add_column()
'''
w.add_widget_to(DefaultLabel, 0, attributes={'text': 'first name*'})
init_focus = w.add_widget_to(DefaultEntry, 0, limit_to='.2f', tag='last')
w.add_widget_to(DefaultLabel, 0, attributes={'text': 'last name*'})
w.add_widget_to(DefaultEntry, 0, tag='first', limit_to='int')
w.add_widget_to(DefaultButton, 0, exec_func=w.generate_data_table, bg='teal', fg='white', hover_bg='pink', no_text=True, image=images + 'User-Add-128.png')
w.allocate_data({'first': 'John', 'last': 'Smith'})
init_focus.focus()
'''
#print(w.generate_data_table())
#w.clear_all_widgets()
table = w.add_widget_to(Table, 0, data_table=[['test', 'test2'],['test3', 'test4']])
#table.delete_all()
table.add_row(['test5', 'test6'])
w.mainloop()
