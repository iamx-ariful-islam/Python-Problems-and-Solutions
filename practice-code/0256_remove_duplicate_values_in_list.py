# method #1

lst = ['a', 'b', 'c', 'd', 'a', 'c']
print(list(set(lst)))


# method #2

lst = ['a', 'b', 'c', 'd', 'a', 'c']
print(list({}.fromkeys(lst).keys()))


# method #3

from collections import OrderedDict

lst = ['a', 'b', 'c', 'd', 'a', 'c']
print(list(OrderedDict.fromkeys(lst).keys()))



'''output:

['d', 'a', 'c', 'b']
['a', 'b', 'c', 'd']
['a', 'b', 'c', 'd']
'''