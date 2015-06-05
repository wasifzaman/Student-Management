import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *
from trigger import Trigger

change_database = Window(child=True, title='Add Student')

change_database.add_row()
change_database.add_row()
change_database.add_column(0)
change_database.add_column(0)
change_database.add_column(1)

database_list = change_database.add_widget_to(Table, 0)
change_database.add_widget_to(DefaultButton, 1, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Set current databse'}, width=17)
change_database.add_widget_to(DefaultButton, 1, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'View encryption key'}, width=17)
change_database.add_widget_to(DefaultButton, 1, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Create new database'}, width=17)
change_database.add_widget_to(DefaultButton, 1, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Delete database'}, width=17)
change_database.add_widget_to(DefaultButton, 0, row_num=1, exec_func=lambda: change_database.hide(True), bg='#2B58A6', fg='white', attributes={'text': 'Close'}, width=26)

database_list.set_canvas_dim(width=500, height=500)

database_list.add_header(['✓', 'Name', 'Students', 'File path'])
database_list.set_width(0, 4)
database_list.set_width(1, 15)
database_list.set_width(2, 13)
database_list.set_width(3, 35)