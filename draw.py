import turtle
def draw():
    turtle.pensize(5)
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.left(70)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(200)
        turtle.right(140)
        turtle.forward(200)
        turtle.left(50)
    turtle.end_fill()
    turtle.penup()

draw()