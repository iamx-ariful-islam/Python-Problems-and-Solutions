# pip install periodictable

import periodictable

def element_info(symbol):
    element = getattr(periodictable, symbol, None)
    if element is None:
        print('Element not found')
        return
    info = {
        'Name': element.name,
        'Number': element.number,   # Atomic
        'Mass': element.mass, # Atomic
        'Density': element.density
    }
    for key, value in info.items():
        print(f'{key}\t: {value}')


symbol = input("Enter the element symbol: ").capitalize()
element_info(symbol=symbol)


'''output:

Enter the element symbol: ag
Name    : silver
Number  : 47
Mass    : 107.8682
Density : 10.5
'''