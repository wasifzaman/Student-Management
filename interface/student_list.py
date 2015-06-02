import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *

student_list = Window(child=True, title='Add Student')

student_list.add_row()
student_list.add_row()
student_list.add_column(0)
student_list.add_column(0)
student_list.add_column(0)
student_list.add_column(0)
student_list.add_column(1)
student_list.add_column(1)

from add_guardian import add_guardian
from add_payment import add_payment
from trigger import Trigger

student_list.add_widget_to(DefaultLabel, 0, attributes={'text': 'Search for:'})
student_list.add_widget_to(DefaultEntry, 0)
student_list.add_widget_to(DefaultLabel, 0, attributes={'text': 'By'})
student_list.add_widget_to(DefaultEntry, 0) #drop down
student_list.add_widget_to(DefaultButton, 0, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Search'}, width=17)
student_list_ = student_list.add_widget_to(Table, 2)
student_list.add_widget_to(DefaultButton, 1, row_num=1, exec_func=lambda: student_list.hide(True), bg='#2B58A6', fg='white', attributes={'text': 'Close'}, width=26)

student_list_.set_canvas_dim(width=500, height=500)

student_list_.add_header(['ID', 'First name', 'Last name'])
student_list_.set_width(0, 10)
student_list_.set_width(1, 13)
student_list_.set_width(2, 14)