import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *

settings = Window(child=True, title='Add Guardian')

settings.add_row()
settings.add_column(0)

settings.add_widget_to(DefaultButton, 0, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Change database'}, width=26)
settings.add_widget_to(DefaultButton, 0, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Manage users'}, width=26)
settings.add_widget_to(DefaultButton, 0, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Check log'}, width=26)
settings.add_widget_to(DefaultButton, 0, exec_func=lambda: settings.hide(True), bg='#2B58A6', fg='white', attributes={'text': 'Cancel'}, width=26)