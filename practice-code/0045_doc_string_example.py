# docstrings or documentation strings

# method #1
def add(a, b):
    '''
    this is the docstrings. docstring always write in the first line of code.
    if docstring not in first line of code then it call a comment and docstring print None.
    '''
    return a+b

print('DocStrings:', add.__doc__)
print('Return output:', add(2, 3))

print()

# method #2
def add(a, b):
    print('Output:')
    '''
    this is the docstrings. docstring always write in the first line of code.
    if docstring not in first line of code then it call a comment and docstring print None.
    '''
    return a+b

print('DocStrings:', add.__doc__)
print('Return output:', add(2, 3))
