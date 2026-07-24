'''AEIOU'''
WORD = input()
LETTER_A = int(WORD.count('a')) + int(WORD.count('A'))
LETTER_E = int(WORD.count('e')) + int(WORD.count('E'))
LETTER_I = int(WORD.count('i')) + int(WORD.count('I'))
LETTER_O = int(WORD.count('o')) + int(WORD.count('O'))
LETTER_U = int(WORD.count('u')) + int(WORD.count('U'))
if LETTER_A:
    print('a :', LETTER_A)
if LETTER_E:
    print('e :', LETTER_E)
if LETTER_I:
    print('i :', LETTER_I)
if LETTER_O:
    print('o :', LETTER_O)
if LETTER_U:
    print('u :', LETTER_U)
