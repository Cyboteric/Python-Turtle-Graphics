import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(2)
hue = 0.3
t.hideturtle()

def VastCoding():
    global hue
    for i in range(4):
        color = colorsys.hsv_to_rgb(hue, 1,1)
        hue+= 0.010
        t.pencolor(color)
        t.fd(200)
        t.right(90)

for j in range(500):
    VastCoding()
    t.goto(0, 0)
    t.rt(2)

t.exitonclick()