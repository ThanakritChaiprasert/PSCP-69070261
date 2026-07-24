'''Gift Wrapping'''
PI = 3.14
area = input().split(' ')
r = float(area[0])
h = float(area[1])
glue = float(area[2])

WIDTH = h + (r * 2)
LENGTH = (2 * PI * r) + glue
print(f'{WIDTH:.2f} {LENGTH:.2f}')
