def scale_1 (x, y, z):
  return (x, y, z)

def scale_2 (x, y, z):
  return (x, x, x)

def scale_3 (x, y, z):
  return (x, x / 2, x)

scale_strategies = {
  'Cube': scale_1,
  'Circle': scale_2,
  'Chest': scale_2,
  'FK Limb 1': scale_2,
  'FK Limb 2': scale_3,
  'Gear Complex': scale_2,
  'Gear Simple': scale_2,
  'Line': scale_2,
  'Paddle': scale_2,
  'Roll': scale_2,
  'Root': scale_2,
  'Sphere': scale_2
}
