'''[A,B] % d = r'''
A = int(input())
B = int(input())
d = int(input())
r = int(input())
COUNT = 0
while A <= B and r < d and A % d != r:
    A += 1
if d == r:
    COUNT = 0
else:
    COUNT = ((B - A) // d) + 1
print(COUNT)
