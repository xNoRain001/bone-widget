from .add_rotation import add_rotation
from .add_scale import add_scale
from .add_shape import add_shape
from .add_show_wire import add_show_wire
from .add_translation import add_translation
from .add_wire_width import add_wire_width

classes = ()

def register():
  # register_classes(classes)
  add_rotation()
  add_scale()
  add_shape()
  add_show_wire()
  add_translation()
  add_wire_width()
  
def unregister():
  # unregister_classes(classes)
  pass
