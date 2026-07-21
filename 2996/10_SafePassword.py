'''Safe Password'''
input_char = input()
input_number = input()
CHAR_PASS =  'H'
NUMBER_PASS = '4567'
if input_char == CHAR_PASS and input_number == NUMBER_PASS:
    print('safe unlocked')
elif input_char != CHAR_PASS and input_number == NUMBER_PASS:
    print('safe locked - change char')
elif input_char == CHAR_PASS and input_number != NUMBER_PASS:
    print('safe locked - change digit')
else:
    print('safe locked')
