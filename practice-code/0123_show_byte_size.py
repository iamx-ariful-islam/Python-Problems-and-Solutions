def ByteSize(string):
    return len(string.encode('utf8'))

_string = 'Python'

print('Input :', _string)
print('Output:', ByteSize('Python'))


'''output:

Input : Python
Output: 6
'''