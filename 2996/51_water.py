'''State of Water'''
def state():
    '''State of Water'''
    temperature = float(input())
    temp_unit = input().lower()
    conv_cel = 0

    units = ['c','f']
    if temp_unit in (units[0], units[1]):
        if temp_unit == units[1]:
            conv_cel = (float(temperature) - 32) * 5/9
        elif temp_unit == units[0]:
            conv_cel = temperature

        if 0 < conv_cel < 100:
            print('liquid')
        elif conv_cel <= 0:
            print('solid')
        else:
            print('gas')

state()
