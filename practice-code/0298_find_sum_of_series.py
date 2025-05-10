def sum_of_series(n):
    if n <= 0:
        return 'N should be a positive integer'
    
    total_sum = 0
    for i in range(1, n+1):
        total_sum += 1/i
        
    return total_sum


nums = int(input('Enter a positive integer number: '))
result = sum_of_series(nums)
print(f'The sum of the series for n={nums} is: {result:.2f}')



'''output:

Enter a positive integer number: 6
The sum of the series for n=6 is: 2.45
'''