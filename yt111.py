import turtle as tur
import colorsys as cs
tur.setup (800,800)
tur.speed (0)
tur.width(2)
tur.bgcolor('black')
tur.seth(45)
n = 180
for i in range(n):
    
    tur.color(cs.hsv_to_rgb( i/6, i/n, 0.8))
    tur.fillcolor(cs.hsv_to_rgb( i/6, i/n, 1))
    tur.right (90)
    tur.circle(i*1.2,90)

    tur.right(59)
tur.hideturtle()
tur.done()