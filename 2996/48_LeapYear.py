'''Leap Year'''
YEAR = int(input())
if 1 <= YEAR <= 2026:
    if not YEAR % 100 and YEAR % 400 and YEAR > 1582:
        print('no')
    elif not YEAR % 4:
        print('yes')
    else:
        print('no')
