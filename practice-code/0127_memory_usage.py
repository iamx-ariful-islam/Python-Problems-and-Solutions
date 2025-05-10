import sys


var1 = 'python'
var2 = 100
var3 = True

print(f'{var1} \t= {sys.getsizeof(var1)}')
print(f'{var2} \t= {sys.getsizeof(var2)}')
print(f'{var3} \t= {sys.getsizeof(var3)}')


'''output:

python  = 47
100     = 28
True    = 28
'''