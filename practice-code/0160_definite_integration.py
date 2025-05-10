# pip install sympy

import sympy as sp


x = sp.Symbol('x')
f = input('Enter the function(in terms of x): ')

F_indefinite = sp.integrate(f, x)
print('Indefinite integral ∫f(x) dx=', F_indefinite)

a = float(input('Enter the lower limit of integration: '))
b = float(input('Enter the upper limit of integration: '))

F_definite = sp.integrate(f, (x, a, b))
print(f'Definite integral ∫f(x) dx from {a} to {b} =', F_definite) # ='%.2f' % F_definite or round(F_definite, 2) for 2 digit after decimal


'''output:

Enter the function(in terms of x): sin(x)
Indefinite integral ∫f(x) dx= -cos(x)
Enter the lower limit of integration: 0
Enter the upper limit of integration: 1
Definite integral ∫f(x) dx from 0.0 to 1.0 = 0.459697694131860

Enter the function(in terms of x): x^2 + 3
Indefinite integral ∫f(x) dx= x**3/3 + 3*x
Enter the lower limit of integration: 9
Enter the upper limit of integration: 27
Definite integral ∫f(x) dx from 9.0 to 27.0 = 6372.00000000000

Enter the function(in terms of x): x^2
Indefinite integral ∫f(x) dx= x**3/3
Enter the lower limit of integration: 3
Enter the upper limit of integration: 27
Definite integral ∫f(x) dx from 3.0 to 27.0 = 6552.00000000000
'''