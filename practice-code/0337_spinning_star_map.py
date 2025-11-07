import turtle


t = turtle.Turtle()
t.speed(8)
s = turtle.Screen()
s.bgcolor('black')

for i in range(36):
    t.color('cyan')
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward(200)
    t.backward(200)
    t.right(10)

turtle.done()