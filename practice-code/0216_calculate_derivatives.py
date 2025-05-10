# pip install sympy

import sympy as sym


x    = sym.Symbol('x')
func = x**4+4*x**2+5*x-6
# sym.Derivative(func, x) # derivative expression
# sym.Derivative(func, x, evaluate=True) # calculate derivative of func
# func.diff(x) # or use this for the same

expr = sym.lambdify(x, func)
expr_der = sym.lambdify(x, func.diff(x))

print(f'Value of func at x=5: {expr(5)}')
print(f'Derivative of func at x=5: {expr_der(5)}')



'''output:

Value of func at x=5: 744
Derivative of func at x=5: 545
'''