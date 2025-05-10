# find all the divisors of an integer

def check_divisor(num):
    num = abs(num)
    divisors = []
    if num <= 1:
        return 'Input must be greater than 1'
    for i in range(2, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
        
number   = int(input('Enter an integer: '))
divisors = check_divisor(number)
print(f'The divisors of {number} are {divisors}')


'''output:

Enter an integer: 15
The divisors of 15 are [3, 5, 15]
'''