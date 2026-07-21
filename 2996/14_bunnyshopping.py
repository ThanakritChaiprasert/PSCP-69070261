'''Bunny Shopping'''
xyz: float = input()
CARROT = float(xyz[:xyz.index(' ')])
CABBAGE = float(xyz[xyz.index(' ') + 1:xyz.rindex(' ')])
TOMATO = float(xyz[xyz.rindex(' ') + 1:])

CARROT_PRICE = CARROT * 10
CABBAGE_PRICE = CABBAGE * 25
TOMATO_PRICE = TOMATO * 3
TOTAL = CARROT_PRICE + CABBAGE_PRICE + TOMATO_PRICE

print(f'{TOTAL:.0f}')
