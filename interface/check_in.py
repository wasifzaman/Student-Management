import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *
from trigger import Trigger

check_in = Window(child=True, title='Check-in')

check_in.add_row()
check_in.add_row()
check_in.add_row()
check_in.add_row()
check_in.add_column(0)
check_in.add_column(0)
check_in.add_column(0)
check_in.add_column(0)
check_in.add_column(0)
check_in.add_column(1)
check_in.add_column(1)
check_in.add_column(2)
check_in.add_column(2)
check_in.add_column(3)

from manual_entry import manual_entry

def remove_from_guardians(): #remove attendance?
	if guardian_list.selected != None:
		guardian_list.delete_row(guardian_list.selected)

check_in.link_window(Trigger(True), manual_entry)

check_in.add_widget_to(DefaultLabel, 0, attributes={'text': 'Search for:'})
init_focus = check_in.add_widget_to(DefaultEntry, 1)
check_in.add_widget_to(DefaultLabel, 2, attributes={'text': 'By:'})
check_in.add_widget_to(DefaultEntry, 3) #drop down
check_in.add_widget_to(DefaultButton, 4, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Search'}, width=17)
check_in.add_widget_to(DefaultLabel, 0, row_num=1, attributes={'text': 'ID'})
check_in.add_widget_to(DefaultEntry, 0, row_num=1, tag='id')
check_in.add_widget_to(DefaultLabel, 0, row_num=1, attributes={'text': 'First name'})
check_in.add_widget_to(DefaultEntry, 0, row_num=1, tag='first')
check_in.add_widget_to(DefaultLabel, 0, row_num=1, attributes={'text': 'Last name'})
check_in.add_widget_to(DefaultEntry, 0, row_num=1, tag='last')
attendance = check_in.add_widget_to(Table, 1, row_num=1) #show weekly attendance only
check_in.add_widget_to(DefaultButton, 0, row_num=2, exec_func=lambda: True, bg='#2B58A6', fg='white', attributes={'text': 'Check-in'}, width=26)
check_in.add_widget_to(DefaultButton, 1, row_num=2, exec_func=manual_entry.show_center, bg='#2B58A6', fg='white', attributes={'text': 'Manual entry'}, width=26)
check_in.add_widget_to(DefaultButton, 0, row_num=3, exec_func=lambda: check_in.hide(True), bg='#2B58A6', fg='white', attributes={'text': 'Close'}, width=26)

attendance.set_canvas_dim(width=600, height=400)

attendance.add_header(['Date', 'Actual time', 'Rounded time'])
attendance.set_width(0, 13)
attendance.set_width(1, 14)
attendance.set_width(2, 14)

init_focus.focus()