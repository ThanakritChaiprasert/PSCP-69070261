'''Calculator'''
key_press = input()
D_COUNT = 2

if int(key_press) <= 1:
    print(key_press)
if int(key_press) > 1:
    total = (int(key_press) * 2)
    while D_COUNT <= len(key_press):
        total = int(key_press) - ((10 ** (int(D_COUNT) - 1)) - 1) + int(total)
        D_COUNT += 1
    print(total)
