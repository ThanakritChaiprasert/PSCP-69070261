'''Colors'''
color = input()
color_mix = color + input()
color_mixLower = color_mix.lower()
if color_mixLower == 'redyellow' or color_mixLower == 'yellowred':
    print('Orange')
elif color_mixLower == 'redblue' or color_mixLower == 'bluered':
    print('Purple')
elif color_mixLower == 'yellowblue' or color_mixLower == 'blueyellow':
    print('Green')
else:
    print('Error')
