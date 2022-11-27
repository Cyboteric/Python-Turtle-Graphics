# How to draw skull with python turtle 
# pip install turtle 

from turtle import *

Screen().bgcolor('ivory')
speed(0)
width(10)

up()
setpos(-150, -190)
down()

#                                           Functions

# Draw teeth

def teeth():
    for i in range(2):
        forward(300)
        left(90)
        forward(100)
        left(90)

    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)

teeth()

# Draw  head(skull)

def head():
    # rest setting

    left(180)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(100)

    # create head(skull)
    right(90)
    forward(10)
    circle(100, 90)
    for i in range(16):
        left(11)
        forward(50)
    right(160)
    circle(-90, -70)
    right(10)
    circle(-100, -25)

head()

# Draw eyes and nose

def eyesNose():
    # rest setting
    up()
    setpos(0, 140)
    left(150)
    forward(100)
    down()

    # draw right eye

    begin_fill()
    circle(40)
    end_fill()

    # rest setting

    up()
    left(20)
    forward(-180)
    down()

    # draw left eye

    begin_fill()
    circle(40)
    end_fill()
    up()
    forward(-50)
    down()

    # draw line hack eye

    left(30)
    forward(250)
    backward(390)

    # draw nose

    up()
    right(40)
    forward(220)
    right(350)
    forward(5)
    down()

    begin_fill()
    for c in range(3):
        forward(100)
        left(120)
    end_fill()


eyesNose()
done()