import textwrap


text = 'I love Python coding'

wrapped_text = textwrap.wrap(text=text, width=10)

for line in wrapped_text:
    print(line)
    

'''output:

I love
Python
coding
'''