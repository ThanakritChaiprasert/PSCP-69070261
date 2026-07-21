'''Quadrant'''
x = input()
y = input()
if float(x) > 0 and float(y) > 0:
    print('Q1')
if float(x) < 0 < float(y):
    print('Q2')
if float(x) < 0 and float(y) < 0:
    print('Q3')
if float(x) > 0 > float(y):
    print('Q4')

if float(x) == 0 == float(y):
    print('O')
elif not float(x):
    print('Y')
elif not float(y):
    print('X')
