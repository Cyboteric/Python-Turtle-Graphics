import turtle as tur
import colorsys as cs
tur. bgcolor('black')
tur. tracer(10)
tur.width(2)
def square(x):
    for i in range(3):
        tur. forward (x)
        tur. left (90)
    tur.forward(x)
n = 35
for i in range(n):
    tur. color(cs.hsv_to_rgb(1-i/n,1-i/n,1) )
    for j in range(4):
      square(30+( i*3) )
      tur.circle(30+(1*3) )
tur.hideturtle()
tur.done()