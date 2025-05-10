from re import sub, findall


# method #1
inp = '4154455441155555'
x = sub(r'^\d{12}', '*'*12, inp)
print(x)


# method #2
inp = '4154455441155555'
dig = findall(r'.{4}', inp)
b1, b2 = dig[:3], dig[3:]
b1r = [i.replace(i, '*') for i in ''.join(b1)]
x = ''.join(b1r)+''.join(b2)
print(x)


'''output:

************5555
************5555
'''