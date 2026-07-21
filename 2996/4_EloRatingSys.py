'''Elo rating system'''
RA: int = input()
RB: int = input()

PLAYER: str = input()
if PLAYER == 'A':
    EA: float = 1 / (1 + (10 ** ((int(RB) - int(RA))/400)))
    print(f'{EA:.2f}')
elif PLAYER == 'B':
    EB: float = 1 / (1 + (10 ** ((int(RA) - int(RB))/400)))
    print(f'{EB:.2f}')
