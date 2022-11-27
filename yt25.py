# Let's draw with turtle 
# You can draw amazing night city with python turtle 

# pip install turtle

# the code here:

from turtle import *

Screen().bgcolor('#282425')
Screen().setup(1100, 650)
width(3)

color('#6d6e71')

# this function to draw square and that represent the windows
def square():
    begin_fill()
    color('#fefefe')
    for i in range(2):
        fd(80)
        left(90)
        fd(60)
        left(90)
    end_fill()


# function to draw small star
def stars():
    color('yellow')
    for i in range(5):
        fd(10)
        right(144)

up()
setpos(0, -70)
down()
begin_fill()
fd(-540)
fd(1080)
left(90)
fd(-320)
left(90)
fd(1090)
left(-90)
fd(320)
end_fill()

# Here this function combind all calls function stars and square and you'll find a lot of setpos()
def setPos_Square_Stars():
    begin_fill()
    # ---------------------------------------
    right(90)
    fd(200)
    # -----------
    left(90)
    fd(300)
    right(90)
    fd(250)
    right(90)
    fd(150)
    # ---------
    left(90)
    fd(150)
    right(90)
    fd(100)
    left(90)
    fd(150)
    # -------------
    left(90)
    fd(300)
    right(90)
    fd(230)
    right(90)
    fd(350)
    end_fill()

    # -------------------------
    up()
    setpos(210, 270)
    down()
    square()

    up()
    setpos(360, 200)
    down()
    square()

    up()
    setpos(280, 80)
    down()
    square()

    up()
    setpos(-50, 50)
    down()
    square()

    up()
    setpos(-250, 80)
    down()
    square()

    up()
    setpos(-340, 220)
    down()
    square()

    up()
    setpos(-330, 300)
    down()
    stars()

    up()
    setpos(-380, 100)
    down()
    stars()

    up()
    setpos(-500, 120)
    down()
    stars()

    up()
    setpos(-400, 200)
    down()
    stars()

    up()
    setpos(-500, 200)
    down()
    stars()

    up()
    setpos(-510, 300)
    down()
    stars()

    up()
    setpos(-100, 300)
    down()
    stars()

    up()
    setpos(100, 200)
    down()
    stars()

    up()
    setpos(100, 300)
    down()
    stars()

    up()
    setpos(10, 150)
    down()
    stars()

    up()
    setpos(-50, 200)
    down()
    stars()

    up()
    setpos(500, 200)
    down()
    stars()

    up()
    setpos(450, 300)
    down()
    stars()


setPos_Square_Stars()
mainloop()