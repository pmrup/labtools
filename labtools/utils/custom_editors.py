"""
.. module:: custom_editors
   :synopsis: Custom TraitsUI editors

.. moduleauthor:: Andrej Petelin <andrej.petelin@gmail.com>

Some custom editors are defined here. These are:
    
    * :class:`.LEDEditor`: for displaying state values as a LED light (green, 
      yelow, red states)
    * :class:`.DisplayEditor`: for displaying numerical values in a coloured 
      LED display (can change color if alarm is triggered)
"""


from traitsui.editor_factory \
    import EditorFactory

from traitsui.api import BooleanEditor

LEDEditor = BooleanEditor
    
from traits.api import Color, Bool, Str

            
class DisplayEditor(EditorFactory):
    """A custom LED editor for float, int, str values. It changes color
    when alarm trait is activated. Colors can be defined.
    
    Examples
    --------
    
    >>> from traitsui.api import *
    >>> from traits.api import *
    >>> editor = DisplayEditor( alarm_name = 'alarm', color = 'green', alarm_color = 'red')
    >>> class Test(HasTraits):
    ...     alarm = Bool(False)
    ...     value = Float(101.)
    ...     view = View('alarm',Item('value', editor = editor, width = 300, height = 50))
             
    >>> t = Test()
    >>> ok = t.configure_traits() # %(skip)s
"""
   # klass = _DisplayEditor
    
    #: trait name for alarm bool, which triggers an alarm color for display
    alarm_name = Str()
    #: normal color of the display
    color = Color('green')
    #: alarm color of the display
    alarm_color = Color('red')

from ..conf import SKIPGUI
if SKIPGUI:
    DisplayEditor.__doc__ = DisplayEditor.__doc__  % {'skip' : 'doctest: +SKIP'}
    LEDEditor.__doc__ = LEDEditor.__doc__  % {'skip' : 'doctest: +SKIP'}
