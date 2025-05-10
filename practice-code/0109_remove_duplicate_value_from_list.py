def dedupe(items):
    seen = set()
    for element in items:
        if element in seen:
            yield element
        seen.add(element)

a = [1, 2, 3, 4,7, 8, 1, 2, 5, 6, 7, 4]
print('Remove duplicates without changing order')
print('Before remove :', a)
print('After remove  :', list(dedupe(a)))


'''output:

Remove duplicates without changing order
Before remove : [1, 2, 3, 4, 7, 8, 1, 2, 5, 6, 7, 4]
After remove  : [1, 2, 7, 4]
'''