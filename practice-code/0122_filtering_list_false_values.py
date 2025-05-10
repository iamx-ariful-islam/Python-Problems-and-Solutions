def filtering(lst):
    return list(filter(None, lst))

lst = [None, 1, 3, 0, "", 5, 7, '']

print('Before filter:', lst)
print('After filter :', filtering(lst=lst))


'''output:

Before filter: [None, 1, 3, 0, '', 5, 7, '']
After filter : [1, 3, 5, 7]
'''