'''AR Tiktok'''
INPUT = input()
r = int(INPUT[:INPUT.index(' ')])
x = int(INPUT[INPUT.index(' ') + 1:INPUT.rindex(' ')])
y = int(INPUT[INPUT.rindex(' ') + 1:])
CALC = (x ** 2) + (y ** 2)
if CALC < r ** 2:
    print('IN')
elif CALC == r ** 2:
    print('ON')
else:
    print('OUT')
