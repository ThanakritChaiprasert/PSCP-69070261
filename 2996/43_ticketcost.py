'''Ticket Cost'''
AGE = int(input())
STATUS = str(input())
if len(STATUS) == 1 and AGE >= 0:
    if AGE < 18 or (not STATUS.find('s') or not STATUS.find('S')):
        print('20')
    else:
        print('50')
