li1 = [1, 3, 2, 5]

li2 = sorted(range(len(li1)), key=lambda k: li1[k])

print('values: ', li1)
print('index : ', li2)
print()
print('values: ', sorted(li1))
print('index : ', sorted(li2))


'''output:

values:  [1, 3, 2, 5]
index :  [0, 2, 1, 3]

values:  [1, 2, 3, 5]
index :  [0, 1, 2, 3]
'''