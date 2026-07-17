'''id card'''
ID_CARD: str = input()

if ID_CARD.isdigit():
    COUNT = len(str(ID))
    if COUNT == 13:
        print('yes')
    else:
        print('no')
else:
    print('no')
