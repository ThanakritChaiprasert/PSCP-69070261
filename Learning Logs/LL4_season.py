'''Season'''
MONTH = int(input())
DAY = int(input())
MONTH_DIV = MONTH / 3

if (MONTH_DIV == 1 and DAY >= 21) or (2 > MONTH_DIV > 1) or (MONTH_DIV == 2 and DAY < 21):
    print('spring')
elif (MONTH_DIV == 2 and DAY >= 21) or (3 > MONTH_DIV > 2) or (MONTH_DIV == 3 and DAY < 21):
    print('summer')
elif (MONTH_DIV == 3 and DAY >= 21) or (4 > MONTH_DIV > 3) or (MONTH_DIV == 4 and DAY < 21):
    print('fall')
else:
    print('winter')
