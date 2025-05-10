# print 1(one)
n = 7
for i in range(1, n+1):
    for j in range(1, n-1):
        if j==4-i or j==3 or i==7:
            print('+', end='')
        else: print(' ', end='')
    print()
    

# print 2(two)
n = 7
for i in range(1, n+1):
    for j in range(1, n-1):
        if i==1 or i==4 or i==7 or (j==5 and i<=4) or (j==1 and i>=4):
            print('+', end='')
        else: print(' ', end='')
    print()
    

# print 3(three)
n = 7
for i in range(1, n+1):
    for j in range(1, n-1):
        if i==1 or i==4 or i==7 or j==5:
            print('+', end='')
        else: print(' ', end='')
    print()
    

'''output:
  +  
 ++
+ +
  +
  +
  +
+++++

+++++
    +
    +
+++++
+
+
+++++

+++++
    +
    +
+++++
    +
    +
+++++
'''