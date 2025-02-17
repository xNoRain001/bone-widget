from ..libs.blender_utils import get_panel, add_row_with_operator, get_selected_pose_bones
from ..operators.clear_bone_widget import OBJECT_OT_clear_widget
from ..operators.clear_unused_widget import OBJECT_OT_clear_unused_widget
from ..operators.reset_transform import OBJECT_OT_reset_transform

class VIEW3D_PT_bone_widget (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'
  bl_label = "Bone Widget"
  bl_idname = "VIEW3D_PT_bone_widget"

  def draw(self, context):
    layout = self.layout
    row = layout.row()
    scene = context.scene
    # row = layout.row()
    # row.prop(scene, 'scale', text = '缩放(%)')
    # row = layout.row()
    # row.prop(scene, 'translation', text = '移动(%)')
    # row = layout.row()
    # row.prop(scene, 'rotation', text = '旋转')
    # row = layout.row()
    row.prop(scene, 'show_wire', text = '线框')
    row = layout.row()
    row.label(text = '线框宽度')
    row.prop(scene, 'wire_width', text = '')
    row = layout.row()
    row.prop(scene, 'shape', text = '形状')
    row = layout.row()
    row.operator(OBJECT_OT_clear_widget.bl_idname, text = '清除自定义形状')
    row.operator(OBJECT_OT_clear_unused_widget.bl_idname, text = '清空未使用的 WGT')
 