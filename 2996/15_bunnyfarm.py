'''Bunny Farm'''
xyz = input().split(' ')
PRICE = float(input())
x = float(xyz[0])
y = float(xyz[1])
z = float(xyz[2])

LENGTH = 2 * (x + y) * z
TOTAL = LENGTH * PRICE

print(f'{LENGTH:.0f}')
print(f'{TOTAL:.0f}')
