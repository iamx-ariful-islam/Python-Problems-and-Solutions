# pip install pyfiglet

import pyfiglet


# ascii_art
def ascii_art(text, style='Slant'):
    string = pyfiglet.figlet_format(text, font=style)
    return string


if __name__ == '__main__':
    # enter any text
    text = input('Enter Your String: ')
    # enter figlet style
    style= input('Enter String Style: ')
    try:
        print(ascii_art(text, style))
    except: print(ascii_art(text))


'''output:

Enter Your String: python
Enter String Style: slant
                 __  __
    ____  __  __/ /_/ /_  ____  ____
   / __ \/ / / / __/ __ \/ __ \/ __ \
  / /_/ / /_/ / /_/ / / / /_/ / / / /
 / .___/\__, /\__/_/ /_/\____/_/ /_/
/_/    /____/

'''