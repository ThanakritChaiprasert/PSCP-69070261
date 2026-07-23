'''Lowest Value (4n't)'''
import math
INPUTS = int(input())
i = 1
RESULT = math.inf

while i <= INPUTS:
    num_input = int(input())
    if num_input < RESULT:
        RESULT = num_input
    i += 1
print(RESULT)
