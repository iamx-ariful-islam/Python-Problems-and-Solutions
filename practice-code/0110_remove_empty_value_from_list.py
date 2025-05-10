old_list = [12, 0, 34, 10, None, 0.0, False]
new_list = [i for i in old_list if i]

print('Remove empty value from list')
print('Before remove :', old_list)
print('After remove  :', new_list)


'''output:

Remove empty value from list
Before remove : [12, 0, 34, 10, None, 0.0, False]
After remove  : [12, 34, 10]
'''