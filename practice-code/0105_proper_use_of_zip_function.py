# students info
name  = ['A', 'B', 'C']
age   = [23, 25, 27]
score = [3.70, 3.80, 3.90]

# zip students info list
info1 = zip(name, age, score)
info2 = zip(name, age, score)

# show unzip info as tuple
# zip objects or unzip zip objects
print(*info1) # or
n, a, s = zip(*info2)
print(n, a, s)


'''output:

('A', 23, 3.7) ('B', 25, 3.8) ('C', 27, 3.9)
('A', 'B', 'C') (23, 25, 27) (3.7, 3.8, 3.9)
'''