# find numbers which are divisible by num1 and multiple of num2

def find_numbers(start, end):
    print(f'Numbers divisible by num1 and multiple of num2 between {start} and {end}:')
    for num in range(start, end + 1):
        if num % 7 == 0 and num % 5 == 0:
            print(num, end=' ')
    print()
    
start = int(input('Enter the start of the range: '))
end   = int(input('Enter the end of the range: '))

find_numbers(start, end)


'''output:

Enter the start of the range: 10
Enter the end of the range: 100
Numbers divisible by num1 and multiple of num2 between 10 and 100:
35 70
'''