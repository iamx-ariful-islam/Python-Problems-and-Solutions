# pip install webcolors

import webcolors


# color name to hex code
def color_name_to_code(color_name):
    try:
        color_code = webcolors.name_to_hex(color_name)
        return color_code
    except ValueError: return None

# hex code to color name
def color_code_to_name(color_code):
    try:
        color_name = webcolors.hex_to_name(color_code)
        return color_name
    except ValueError: return None
    
# color name to rgb values
def color_name_to_rgb(color_name):
    try:
        color_rgb = webcolors.name_to_rgb(color_name)
        return color_rgb
    except ValueError: return None
    
# enter a color name
color_name = input('Enter color name : ')
color_code = color_name_to_code(color_name)

print('Color code :', color_code)
print('RGB code   :', color_name_to_rgb(color_name))
print('Color name :', color_code_to_name(color_code))


'''output:

Enter color name : red
Color code : #ff0000
RGB code   : IntegerRGB(red=255, green=0, blue=0)
Color name : red
'''