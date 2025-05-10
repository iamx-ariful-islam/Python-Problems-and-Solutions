def check_duplicate(lst):
    return len(lst) != len(set(lst))


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 2, 1]

print('List 1:', list1)
print('Ouput1:', check_duplicate(list1))

print('List 2:', list2)
print('Ouput2:', check_duplicate(list2))


'''output:

List 1: [1, 2, 3, 4, 5]
Ouput1: False

List 2: [1, 2, 3, 2, 1]
Ouput2: True
'''