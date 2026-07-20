'''Colors'''
color = input()
color_mix = color + input()
if color_mix == 'RedYellow' or color_mix == 'YellowRed':
    print('Orange')
elif color_mix == 'RedBlue' or color_mix == 'BlueRed':
    print('Purple')
elif color_mix == 'YellowBlue' or color_mix == 'BlueYellow':
    print('Green')
else:
    print('Error')
