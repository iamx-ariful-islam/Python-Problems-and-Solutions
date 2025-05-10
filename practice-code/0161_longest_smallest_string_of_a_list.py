# find longest words from a list
def longest_words(words):
    return max(words, key=len)

# find smallest words from a list
def smallest_words(words):
    return min(words, key=len)


# default words list
words = ['apple', 'orange', 'cat', 'elephant']
print('List of word:', words)

# print longest words
print('Longest word:', longest_words(words=words))

# print smallest words
print('Smallest word:', smallest_words(words))


'''output:

List of word: ['apple', 'orange', 'cat', 'elephant']
Longest word: elephant
Smallest word: cat
'''