class Trigger():

	def __init__(self, func):
		self.var = {}
		self.func = func

	def exec_func(self):
		self.func(self.var)