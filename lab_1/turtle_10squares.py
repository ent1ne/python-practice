import turtle
turtle.shape ("turtle")

a = 10
x = 1
for i in range(a):
    turtle.pendown()
    for k in range(4):
        turtle.forward(x * 10)
        turtle.right(90)
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.back(10)
    x += 2
