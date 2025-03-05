import turtle

sc = turtle.Screen()

turtle.Screen().bgcolor("blue")

sc.setup(300,500)

turtle.title("This is the turtle canvas!")

pen = turtle.Turtle()

for i in range(4):

    pen.forward(70)

    pen.right(90)

turtle.done()