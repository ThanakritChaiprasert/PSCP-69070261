'''Taxi Cost'''
def total_cost():
    '''Taxi Cost'''
    COST = 0
    km = int(input())
    if 0 < km <= 1:
        COST = 35
    elif 1 < km <= 10:
        COST = ((km - 1) * 5) + 35
    elif 10 < km:
        COST = ((km - 10) * 8) + 80
    print(COST)

total_cost()
