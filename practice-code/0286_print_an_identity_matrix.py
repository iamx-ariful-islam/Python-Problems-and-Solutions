def print_identity_matrix(n):
    if n <= 0:
        print('Please enter a positive integer for the size of the matrix')
        return
    for i in range(n):
        for j in range(n):
            if i == j:
                print(1, end=' ')
            else: print(0, end=' ')
        print()
        
        
m_size = int(input('Enter the size of the identity matrix: '))
print_identity_matrix(m_size)



'''output:

Enter the size of the identity matrix: 3
1 0 0 
0 1 0 
0 0 1 
'''