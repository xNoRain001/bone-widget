from ..libs.blender_utils import register_classes, unregister_classes, add_scene_custom_prop
from .reload_addon import VIEW3D_PT_reload_addon
from .bone_widget import VIEW3D_PT_bone_widget

classes = (
  VIEW3D_PT_reload_addon,
  VIEW3D_PT_bone_widget
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
