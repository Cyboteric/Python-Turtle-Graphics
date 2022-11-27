import turtle as t
import colorsys

t.bgcolor('black')
t.tracer(10)
t.pensize(2)
h = 0.0

for i in range(500):
    color = colorsys.hsv_to_rgb(h, 0.8, 1)
    t.pencolor(color)
    t.circle(130)
    t.left(95)
    t.circle(90)
    h+= 0.005