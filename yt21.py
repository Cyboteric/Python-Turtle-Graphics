# a lot of circle 


from turtle import *
Screen().bgcolor('black')
speed(0)
up()
setpos(0, -50)
down()
width(2)

for i in range(50):
    color('gold')
    circle(115)
    left(10)
    fd(10)
    if i == 49:
        for c in range(50):
            color('brown')
            circle(80)
            left(10)
            fd(10)

mainloop()