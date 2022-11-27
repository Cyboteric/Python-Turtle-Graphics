import turtle as t
t.Screen()
t.pencolor("cyan")#F9CCD3
t.goto(0, 200)
t.bgcolor("black")
t.speed(0)
size = 0
angle = 0
i = 0
while True:
    t.forward(size)
    t.right(angle)
    size += 3
    angle += 1
    i += 1
    if angle == 200:
        break

t.mainloop()