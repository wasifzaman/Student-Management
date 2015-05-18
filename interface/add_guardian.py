import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *

add_guardian = Window(child=True, title='Add Guardian')

add_guardian.add_row()
add_guardian.add_row()
add_guardian.add_column(0)
add_guardian.add_column(0)
add_guardian.add_column(0)
add_guardian.add_column(1)
add_guardian.add_column(1)

add_guardian.add_widget_to(DefaultLabel, 0, attributes={'text': 'first name*'})
init_focus = add_guardian.add_widget_to(DefaultEntry, 0, tag='first')
add_guardian.add_widget_to(DefaultLabel, 0, attributes={'text': 'last name*'})
add_guardian.add_widget_to(DefaultEntry, 0, tag='last')
add_guardian.add_widget_to(DefaultLabel, 0, attributes={'text': 'relation'})
add_guardian.add_widget_to(DefaultEntry, 0, tag='relation')
add_guardian.add_widget_to(DefaultLabel, 1, attributes={'text': 'address 1*'})
add_guardian.add_widget_to(DefaultEntry, 1, tag='address_1')
add_guardian.add_widget_to(DefaultLabel, 1, attributes={'text': 'address 2*'})
add_guardian.add_widget_to(DefaultEntry, 1, tag='address_2')
add_guardian.add_widget_to(DefaultLabel, 1, attributes={'text': 'city*'})
add_guardian.add_widget_to(DefaultEntry, 1, tag='city')
add_guardian.add_widget_to(DefaultLabel, 1, attributes={'text': 'state*'})
add_guardian.add_widget_to(DefaultEntry, 1, tag='state')
add_guardian.add_widget_to(DefaultLabel, 1, attributes={'text': 'zipcode*'})
add_guardian.add_widget_to(DefaultEntry, 1, tag='zipcode')
add_guardian.add_widget_to(DefaultButton, 0, row_num=1, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Add Guardian'}, width=26)
add_guardian.add_widget_to(DefaultButton, 1, row_num=1, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Cancel'}, width=26)

'''
add_guardian.add_widget_to(DefaultButton, 1, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Log Out'}, image=images + 'Logout-Door-128.png')
add_guardian.add_widget_to(DefaultButton, 2, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Print'}, image=images + 'Printer-128.png')
add_guardian.add_widget_to(DefaultButton, 2, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Settings'}, image=images + 'Settings-01-128.png')
'''

init_focus.focus()