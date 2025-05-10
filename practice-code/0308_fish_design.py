import math

def fish_pattern(n):
    n += 14
    s = n / 10
    t = 4.72 / n

    for j in range(math.floor(s), -math.ceil(s) - 1, -1):
        i = 0
        while i <= 4:
            if ((j < s / 2 and j > s / 4 and i < 1 and i > 0.8) or
                (j == 0 and i < 0.6) or
                (math.pow(j / s, 2) >= math.pow(math.sin(i), 2))):
                print(' ', end='')
            else:
                print('*', end='')
            i += t
        print()


n = float(input('Enter the size of fish: '))
fish_pattern(n)