'''Colors'''
color = input()
color_mix = color + input()
if color_mix in ['RedYellow', 'YellowRed']:
    print('Orange')
elif color_mix in ['RedBlue', 'BlueRed']:
    print('Violet')
elif color_mix in ['YellowBlue', 'BlueYellow']:
    print('Green')
else:
    print('Error')
