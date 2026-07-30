'''BDay'''
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())
PERSON1 = (y1 * 12 * 30) + (m1 * 30) + d1
PERSON2 = (y2 * 12 * 30) + (m2 * 30) + d2
if -7 < (int(PERSON1) - int(PERSON2)) < 7:
    print('0')
elif int(PERSON1) >= int(PERSON2):
    print('2')
elif int(PERSON1) <= int(PERSON2):
    print('1')
