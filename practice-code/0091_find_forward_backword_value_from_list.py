import random


List = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(List)
print('Length:', len(List))

choice = random.choice(List)
fkey   = List[(List.index(choice) + 2) % 26]
bkey   = List[(List.index(choice) - 2) % 26]

print(f'choose character : {choice}\t= {List.index(choice)}(index)')
print(f'Forward key      : {fkey}  \t= {List.index(fkey)}(index)')
print(f'Backward key     : {bkey}  \t= {List.index(bkey)}(index)')

print(choice, fkey, bkey)


'''
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Length: 26
choose character : F    = 5(index)
Forward key      : H    = 7(index)
Backward key     : D    = 3(index)
F H D
'''