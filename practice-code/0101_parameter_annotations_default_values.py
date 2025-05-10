# parameter annotations describe the details of parameter documentation as dictionary
# set default value of parameter annotations


# method #1
def add(a:str='Hello', b:str='World'):
    return a+b

print('Annotations:', add.__annotations__)
print('Return output:', add())

print()

# method #2
def add(a:int, b:int=5)->int:
    return a+b

print('Annotations:', add.__annotations__)
print('Return output:', add(3))

print()

# method #3
def add(a:int=2, b:int=5)->'Hello':
    return a+b

print('Annotations:', add.__annotations__)
print('Return output:', add(3, 2))


'''output:

Annotations: {'a': <class 'str'>, 'b': <class 'str'>}
Return output: HelloWorld

Annotations: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
Return output: 8

Annotations: {'a': <class 'int'>, 'b': <class 'int'>, 'return': 'Hello'}
Return output: 5
'''