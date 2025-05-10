# pip install roman

import roman

# number to roman
n = 100
print(f'Decimal to Roman [{n}] \t= {roman.toRoman(n)}')

# roman to number
r = 'M'
print(f'Roman to Decimal [{r}] \t= {roman.fromRoman(r)}')


'''output:

Decimal to Roman [100]  = C
Roman to Decimal [M]    = 1000
'''