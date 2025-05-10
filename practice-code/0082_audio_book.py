# pip install pyttsx3

import pyttsx3


# read text from txt file
abook = open(r'abook.txt')
btext = abook.readlines()

engine = pyttsx3.init()

# engine read line bye line from text file
for x in btext:
    engine.say(x)
    engine.runAndWait()