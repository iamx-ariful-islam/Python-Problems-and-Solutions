# pip install numtext

import numtext as nt

num1 = 10201
num2 = '222'
result1 = nt.convert(num1)
result2 = nt.convert(num2)
print(result1)
print(result2)

'''output:

ten thousand two hundred and one
two hundred and twenty two
'''