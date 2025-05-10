from collections import Counter

with open('text_file.txt') as fl:
    words = fl.read().split()
    print(Counter(words).most_common(10))


'''output:

[('Hello', 1), ('world', 1)]
'''