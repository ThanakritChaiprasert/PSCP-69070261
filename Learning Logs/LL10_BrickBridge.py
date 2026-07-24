'''BrickBridge'''
small_b = int(input())
BIG_B = int(input())
GOAL = int(input())

COUNT = GOAL // 5
if small_b >= 0 and BIG_B >= 0:
    if COUNT < BIG_B:
        REQUIRED = COUNT
    else:
        REQUIRED = COUNT - abs(COUNT - BIG_B)
    small_b_needed = GOAL - (REQUIRED * 5)
    if GOAL < (BIG_B * 5):
        REQUIRED = 0
    if int(small_b_needed) > int(small_b) or (not small_b and not REQUIRED):
        small_b_needed = -1
    print(small_b_needed)
