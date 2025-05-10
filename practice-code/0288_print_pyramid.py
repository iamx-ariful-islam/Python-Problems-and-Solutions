b = 0
rows = 5

for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i+1):
        print(b, end=' ')
    print('\r')
    


'''output:

1 1 1 1 1 
2 2 2 2
3 3 3
4 4
5
'''