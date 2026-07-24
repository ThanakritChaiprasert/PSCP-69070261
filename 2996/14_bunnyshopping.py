'''Bunny Shopping'''
xyz: float = input().split(' ')
CARROT = float(xyz[0])
CABBAGE = float(xyz[1])
TOMATO = float(xyz[2])

CARROT_PRICE = CARROT * 10
CABBAGE_PRICE = CABBAGE * 25
TOMATO_PRICE = TOMATO * 3
TOTAL = CARROT_PRICE + CABBAGE_PRICE + TOMATO_PRICE

print(f'{TOTAL:.0f}')
