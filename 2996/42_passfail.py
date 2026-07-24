'''Pass/Fail'''
MID = int(input())
FINAL = int(input())
TOTAL = MID + FINAL
if TOTAL >= 50:
    print(TOTAL)
    print('pass')
else:
    print(TOTAL)
    print('fail')
