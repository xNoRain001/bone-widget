# pip install blender_utils --target "C:\Users\xNoRain\AppData\Roaming\Blender Foundation\Blender\4.2\scripts\addons\bone-widget\libs"

bl_info = {
  "name": "Bone Widget",
  "blender": (4, 2, 3),
  "version": (0, 0, 0),
  "category": "Rigging",
}

from .libs.blender_utils import register as utils_register, unregister as utils_unregister
from .panels import register as panels_register, unregister as panels_unregister
from .operators import (
  register as operators_register, 
  unregister as operators_unregister
)
from .scene import (
  register as scene_register, 
  unregister as scene_unregister
)

def register():
  utils_register()
  operators_register()
  panels_register()
  scene_register()

def unregister():
  utils_unregister()
  panels_unregister()
  operators_unregister()
  scene_unregister()

if __name__ == "__main__":
  register()
