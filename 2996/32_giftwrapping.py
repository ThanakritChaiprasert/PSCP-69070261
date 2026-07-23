'''Gift Wrapping'''
PI = 3.14
area = input()
r = float(area[:area.index(' ')])
h = float(area[area.index(' ') + 1:area.rindex(' ')])
glue = float(area[area.rindex(' ') + 1:])

WIDTH = h + (r * 2)
LENGTH = (2 * PI * r) + glue
print(f'{WIDTH:.2f} {LENGTH:.2f}')
