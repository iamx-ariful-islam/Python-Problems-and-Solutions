import turtle
import random as rand


# set default colors
colors = ['red', 'cyan', 'pink', 'yellow', 'green', 'orange']

t = turtle.Turtle()
t.speed(1000)
t.hideturtle()
ln = 100
an = 50

size = 5

for i in range(ln):
    color = rand.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i+20)
    t.pendown()
    t.left(angle=an)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    
turtle.exitonclick()