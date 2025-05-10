def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
        return count
    

num = int(input('Enter an integer: '))
print(f'The number of set bits in {num} is {count_set_bits(num)}')



'''output:

Enter an integer: 12
The number of set bits in 12 is 0
'''