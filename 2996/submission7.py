'''Cyan's password generator'''
name: str = input()
nickname: str = input()
user_age: str = input()

if len(name) >= 5 and len(nickname) >= 5:
    print(name[:2] + nickname[-1] + user_age[-1])
else:
    print(name[0] + user_age + nickname[-1])
