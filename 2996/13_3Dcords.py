'''3D cordinates'''
xyz1: float = input().split(' ')
xyz2: float = input().split(' ')
x1 = float(xyz1[0])
y1 = float(xyz1[1])
z1 = float(xyz1[2])
x2 = float(xyz2[0])
y2 = float(xyz2[1])
z2 = float(xyz2[2])
DISTANCE = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
print(f'{DISTANCE:.2f}')
