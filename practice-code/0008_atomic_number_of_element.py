# pip install periodictable

import periodictable


# enter a atomic number of a element
atomic_num = int(input('Enter element atomic no: '))

# find the element using number
element = periodictable.elements[atomic_num]

# show the element details
print('Atomic number  :', element.number)
print('Element symbol :', element.symbol)
print('Element name   :', element.name)
print('Atomic mass    :', element.mass)
print('Density        :', element.density)


'''output:

Enter element atomic no: 74 
Atomic number  : 74
Element symbol : W
Element name   : tungsten
Atomic mass    : 183.84
Density        : 19.3
'''