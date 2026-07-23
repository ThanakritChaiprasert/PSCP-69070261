'''Divide by 10'''
NUM = int(input())
DIVIDABLE = (NUM // 10) * 10
ANS = DIVIDABLE
while int(DIVIDABLE) > 0:
    DIVIDABLE = int(DIVIDABLE) - 10
    ANS = str(ANS) + ' ' + str(DIVIDABLE)
print(ANS)
