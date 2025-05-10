rows = 6

for i in range(rows, 0, -1):  
    for j in range(rows - i):  
        print(" ", end="")
    for j in range(i):  
        print("*", end=" ")
    print()



'''output:

* * * * * * 
 * * * * * 
  * * * *
   * * *
    * *
     *
'''