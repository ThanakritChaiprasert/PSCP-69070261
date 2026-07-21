'''Bunny Farm'''
xyz = input()
PRICE = float(input())
x = float(xyz[:xyz.index(' ')])
y = float(xyz[xyz.index(' ') + 1:xyz.rindex(' ')])
z = float(xyz[xyz.rindex(' ') + 1:])

LENGTH = 2 * (x + y) * z
TOTAL = LENGTH * PRICE

print(f'{LENGTH:.0f}')
print(f'{TOTAL:.0f}')
