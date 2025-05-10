txt  = 'hello world'
txt1 = '22/02/2022'

print(txt.capitalize())
print(txt.lower())
print(txt.upper())
print(txt.center(len(txt)+6, '*'))
print(txt.count('l'))
print(txt.index('o'))
print(txt.find('or'))
print(txt1.replace('/', '-'))
print(txt1.split('/'))
print(txt.isalnum())
print(txt.isnumeric())
print(txt.islower())
print(txt.isupper())


''' output:

Hello world
hello world
HELLO WORLD
***hello world***
3
4
7
22-02-2022
['22', '02', '2022']
False
False
True
False
'''