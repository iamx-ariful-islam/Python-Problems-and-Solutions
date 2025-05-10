import re


# set default value
data    = '18/Dec/2022 Fifa World Cup final'

# set pattern
pattern = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')
result  = pattern.match(data)

day, month, year = result.groups()
print('Data  :', data)
print('Day   :', day)
print('Month :', month)
print('Year  :', year)


'''output:

Data  : 18/Dec/2022 Fifa World Cup final
Day   : 18
Month : Dec
Year  : 2022
'''