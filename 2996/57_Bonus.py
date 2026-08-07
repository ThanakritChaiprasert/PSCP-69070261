'''Bonus'''
def recieved_bonus():
    '''Bonus'''
    INPUT = input().split(' ')
    ROLE = INPUT[0].upper()
    AGE = INPUT[1]
    SALARY = INPUT[2]
    RECIEVE = 0
    BONUS = 0
    BONUS2 = 0
    bonuses = [1500, 1000, 500]
    bonuses1 = [.06, .08, .1]
    bonuses2 = [.05, .06, .07]
    bonuses3 = [.04, .05, .06]
    if ROLE == 'M':
        BONUS = bonuses1
        BONUS2 = bonuses[0]
    elif ROLE == 'B':
        BONUS = bonuses2
        BONUS2 = bonuses[1]
    elif ROLE == 'G':
        BONUS = bonuses3
        BONUS2 = bonuses[2]

    if ROLE not in ('M', 'B', 'G'):
        RECIEVE = 0
    else:
        if 0 < int(AGE) < 5:
            RECIEVE = (float(SALARY) * float(BONUS[0])) + float(BONUS2)
        elif 5 <= int(AGE) <= 10:
            RECIEVE = (float(SALARY) * float(BONUS[1])) + float(BONUS2)
        elif 10 < int(AGE):
            RECIEVE = (float(SALARY) * float(BONUS[2])) + float(BONUS2)

    print(int(RECIEVE))

recieved_bonus()
