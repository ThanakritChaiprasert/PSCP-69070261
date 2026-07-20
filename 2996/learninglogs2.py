'''Colors'''
color = input()
color_mix = color + input()
if color_mix in ['RedYellow','YellowRed']:
    print('Orange')
elif color_mix in ['RedBlue','BlueRed']:
    print('Violet')
elif color_mix in ['YellowBlue','BlueYellow']:
    print('Green')
elif color_mix in ['RedRed','YellowYellow','BlueBlue']:
    print(color)
else:
    print('Error')
