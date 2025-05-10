import os
import random as rand


# input user choice for testing purpose
usr_pwd = input('Enter your password: ')
# set default some password characters
set_pwd = ['a', 'b', 'c', 'd', 'e']

pwd = ''
while pwd != usr_pwd:
    pwd = ''
    for _ in range(len(usr_pwd)):
        gues_pwd = set_pwd[rand.randint(0, len(set_pwd)-1)]
        pwd = gues_pwd + pwd
        print(pwd)
        print('Cracking password...please wait')
        # clean the screen
        os.system('cls')
        
print('Your password is :', pwd)