import turtle
a = turtle.Screen()
a.bgcolor('cyan')
a.setup(400 , 200)
turtle.title('WELCOME TO TURTLE WINDOW LETS CREATE A SQUARE')
pen= turtle.Turtle()
for i in range(4):
    pen.forward(100)
    pen.right(90)
turtle.done()