'''Colors'''
color = input()
color_mix = color + input()
color_mixLower = color_mix.lower()
if color_mix  == '':
    if color_mixLower in ['redyellow', 'yellowred']:
        print('Orange')
    elif color_mixLower in ['redblue', 'bluered']:
        print('Violet')
    elif color_mixLower in ['yellowblue', 'blueyellow']:
        print('Green')
    else:
        print('Error')
print(color)