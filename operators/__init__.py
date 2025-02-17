from ..libs.blender_utils import register_classes, unregister_classes
from .reload_addon import OBJECT_OT_reload_addon
from .clear_bone_widget import OBJECT_OT_clear_widget
from .clear_unused_widget import OBJECT_OT_clear_unused_widget
from .reset_transform import OBJECT_OT_reset_transform

classes = (
  OBJECT_OT_reload_addon,
  OBJECT_OT_clear_widget,
  OBJECT_OT_clear_unused_widget,
  OBJECT_OT_reset_transform
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
