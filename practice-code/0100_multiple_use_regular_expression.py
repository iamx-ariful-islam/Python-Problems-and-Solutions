import re


data    = '18/Dec/2022 Fifa World Cup final'
pattern = re.compile(r'\d+/[a-zA-Z]+/\d{4}')

if pattern.match(data):
    print('Match')
else:
    print('Not match')
    
    
'''output:

Match
'''