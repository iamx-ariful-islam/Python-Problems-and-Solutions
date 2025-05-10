def find_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                if a**2 + b**2 == c**2:
                    triplets.append((a, b, c))
    return triplets


limit    = int(input('Enter the range limit: '))
triplets = find_pythagorean_triplets(limit)

print('Pythagorean Triplets in the range 1 to', limit, 'are:')
for triplet in triplets:
    print(triplet)
    
    
'''output:

Enter the range limit: 7
Pythagorean Triplets in the range 1 to 7 are:
(3, 4, 5)
'''