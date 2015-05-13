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