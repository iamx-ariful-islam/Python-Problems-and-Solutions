tallies = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}

def RomanNumerialToDecimal(romanNumerial):
    sum = 0
    for i in range(len(romanNumerial)-1):
        left = romanNumerial[i]
        right = romanNumerial[i+1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else: sum += tallies[left]
    sum += tallies[romanNumerial[-1]]
    return sum

roman = input('Enter roman numbers: ').upper()
print('Deciaml number:', RomanNumerialToDecimal(roman))


'''output:

Enter roman numbers: IV
Deciaml number: 4
'''