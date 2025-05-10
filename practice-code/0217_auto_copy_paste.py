# pip install pyperclip

import pyperclip as pc


text1 = input('Enter a text : ')
pc.copy(text1)

text2 = pc.paste()

print('Copy text:', text2)



'''output:

Enter a text : Hello Python
Copy text: Hello Python
'''