# pip install pyfiglet

import pyfiglet
from termcolor import colored


text = pyfiglet.figlet_format("Happy valentine's", font='slant')

print(colored(text, 'red'))