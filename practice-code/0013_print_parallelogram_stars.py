# enter row number
rows = int(input('Enter row number : '))

for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(' ', end='')
    for k in range(1, rows+1):
        print('*', end='')
    print()

for i in range(rows-1, 0, -1):
    for j in range(1, rows-i+1):
        print(' ', end='')
    for k in range(1, rows+1):
        print('*', end='')
    print()
    
    
'''output:

Enter row number : 5
    *****
   *****
  *****
 *****
*****
 *****
  *****
   *****
    *****
'''