import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *

manual_entry = Window(child=True, title='Add Guardian')

manual_entry.add_row()
manual_entry.add_row()
manual_entry.add_column(0)
manual_entry.add_column(0)
manual_entry.add_column(0)
manual_entry.add_column(1)
manual_entry.add_column(1)

manual_entry.add_widget_to(DefaultLabel, 0, attributes={'text': 'ID*'})
init_focus = manual_entry.add_widget_to(DefaultEntry, 0, tag='id')
manual_entry.add_widget_to(DefaultLabel, 0, attributes={'text': 'Date*'})
manual_entry.add_widget_to(DefaultEntry, 0, limit_to='date')
manual_entry.add_widget_to(DefaultLabel, 0, attributes={'text': 'Time*'})
manual_entry.add_widget_to(DefaultEntry, 0, limit_to='time')
manual_entry.add_widget_to(DefaultButton, 0, row_num=1, exec_func=manual_entry.hide, bg='#2B58A6', fg='white', attributes={'text': 'Add'}, width=26)
manual_entry.add_widget_to(DefaultButton, 1, row_num=1, exec_func=lambda: manual_entry.hide(True), bg='#2B58A6', fg='white', attributes={'text': 'Cancel'}, width=26)

init_focus.focus()