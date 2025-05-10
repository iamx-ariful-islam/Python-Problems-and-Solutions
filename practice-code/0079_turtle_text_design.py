import colorsys
from turtle import *


bgcolor('black')
h = 1
text = ['Python', 'Turtle']

for i in range(100):
    color(colorsys.hsv_to_rgb(h, 1, 1))
    h += 0.005
    up()
    fd(i*8)
    down()
    write(text[i%2], font=('Arial', int((i+4)/4), 'bold'))
    lt(45)

done()