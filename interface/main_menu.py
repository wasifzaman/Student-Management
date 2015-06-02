import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *
from trigger import Trigger

main_window = Window()
#main_window.configure(background='grey')

main_window.add_row()
main_window.add_column(0)
main_window.add_column(0)
main_window.add_column(0)

#for column in main_window.columns.values():
#	column.configure(bg='grey')

from add_student import add_student
from add_guardian import add_guardian
from student_list import student_list

main_window.link_window(Trigger(lambda: True), add_student)
main_window.link_window(Trigger(lambda: True), student_list)

main_window.add_widget_to(DefaultButton, 0, exec_func=add_student.show_center, bg='#2B58A6', fg='white', attributes={'text': 'Add Student'}, image=images + 'User-Add-128.png')
main_window.add_widget_to(DefaultButton, 0, exec_func=student_list.show_center, bg='#2B58A6', fg='white', attributes={'text': 'Modify Student'}, image=images + 'User-Modify-128.png')
main_window.add_widget_to(DefaultButton, 1, exec_func=main_window.generate_data_table, bg='#2B58A6', fg='white', attributes={'text': 'Check In'}, image=images + 'Login-Door-128.png')
main_window.add_widget_to(DefaultButton, 1, exec_func=main_window.generate_data_table, bg='#2B58A6', fg='white', attributes={'text': 'Check Out'}, image=images + 'Logout-Door-128.png')
main_window.add_widget_to(DefaultButton, 2, exec_func=main_window.generate_data_table, bg='#2B58A6', fg='white', attributes={'text': 'Print'}, image=images + 'Printer-128.png')
main_window.add_widget_to(DefaultButton, 2, exec_func=main_window.generate_data_table, bg='#2B58A6', fg='white', attributes={'text': 'Settings'}, image=images + 'Settings-01-128.png')

main_window.mainloop()