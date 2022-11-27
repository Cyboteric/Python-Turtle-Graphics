import turtle as t
import colorsys
t.bgcolor('black')
t.pencolor('cyan')
t.tracer(2)
t.hideturtle()

def VastCoding():
    for i in range(4):
        t.fd(200)
        t.right(90)

for j in range(500):
    VastCoding()
    t.goto(0, 0)
    t.rt(2)

t.exitonclick()