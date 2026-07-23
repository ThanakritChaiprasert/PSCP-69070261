'''Pods'''
INPUT = input()
PASSENGERS = int(INPUT[:INPUT.index(' ')])
LINE = int(INPUT[:INPUT.index(' '):-1])
i = 1
STORAGE = ''
REMAIN = 0

while i <= PASSENGERS and 1 <= PASSENGERS <= 100000 and 1 <= LINE <= 300:
    POD = int(input())
    REMAIN += 1
    if 1 <= POD <= LINE and STORAGE.find(str(POD)) == -1:
        STORAGE = str(STORAGE) + str(POD)
        if len(STORAGE) == int(LINE):
            STORAGE = ''
            REMAIN -= int(LINE)
    i += 1
print(REMAIN)
