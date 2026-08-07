'''Vowel Count'''
def vowelcount():
    '''Vowel Count'''
    i = int(input())
    WORD = ''
    COUNT = 0
    vowels = ['A','E','I','O','U']

    for i in range(i):
        LETTER = str(input())
        WORD += str(LETTER)
    for j in range(5):
        COUNT += WORD.count(vowels[j])

    if WORD == WORD.upper():
        print(COUNT)

vowelcount()
