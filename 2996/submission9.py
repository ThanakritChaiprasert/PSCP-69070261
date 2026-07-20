'''Pro'''
x = int(input())
y = int(input())
a = int(input())
z = int(input())

if x >= y >= 1 and a >= 0 and z >= 0:
    GROUPS = z // x
    REMAINDER = z % x
    TOTAL_PAY = (GROUPS * y * a) + (REMAINDER * a)
    print(TOTAL_PAY)
