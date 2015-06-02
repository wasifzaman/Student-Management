from tkinter import *
from widgets import *

class Window(Tk):

	def __init__(self, child=False, **kwargs):
		if child:
			Toplevel.__init__(self)
			self.wm_state('normal')
			self.overrideredirect(1)
			self.withdraw()
			self.title_frame = Frame(self, bg='navy')
			self.title = Label(self.title_frame, text=kwargs['title'], bg='navy', fg='white')
			self.title.pack()
			self.title_frame.pack(fill=X)
			self.outer = Frame(self, bg='navy')
			self.body = Frame(self.outer)
			self.outer.pack()
			self.body.pack(padx=1, pady=(0, 1))
		else:
			Tk.__init__(self)
			self.wm_state('zoomed')
			self.body = Frame(self)
			self.body.pack()
		self.columns = {}
		self.rows = {}

	def add_row(self):
		index = len(self.rows)
		self.rows[index] = Frame(self.body)
		self.rows[index].pack(anchor=N, padx=10, pady=10)
		self.columns[index] = {}

	def add_column(self, row_num):
		index = len(self.columns[row_num])
		self.columns[row_num][index] = Frame(self.rows[row_num])
		self.columns[row_num][index].pack(side=LEFT, anchor=N, padx=10, pady=10)

	def add_widget_to(self, widget, column_num, row_num=0, tag=False, attributes=False, **kwargs):
		widget_ = widget(self.columns[row_num][column_num], **kwargs)
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

	def show_center(self):
		self.deiconify()
		self.clear_all_widgets()
		screen_w = self.winfo_screenwidth()
		screen_h = self.winfo_screenheight()
		size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
		x = screen_w/2 - size[0]/2
		y = screen_h/2 - size[1]/2
		self.geometry("%dx%d+%d+%d" % (size + (x, y)))
		self.grab_set()

	def hide(self, cancel=False):
		self.withdraw()
		if hasattr(self, 'parent_win'):
			self.parent_win.grab_set()
			self.parent_win.focus_set()
		if not cancel and hasattr(self, 'return_to_var'):
			self.return_to_var.var.clear()
			self.return_to_var.var.update(self.retrieve_data())
			self.return_to_var.exec_func()

	def retrieve_data(self):
		tagged_widgets = self.find_all_tagged_widgets()
		data_table = {}

		for widget in tagged_widgets:
			data_table[widget.tag] = widget.stringvar.get()

		return data_table

	def link_window(self, variable, window):
		setattr(window, 'return_to_var', variable)
		setattr(window, 'parent_win', self)
		#or dictionary of return variables
		#return data to multiple windows
		return

def find_all(root, output, type_):
	if len(root.winfo_children()) == 0:
		return
	else:
		for child in root.winfo_children():
			find_all(child, output, type_)
			if type_ == 'all' or type(child) == type_:
				output.append(child)



'''
from widgets import *
import sys, os
images = os.path.abspath(os.pardir) + '\images\\'
test_win = Window()
test_win.add_row()
test_win.add_column(0)
test_win.add_column(0)
test_win.add_widget_to(DefaultLabel, 0, attributes={'text': 'first name*'})
init_focus = test_win.add_widget_to(DefaultEntry, 0, limit_to='.2f', tag='last')
test_win.add_widget_to(DefaultLabel, 0, attributes={'text': 'last name*'})
test_win.add_widget_to(DefaultEntry, 0, tag='first', limit_to='int')
test_win.add_widget_to(DefaultButton, 0, exec_func=test_win.generate_data_table, bg='teal', fg='white', hover_bg='pink', no_text=True, image=images + 'User-Add-128.png')
test_win.allocate_data({'first': 'John', 'last': 'Smith'})
init_focus.focus()
'''
#print(test_win.generate_data_table())
#test_win.clear_all_widgets()
#table = test_win.add_widget_to(Table, 0, data_table=[['test', 'test2'],['test3', 'test4']])
#table.canvas.config(width=200, height=200)
#table.delete_all()
#for i in range(0, 100):
	#table.add_row(['test5', 'test6'])

'''
of = Frame(test_win)
of.pack()
c = Canvas(of, width=500, height=500, bg='red')
f = Frame(c)
c.create_window((0,0), window=f, anchor=NW)
l = Frame(f)
l.grid()
Label(l, text='test').grid()
c.grid()
xscrollbar = Scrollbar(of, orient="horizontal", command=c.xview)
yscrollbar = Scrollbar(of, orient="vertical", command=c.yview)
yscrollbar.grid(row=0, column=1, sticky=NS)
xscrollbar.grid(row=1, column=0, sticky=EW)
test_win.mainloop()
'''
