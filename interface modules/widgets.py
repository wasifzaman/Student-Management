from tkinter import *
from PIL import Image, ImageTk

class DefaultEntry(Entry):

	def __init__(self, parent, limit_to=False, required=False): #required - temp
		self.frame = Frame(parent, bg='lightgrey')
		self.stringvar = StringVar()
		Entry.__init__(self, self.frame, textvariable=self.stringvar, relief=FLAT)
		self.pack(padx=2, pady=2)
		self.required = required #test
		if limit_to:
			self.limit_to = limit_to
			self.is_valid = False
			self.bind("<FocusOut>", lambda event: self.validate())

	def validate(self):
		if self.limit_to == 'int':
			try:
				int(self.stringvar.get())
				self.frame.config(bg='lightgreen')
				self.is_valid = True
			except ValueError:
				self.frame.config(bg='red')
				self.is_valid = False
		elif self.limit_to == '.2f':
			try:
				self.stringvar.set('%.2f' % float(self.stringvar.get()))
				self.frame.config(bg='lightgreen')
				self.is_valid = True
			except ValueError:
				self.frame.config(bg='red')
				self.is_valid = False
		elif self.limit_to == 'date':
			return

class DefaultLabel(Label):
	
	def __init__(self, parent, limit_to=False):
		self.frame = Frame(parent)
		Label.__init__(self, self.frame)
		self.pack()

class DefaultButton(Label):

	def __init__(self, parent, bg, fg, exec_func, image=False, no_text=False,
		hover_image=False, hover_fg=False, hover_bg=False, limit_to=False, width=False):
		self.frame = Frame(parent)
		Label.__init__(self, self.frame)
		if not no_text: self.pack(fill=X)
		self.bg = bg
		self.fg = fg
		self.hover_bg = hover_bg
		self.hover_fg = hover_fg
		self.config(bg=self.bg, fg=self.fg)
		self.bind("<Enter>", self.hover_on)
		self.bind("<Leave>", self.hover_off)
		self.bind("<Button-1>", lambda event: self.execute(exec_func))
		if image:
			self.picture = Image.open(image)
			self.image = ImageTk.PhotoImage(self.picture)
			self.img_label = Label(self.frame, bg=self.bg)
			self.img_label.pack()
			self.img_label.config(image=self.image)
			self.img_label.bind('<Button-1>', lambda event: self.execute(exec_func))
		if width: self.config(width=width)

	def execute(self, exec_func):
		self.focus_set()
		exec_func()

	def hover_on(self, event):
		#self.frame.config(bg=self.hover_bg)
		if self.hover_bg: self.config(bg=self.hover_bg)

	def hover_off(self, event):
		#self.frame.config(bg=self.bg)
		self.config(bg=self.bg)

class DefaultList(Listbox):

	def __init__(self, parent, width=False):
		self.frame = Frame(parent, bg='lightgrey')
		Listbox.__init__(self, self.frame, relief=FLAT)
		self.pack(padx=2, pady=2)
		if width: self.config(width=width)
		#add scrolling
		#bind selection

	def add(self, data):
		self.insert(END, data['display'])
		return

	def remove(self):
		self.delete()
		return

class Table():

	#add scrollbars
	#add window size

	def __init__(self, parent, data_table=[[]]):
		self.frame = Frame(parent, bg='lightgrey')
		self.selected = None
		self.labels = []
		for row in data_table:
			row_labels = []
			for data in row:
				row_labels.append(
					self.add_cell(data_table.index(row), row.index(data), data))
			self.labels.append(row_labels)

	def add_cell(self, row, column, data):
		cell = Frame(self.frame, bg='white')
		label = Label(cell, text=data, justify=LEFT, bg='white')
		cell.grid(row=row, column=column, sticky=EW)
		label.pack(anchor=W)
		label.bind('<Button-1>', lambda event: self.select_row(row))
		return cell

	def add_row(self, data):
		row_labels = []
		for data_ in data:
			row_labels.append(
				self.add_cell(len(self.labels), data.index(data_), data_))
		self.labels.append(row_labels)

	def delete_row(self, row_num):	
		for label in self.labels[row_num]:
			label.destroy()
		self.labels.pop(row_num)

	def delete_all(self):
		while len(self.labels) > 0:
			self.delete_row(0)

	def select_row(self, row_num):
		if self.selected != None:
			for label in self.labels[self.selected]:
				cell = label.winfo_children()[0]
				label.config(bg='white')
				cell.config(bg='white', fg='black')
		for label in self.labels[row_num]:
			cell = label.winfo_children()[0]
			label.config(bg='blue')
			cell.config(bg='blue', fg='white')
		self.selected = row_num