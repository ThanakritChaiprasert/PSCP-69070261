'''All the same'''
IN1 = int(input())
IN2 = int(input())
IN3 = int(input())
if all(0 <= N <= 1000 for N in (IN1,IN2,IN3)):
    if IN1 == IN2 == IN3:
        print('all the same')
    elif IN1 != IN2 != IN3 and IN1 != IN3:
        print('all different')
    else:
        print('neither')
