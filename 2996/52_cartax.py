'''CarTax'''
def taxresult():
    '''CarTax'''
    YEAR = int(input())
    CC = int(input())

    tax1 = [1250, 1400, 2000]
    tax2 = [1100, 1300, 1700]
    tax3 = [1000, 1200, 1500]

    if YEAR <= 1990:
        YEAR = tax1
    elif 1991 <= YEAR <= 1999:
        YEAR = tax2
    else:
        YEAR = tax3

    if CC <= 1500:
        results = YEAR[0]
    elif 1500 < CC <= 2000:
        results = YEAR[1]
    else:
        results = YEAR[2]

    print(results)

taxresult()
