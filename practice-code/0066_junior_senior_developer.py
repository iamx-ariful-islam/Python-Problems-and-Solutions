# junior developer

n = 5
for i in range(1, n+1):
    # printing spaces
    for j in range(i-1):
        print(' ', end='')
    # printing starts
    for j in range(2*(n-i)+1):
        print('*', end='')
    print()
    


# senior developer

n = 5
for i in range(1, n+1):
    print(' ' * (i-1), end='')
    print('*' * (2*(n-i)+1))
    
    
'''output:

*********
 *******
  *****
   ***
    *
*********
 *******
  *****
   ***
    *
'''