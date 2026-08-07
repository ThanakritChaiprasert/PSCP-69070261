'''Basic ATM'''
def banknotes():
    '''Basic ATM'''
    WITHDRAW = int(input())
    thousand_bht = WITHDRAW // 1000
    remain1 = WITHDRAW % 1000
    fhundred_bht = remain1 // 500
    remain2 = remain1 % 500
    hundred_bht = remain2 // 100
    if WITHDRAW % 100:
        print('ERROR')
    else:
        if thousand_bht:
            print('1000 =', thousand_bht)
        if fhundred_bht:
            print('500 =', fhundred_bht)
        if hundred_bht:
            print('100 =', hundred_bht)

banknotes()
