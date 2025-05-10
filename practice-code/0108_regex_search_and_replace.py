import re

data    = '18/Dec/2022 Fifa World Cup final'
pattern = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')

print('Before: ', data)

# convert to 18/Dec/2022 to 2022-Dec-18
m_data = pattern.sub(r'\3-\2-\1', data)
print('Modify: ', m_data)


'''output:

Before:  18/Dec/2022 Fifa World Cup final
Modify:  2022-Dec-18 Fifa World Cup final
'''