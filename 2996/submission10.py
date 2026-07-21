'''Safe Password'''
input_char = input()
input_number = input()
char_pass =  'H'
number_pass = '4567'
if input_char == char_pass and input_number == number_pass:
    print('safe unlocked')
elif input_char != char_pass and input_number == number_pass:
    print('safe locked - change char')
elif input_char == char_pass and input_number != number_pass:
    print('safe locked - change number')
else:
    print('safe locked')
