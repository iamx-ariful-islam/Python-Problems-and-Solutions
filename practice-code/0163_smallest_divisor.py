# find the smallest divisor of an integer

def smallest_divisor(num):
    num = abs(num)
    if num <= 1:
        return 'Input must be greater than 1'
    for i in range(2, num + 1):
        if num % i == 0:
            return i
        
number = int(input('Enter an integer: '))
result = smallest_divisor(number)
print(f'The smallest divisor of {number} is {result}')


'''output:

Enter an integer: 15
The smallest divisor of 15 is 3
'''