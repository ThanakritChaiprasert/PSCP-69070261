'''Pyramid Castle'''
ROOM = int(input())
MIN = 1
MAX = 1
ODD = -3
EVEN = -2
i = 1
LAYERS = 1

FIND_OE = ROOM % 2

while i <= LAYERS:
    MAX = MIN + ((2 * i) - 2)
    MIN = MAX + 1
    if i % 2 == 1:
        EVEN += 1
        ODD += 3
    else:
        EVEN += 3
        ODD += 1
    if MIN <= ROOM >= MAX:
        LAYERS += 1
    i += 1
if FIND_OE == 1:
    print(ODD)
else:
    print(EVEN)
