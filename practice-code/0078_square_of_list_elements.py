def square(n):
    return n**2


List = [1, 2, 3, 4, 5]
squares = list(map(square, List))
print('Input List  :', List)
print('Output List :', squares)


'''output:

Input List  : [1, 2, 3, 4, 5]
Output List : [1, 4, 9, 16, 25]
'''