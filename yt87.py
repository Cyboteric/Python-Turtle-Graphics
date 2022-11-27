import turtle
import math
colors = ["red","purple","blue","green","orange","yellow"]
mypen =turtle.pen()
turtle.bgcolor("black")
turtle.speed(200)
for x in range(360):
    turtle.pencolor(colors[x % 6])
    turtle.width(x*10/100+1)
    turtle.left(97)
    turtle.forward(x-10)
    turtle.backward(x)
    turtle.right(90)
turtle.done()