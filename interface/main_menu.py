import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *

w = Window()
#w.configure(background='grey')

w.add_row()
w.add_column(0)
w.add_column(0)
w.add_column(0)

#for column in w.columns.values():
#	column.configure(bg='grey')

from add_student import add_student
from add_guardian import add_guardian

w.add_widget_to(DefaultButton, 0, exec_func=add_student.show_center, bg='#2B58A6', fg='white', attributes={'text': 'Add Student'}, image=images + 'User-Add-128.png')
w.add_widget_to(DefaultButton, 0, exec_func=w.generate_data_table, bg='#2B58A6', fg='white', attributes={'text': 'Modify Student'}, image=images + 'User-Modify-128.png')
w.add_widget_to(DefaultButton, 1, exec_func=w.generate_data_table, bg='#2B58A6', fg='white', attributes={'text': 'Check In'}, image=images + 'Login-Door-128.png')
w.add_widget_to(DefaultButton, 1, exec_func=w.generate_data_table, bg='#2B58A6', fg='white', attributes={'text': 'Check Out'}, image=images + 'Logout-Door-128.png')
w.add_widget_to(DefaultButton, 2, exec_func=w.generate_data_table, bg='#2B58A6', fg='white', attributes={'text': 'Print'}, image=images + 'Printer-128.png')
w.add_widget_to(DefaultButton, 2, exec_func=w.generate_data_table, bg='#2B58A6', fg='white', attributes={'text': 'Settings'}, image=images + 'Settings-01-128.png')

w.mainloop()