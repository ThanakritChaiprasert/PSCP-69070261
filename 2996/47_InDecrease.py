'''Increase/Descrease'''
IN1 = float(input())
IN2 = float(input())
IN3 = float(input())
if IN1 < IN2 < IN3:
    print('increasing')
elif IN1 > IN2 > IN3:
    print('decreasing')
else:
    print('neither')
