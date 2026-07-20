'''Colors'''
color = input()
color2 = input()
color_mix = color + color2
if color_mix in ['RedYellow']:
    print('Orange')
elif color_mix in ['RedBlue']:
    print('Purple')
elif color_mix in ['YellowBlue']:
    print('Green')
else:
    print('Error')
