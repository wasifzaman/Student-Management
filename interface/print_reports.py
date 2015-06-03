import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *

print_reports = Window(child=True, title='Add Guardian')

print_reports.add_row()
print_reports.add_column(0)

print_reports.add_widget_to(DefaultButton, 0, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Student attendance'}, width=26)
print_reports.add_widget_to(DefaultButton, 0, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Monthly attendance'}, width=26)
print_reports.add_widget_to(DefaultButton, 0, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Custom attendance'}, width=26)
print_reports.add_widget_to(DefaultButton, 0, exec_func=lambda: print_reports.hide(True), bg='#2B58A6', fg='white', attributes={'text': 'Cancel'}, width=26)