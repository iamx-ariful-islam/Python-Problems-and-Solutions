# method #1
for i in range(5):
    space = (8-i)*" "
    num = 11**i
    num = ' '.join([a for a in str(num)])
    print(space, num)


# method #2
from math import factorial
 
n = 5
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
 
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()


# method #3
n = 5
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
        
    C = 1
    for j in range(1, i+1):
        print(' ', C, sep='', end='')
        C = C * (i - j) // j
    print()


# method #4
n = 5
for i in range(n):
    print(' '*(n-i), end='')
    print(' '.join(map(str, str(11**i))))



# output
'''
         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
'''