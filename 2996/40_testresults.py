'''Test Results'''
EXER = int(input())
MID = int(input())
FINAL = int(input())
PASSES = 0
if EXER <= 10 and MID <= 40 and FINAL <= 50:
    if EXER >= 5:
        PASSES += 1
    if MID >= 20:
        PASSES += 1
    if FINAL >= 25:
        PASSES += 1
    if PASSES != 3:
        print('fail')
    else:
        print('pass')
