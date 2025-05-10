number = int(input('Enter a number: '))

series    = ' + '.join(str(i) for i in range(1, number+1))
total_sum = sum(range(1, number+1))


print(f'{series} = {total_sum}')



'''output:

1 + 2 + 3 + 4 + 5 + 6 = 21
'''