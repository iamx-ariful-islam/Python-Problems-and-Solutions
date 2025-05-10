# pass by known and unknown or default values
def Func(a, b, c, d=0, e=0, f=0):
    print(a, b, c, d, e, f)

# list of value
L = [1, 2, 3]

# pass the value
Func(9, *L, 8)


'''output:

9 1 2 3 8 0
'''