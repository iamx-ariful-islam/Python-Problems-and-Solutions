# pip install pyfiglet

import pyfiglet
from colorama import Fore


text_font = pyfiglet.figlet_format('Hello, Python')
print(Fore.BLUE + text_font)