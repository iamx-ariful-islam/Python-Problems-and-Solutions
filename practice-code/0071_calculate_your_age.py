# calculate age

from datetime import date

birth_year = int(input('Enter your birth year: '))

print(f"Wow! You are '{date.today().year - birth_year}' year(s) old")


'''output:

Enter your birth year: 2010
Wow! You are '14' year(s) old
'''