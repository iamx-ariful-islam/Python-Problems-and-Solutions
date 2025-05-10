# upper case

# method #1
for i, j in enumerate(range(65, 70), 1):
    print(chr(j)*i)

# method #2
x = '\n'.join(chr(j)*i for i, j in enumerate(range(65, 70), 1))
print(x)



# lower case

# method #1
for i, j in enumerate(range(97, 102), 1):
    print(chr(j)*i)

# method #2
x = '\n'.join(chr(j)*i for i, j in enumerate(range(97, 102), 1))
print(x)


'''output:

A
BB
CCC
DDDD
EEEEE
A
BB
CCC
DDDD
EEEEE
a
bb
ccc
dddd
eeeee
a
bb
ccc
dddd
eeeee
'''