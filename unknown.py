import turtle

if __name__ == '__main__':

    turtle.title('Hi! We\'re Bob and Larry!')
    turtle.setup(width=800, height=800)

    bob = turtle.Turtle(shape='turtle')
    larry = turtle.Turtle(shape='turtle')
    bob.color('orange')
    larry.color('purple')

    bob.penup()
    larry.penup()
    bob.goto(-180, 200)
    larry.goto(-150, 200)
    for i in range(30, -30, -1):

        bob.stamp()
        larry.stamp()
        bob.right(i)
        larry.right(i)
        bob.forward(20)
        larry.forward(20)

    turtle.exitonclick()