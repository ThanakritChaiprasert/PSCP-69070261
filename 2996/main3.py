'''student id'''
ID: str = input()

if ID.isdigit():
    COUNT = len(str(ID))
    if COUNT == 13:
        print('yes')
    else:
        print('no')
else:
    print('no')
