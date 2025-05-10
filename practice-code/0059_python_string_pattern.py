s = 'Python'

# method #1
x = []
for i in range(len(s)+1):
    x.append(s[:i])

for x in x+x[::-1]:
    print(x)

# methed #2
p = [s[:i] for i in range(len(s)+1)]
print(*p+(p[::-1]), sep='\n')


'''output:

P
Py
Pyt
Pyth
Pytho
Python
Python
Pytho
Pyth
Pyt
Py
P
'''