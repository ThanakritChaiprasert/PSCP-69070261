'''3D cordinates'''
xyz1: float = input()
xyz2: float = input()
x1 = float(xyz1[:xyz1.index(' ')])
y1 = float(xyz1[xyz1.index(' ') + 1:xyz1.rindex(' ')])
z1 = float(xyz1[xyz1.rindex(' ') + 1:])
x2 = float(xyz2[:xyz2.index(' ')])
y2 = float(xyz2[xyz2.index(' ') + 1:xyz2.rindex(' ')])
z2 = float(xyz2[xyz2.rindex(' ') + 1:])
DISTANCE = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
print(f'{DISTANCE:.2f}')
