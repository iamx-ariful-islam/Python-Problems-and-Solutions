# pip install pyfiglet

import random
import pyfiglet
from termcolor import colored


def wish_happy_birthday():
    birthday_msg = pyfiglet.figlet_format("Happy Birthday")
    colors = ["red", "yellow", "green", "cyan", "magenta", "blue"]

    for line in birthday_msg.split("\n"):
        print(colored(line, color=random.choice(colors)))

    print("Wishing You a Bright and Joyful Birthday!!")

wish_happy_birthday()