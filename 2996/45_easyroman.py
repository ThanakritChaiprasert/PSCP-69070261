'''Easy Roman Numbers'''
num_input = int(input())
ROMAN_NUM = 'I II III IV V VI VII VIII IX'
ROMAN_NUM2 = ROMAN_NUM.split(' ')
if num_input < 0:
    print('Error : Please input positive number')
elif num_input > 9 or not num_input:
    print('Error : Out of range')
else:
    print(ROMAN_NUM2[int(num_input)-1])
