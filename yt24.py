# pip install turtle (from terminal)

# Here we will draw a simple home with python turtle the code ⬇⬇:

from turtle import *

Screen().setup(1300, 650)
bgcolor('white')
speed(0)
setpos(-400, -250)

# This function to draw the structure 
def square():
    begin_fill()
    color('brown')
    for i in range(2):
        fd(800)
        left(90)
        fd(350)
        left(90)
    end_fill()

square()

up()
goto(280, -20)
down()

#Here we will draw the windows

def windows():
    for i in range(4):
        for i in range(4):
            fd(100)
            left(90)
        left(90)

begin_fill()
color('#c0c9f0')
windows()
end_fill()
width(3)
color('black')
windows()

up()
goto(-350, -230)
down()

# and this is the door
def door():
    for i in range(4):
        fd(200)
        left(90)
        fd(300)
        left(90)
begin_fill()
color('#145369')
door()
end_fill()
color('black')
door()

up()
goto(-180, -80)
fd(-30)
down()

# This function key is hand handle

def key():
    for c in range(2):
        fd(35)
        left(90)
        fd(50)
        left(90)
    up()
    goto(-192, -60)
    down()
    begin_fill()
    circle(8)
    end_fill()

key()
up()
goto(-400, 100)
down()

# Finally, we will draw the roof

def roof():
        fd(800)
        left(120)
        fd(150)
        left(60)
        fd(650)
        left(60)
        fd(150)


begin_fill()
color('#955242')
roof()
end_fill()

mainloop()
