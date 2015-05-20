import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *

add_student = Window(child=True, title='Add Student')

add_student.add_row()
add_student.add_row()
add_student.add_column(0)
add_student.add_column(0)
add_student.add_column(0)
add_student.add_column(0)
add_student.add_column(1)
add_student.add_column(1)

from add_guardian import add_guardian

add_student.add_widget_to(DefaultLabel, 0, attributes={'text': 'first name*'})
init_focus = add_student.add_widget_to(DefaultEntry, 0, tag='first')
add_student.add_widget_to(DefaultLabel, 0, attributes={'text': 'last name*'})
add_student.add_widget_to(DefaultEntry, 0, tag='last')
add_student.add_widget_to(DefaultLabel, 0, attributes={'text': 'date of birth'})
add_student.add_widget_to(DefaultEntry, 0, limit_to='date', tag='dob')
add_student.add_widget_to(DefaultLabel, 1, attributes={'text': 'address 1*'})
add_student.add_widget_to(DefaultEntry, 1, tag='address_1')
add_student.add_widget_to(DefaultLabel, 1, attributes={'text': 'address 2*'})
add_student.add_widget_to(DefaultEntry, 1, tag='address_2')
add_student.add_widget_to(DefaultLabel, 1, attributes={'text': 'city*'})
add_student.add_widget_to(DefaultEntry, 1, tag='city')
add_student.add_widget_to(DefaultLabel, 1, attributes={'text': 'state*'})
add_student.add_widget_to(DefaultEntry, 1, tag='state')
add_student.add_widget_to(DefaultLabel, 1, attributes={'text': 'zipcode*'})
add_student.add_widget_to(DefaultEntry, 1, tag='zipcode')
guardian_list = add_student.add_widget_to(Table, 2)
add_student.add_widget_to(DefaultButton, 2, exec_func=add_guardian.show_center, bg='#2B58A6', fg='white', attributes={'text': 'Add Guardian'}, width=26)
add_student.add_widget_to(DefaultButton, 2, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Remove Guardian'}, width=26)
payment_list = add_student.add_widget_to(Table, 3)
add_student.add_widget_to(DefaultButton, 3, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Add Payment'}, width=26)
add_student.add_widget_to(DefaultButton, 3, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Remove Payment'}, width=26)
add_student.add_widget_to(DefaultButton, 0, row_num=1, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Add Student'}, width=26)
add_student.add_widget_to(DefaultButton, 1, row_num=1, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Cancel'}, width=26)

guardian_list.canvas.config(width=200, height=200)
payment_list.canvas.config(width=200, height=200)
'''
add_student.add_widget_to(DefaultButton, 1, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Log Out'}, image=images + 'Logout-Door-128.png')
add_student.add_widget_to(DefaultButton, 2, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Print'}, image=images + 'Printer-128.png')
add_student.add_widget_to(DefaultButton, 2, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Settings'}, image=images + 'Settings-01-128.png')
'''

init_focus.focus()