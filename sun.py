import turtle

if __name__ == '__main__':

    turtle.title('Hi! I\'m Bob the turtle!')
    turtle.setup(width=800, height=800)

    bob = turtle.Turtle(shape='turtle')
    bob.color('orange')

    # Drawing a filled star thingy
    bob.speed(2000)
    bob.fillcolor('yellow')
    bob.pencolor('red')

    for i in range(200):

        bob.begin_fill()
        bob.forward(300 - i)
        bob.left(170)
        bob.forward(300 - i)
        bob.end_fill()

    turtle.exitonclick()