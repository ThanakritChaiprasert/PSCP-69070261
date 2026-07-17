'''student id'''
id: str = input()
if id.isdigit():
    count = len(str(id))
    if count == 8 and id[2:4] == '16':
        print('yes')
    else:
            print('no')
else:
    print('no')