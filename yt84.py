import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)

for i in range(220):
    t.color('orangered')
    t.circle(190-i, 90)
    t.lt(90)
    t.color('yellow')
    t.circle(190-i, 90)
    t.left(18)