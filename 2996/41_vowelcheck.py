'''Vowel Check'''
LETTER = input()
CHECK = int(LETTER.find('a')) + int(LETTER.find('e')) + int(LETTER.find('i'))
CHECK2 = int(CHECK) + int(LETTER.find('o')) + int(LETTER.find('u'))
if CHECK2 == -4:
    print('yes')
else:
    print('no')
