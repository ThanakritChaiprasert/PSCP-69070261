'''Swap Number'''
number = input()
symbol = input()
REV_INPUT = number[::-1].lstrip('0')
if 10 <= int(number) <= 99:
    if symbol == '+':
        print(number, symbol, REV_INPUT, '=', (int(number) + int(REV_INPUT)))
    elif symbol == '*':
        print(number, symbol, REV_INPUT, '=', (int(number) * int(REV_INPUT)))
