import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\interface modules')
images = os.path.abspath(os.pardir) + '\images\\'

from widgets import *
from interface import *

add_payment = Window(child=True, title='Add Payment')

add_payment.add_row()
add_payment.add_row()
add_payment.add_column(0)
add_payment.add_column(0)
add_payment.add_column(0)
add_payment.add_column(1)
add_payment.add_column(1)

add_payment.add_widget_to(DefaultLabel, 0, attributes={'text': 'date'})
add_payment.add_widget_to(DefaultEntry, 0, tag='date') #calendar widget?
add_payment.add_widget_to(DefaultLabel, 0, attributes={'text': 'payment amount*'})
init_focus = add_payment.add_widget_to(DefaultEntry, 0, tag='value')
add_payment.add_widget_to(DefaultButton, 0, row_num=1, exec_func=add_payment.hide, bg='#2B58A6', fg='white', attributes={'text': 'Add Guardian'}, width=26)
add_payment.add_widget_to(DefaultButton, 1, row_num=1, exec_func=lambda: add_payment.hide(True), bg='#2B58A6', fg='white', attributes={'text': 'Cancel'}, width=26)

init_focus.focus()