"""
.. module:: translator_views
   :synopsis: View objecta for translatorui

.. moduleauthor:: Andrej Petelin <andrej.petelin@gmail.com>

This module hold view objects for translatorui module
"""

from labtools.standa.conf import *
from traitsui.api import View, Item, Group, HGroup, spring
from labtools.utils.custom_editors import LEDEditor ,DisplayEditor 

position_view = View(

    HGroup(
    spring,
Item('much_less', style = 'custom', show_label = False),
Item('less', style = 'custom', show_label = False),
Group(Item('value', show_label = False)),
Item('more', style = 'custom', show_label = False),
Item('much_more', style = 'custom', show_label = False),
spring,
    ),resizable = True)
    
def _item(name):
    if POWERUSER:
        return Item(name, label = name)
    else:
        return Item(name, style = 'readonly', label = name)

motor_settings_view = \
View(
    'speed',
    'reversed',
    Group(*[Item(name,label = name) for name in PARAMETERS],label = 'Parameters'),
    Group(*[Item(name,label = name) for name in START_PARAMETERS], label = 'Start Parameters'),
    Group(*[_item(name) for name in MODE], label = 'Mode'),
     buttons = ['OK']    
 )
    

translator_view_groups = [ 
Group(
  HGroup(
    Item('init_button', show_label = False),   
    Item('settings_button', show_label = False, enabled_when = '_motor_status > 0'),
    Item('save_button', show_label = False, enabled_when = '_motor_status > 0'),
    spring,
    Item('_motor_status', show_label= False, editor = LEDEditor()),
  ), 
  HGroup(
    Item('device', label = 'ID', enabled_when = '_initialized == False'),
    spring,
    Item('_serial', style = 'readonly', label = 'Serial No'), 
  ),label = 'Device', show_border = True
), 
Group(
   
   Item('_target_position',show_label = False, style = 'custom'),

    HGroup(
        Item('move_button', show_label = False,enabled_when = '_initialized'),
        Item('home_button', show_label = False,enabled_when = '_initialized'),
        spring,
        Item('stop_button', show_label = False,enabled_when = '_initialized'),
    ),label = 'Target position [mm]', show_border = True
),
Group(
    Item('_position_str', show_label = False, editor = DisplayEditor(alarm_name = '_alarm'), height = 50), 
    Item('zero_button', show_label = False, enabled_when = '_motor_status > 1'),
    label = 'Current position [mm]', show_border = True
),
HGroup(
  Item('_status_message', style = 'readonly', show_label = False),
  show_border = True, label = 'Status'
)
]  


standa_translator_view = View(Group(*translator_view_groups), title = 'Standa 8MT184-13 controller')
 
    
    
