'''Odd Even Count'''
i = 1
EVEN = 0
ODD = 0
NUMBER = 0
while i <= 3 and -1000 <= NUMBER <= 1000:
    NUMBER = int(input())
    if not NUMBER % 2:
        EVEN += 1
    else:
        ODD += 1
    i += 1
print(EVEN)
print(ODD)
