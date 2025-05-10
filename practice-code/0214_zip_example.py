names  = ['Alice', 'Bob']
scores = [85, 90]

for name, score in zip(names, scores):
    print('{:10}: {}'.format(name, score))
    
for name, score in zip(names, scores):
    print('{:*^15}: {}'.format(name, score))
    
    
'''output:

Alice     : 85
Bob       : 90
*****Alice*****: 85
******Bob******: 90
'''