data   = {
    'a': [1, 2, 3, 4, 5],
    'b': [6, 7, 8, 9, 0],
    'c': [1, 3, 5, 7, 9],
    'd': [2, 4, 6, 8, 0],
    'e': [1, 2, 3, 4, 5],
}

print(data.keys())
# print(list(data.keys()))
print(data.values())
# print(list(data.values()))

all_values = sum(data.values(), [])
print(all_values)


'''output:

dict_keys(['a', 'b', 'c', 'd', 'e'])
dict_values([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [1, 3, 5, 7, 9], [2, 4, 6, 8, 0], [1, 2, 3, 4, 5]])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 3, 5, 7, 9, 2, 4, 6, 8, 0, 1, 2, 3, 4, 5]
'''