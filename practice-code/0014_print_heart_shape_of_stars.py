# set the row number
rows = 7

for i in range(rows):
    for j in range(rows):
        if i==0 and j%3!=0 or i==1 and j%3==0 or i-j==2 or i+j==8:
            print('*', end='')
        else: print(' ', end='')
    print()
    

'''output:

 ** ** 
*  *  *
*     *
 *   *
  * *
   *
  * *
'''