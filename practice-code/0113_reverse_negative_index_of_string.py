s = 'python'

length = len(s)
print(*s, sep=' | ')
print('='*(length*4-2))
print(*range(-len(s), 0, 1))


'''output:

p | y | t | h | o | n
======================
-6 -5 -4 -3 -2 -1
'''