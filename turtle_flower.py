import turtle
turtle.shape ("turtle")

def flower (x, y):
    a = 0
    while a < 6:
        turtle.circle (x)
        turtle.right (y)
        a += 1

flower (100, 60)
flower (50, 60)

