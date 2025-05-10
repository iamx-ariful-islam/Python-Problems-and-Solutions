# find sum of digit of a number using recursion

def sum_of_digits(num):
    if num == 0: return 0
    return (num % 10) + sum_of_digits(num // 10)

number = int(input('Enter a number: '))
result = sum_of_digits(abs(number))

print(f'The sum of the digits of {number} is {result}')


'''output:

Enter a number: 65
The sum of the digits of 65 is 11
'''