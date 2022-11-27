import turtle
import colorsys
vk=turtle.Turtle()
turtle.bgcolor("black")
turtle.tracer(78)
vk.pensize(2)

h = 0.001
n=889
for i in range(767):
    c=colorsys.hsv_to_rgb (h,1,.7)
    h=h+(1/n)
    vk.up()
    vk.goto(-8,25)
    vk.down()
    vk.pencolor(c)
    vk.fd(i)
    vk.rt(89)
    vk.fillcolor(c)
    vk.begin_fill()
    vk.circle(15,320)
    vk.end_fill()
    vk.lt(179)
    vk.bk(i)
    vk.fd(i)
    vk.rt(6)
turtle.done()