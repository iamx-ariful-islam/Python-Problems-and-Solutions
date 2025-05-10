# parameter annotations describe the details of parameter documentation as dictionary

# method #1
def add(a, b):
    return a+b

print('Annotations:', add.__annotations__) # print empty dictionary
print('Return output:', add(2, 3))

print()

# method #2
def add(a:int, b:int):
    return a+b

print('Annotations:', add.__annotations__)
print('Return output:', add(2, 3))

print()

# method #3
def add(a:int, b:int)->int:
    return a+b

print('Annotations:', add.__annotations__)
print('Return output:', add(2, 3))

print()

# method #4
def add(a:'First value', b:'second value') -> 'Output value':
    return a+b

print('Annotations:', add.__annotations__)
print('Return output:', add(2, 3))

print()

# method #5
def add(a, b) -> None:
    return a+b

print('Annotations:', add.__annotations__)
print('Return output:', add(2, 3))

print()

# method #6
def add(a:int, b:int):
    return a+b

print('Annotations:', add.__annotations__)
print('Return output:', add('a', 'b'))

print()

# method #7
def add(a:int, b:int)->str:
    return a+b

print('Annotations:', add.__annotations__)
print('Input:')
a = 2
b = 3
print(a, type(a))
print(b, type(b))
print('Return output:')
x = add(a, b)
print(x, type(x))