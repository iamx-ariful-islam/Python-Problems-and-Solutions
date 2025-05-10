fruits = ['apple', 'banana', 'cherry']

for i, fruit in enumerate(fruits, start=1): # or use enumerate(fruits, 1)
    print(f'index:{i}, {fruit}')
    

'''output:

index:1, apple
index:2, banana
index:3, cherry
'''