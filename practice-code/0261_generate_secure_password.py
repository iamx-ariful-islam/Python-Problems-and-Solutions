# method #1

import re
from random import choice
from string import ascii_letters, digits


inp = int(input('Enter password length more then 4: '))
c   = ascii_letters + digits + '#$%&*+@*?:'

passwds = [''.join(choice(c, k=inp)) for i in range(50)]
rgx     = ['\W', '[a-z]', '[A-Z]', '\d']

for i in passwds:
    x = len([*filter(lambda x: re.search(x, i), rgx)])
    if x == 4:
        print('Your secure password:', i)
        break


# method #2

import re

st = 'g0&ER0iR04'

if len(st) >= 7 and len(re.findall(r'\W{2,}', st)) and len(re.findall(r'\d{2,}', st)):
    print('Valid secure password')
else:
    print('Not valid')