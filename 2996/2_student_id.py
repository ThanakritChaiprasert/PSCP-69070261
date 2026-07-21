'''student id'''
STU_ID: str = input()

if STU_ID.isdigit():
    COUNT = len(str(STU_ID))
    if COUNT == 8 and STU_ID[2:4] == '16':
        print('yes')
    else:
        print('no')
else:
    print('no')
