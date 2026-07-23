'''Money Exchange'''
DOLLADOLLA = int(input())

TEN_a = DOLLADOLLA // 10
TEN_b = DOLLADOLLA % 10
FIVE_a = TEN_b // 5
FIVE_b = TEN_b % 5
TWO_a = FIVE_b // 2
ONE_COIN = FIVE_b % 2

print('10 =' , TEN_a)
print('5 =', FIVE_a)
print('2 =', TWO_a)
print('1 =', ONE_COIN)
