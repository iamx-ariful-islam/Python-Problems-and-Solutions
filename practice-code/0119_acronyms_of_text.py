phrase_input = input('Enter a phrase: ')
texts = phrase_input.split()

acronyms = ""

for text in texts:
    acronyms = acronyms+str(text[0]).upper()
    
print('Acronyms text:', acronyms)


'''output:

Enter a phrase: all is well
Acronyms text: AIW
'''