from collections import Counter

def anagrams(str1, str2):
    return Counter(str1) == Counter(str2)

value1 = 'abc1'
value2 = '1bac'

print(value1, value2)
print(anagrams(value1, value2))


'''output:

abc1 1bac
True
'''