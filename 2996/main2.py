'''student id'''
STU_ID: str = input()

if id.isdigit():
    COUNT = len(str(STU_ID))
    if COUNT == 8 and id[2:4] == '16':
        print('yes')
    else:
        print('no')
else:
    print('no')
