'''Lowest Value'''
import math
i = 1
RESULT = math.inf

while i <= 3:
    num_input = int(input())
    if num_input < RESULT:
        RESULT = num_input
    i += 1
print(RESULT)
