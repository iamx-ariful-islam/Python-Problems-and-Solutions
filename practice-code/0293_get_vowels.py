def get_vowels(string):
    return [each for each in string if each in 'aeiou']


word = input('Enter a word to check vowels: ')
print(get_vowels(word))



'''output:

Enter a word to check vowels: Hello, Python
['e', 'o', 'o']
'''