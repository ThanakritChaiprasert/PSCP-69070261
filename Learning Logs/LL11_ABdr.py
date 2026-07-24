'''[A,B] % d = r'''
A = int(input())
B = int(input())
d = int(input())
r = int(input())
COUNT = 0
while A <= B:
    if A % d == r and A < B and r < d: 
        '''Change this part'''
        A += d
        COUNT += 1
    elif A % d != r and A < B and r < d:
        A += 1
print(COUNT)
