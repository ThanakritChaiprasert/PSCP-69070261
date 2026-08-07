'''Ticket'''
def cost():
    '''Ticket'''
    INPUT = input().split(' ')
    AGE = int(INPUT[0])
    DATE = INPUT[1].lower()
    if 0 <= AGE <= 120:
        if AGE < 5:
            COST = 0
        elif 5 <= AGE <= 18:
            COST = 100
        else:
            COST = 150

        if DATE == 'wed':
            COST = COST // 2
        print(int(COST))

cost()
