'''AR Tiktok'''
INPUT = input().split(' ')
r = int(INPUT[0])
x = int(INPUT[1])
y = int(INPUT[2])
CALC = (x ** 2) + (y ** 2)
if CALC < r ** 2:
    print('IN')
elif CALC == r ** 2:
    print('ON')
else:
    print('OUT')
