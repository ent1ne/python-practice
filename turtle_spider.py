import turtle
turtle.shape ("turtle")

n = int(input("How many legs should the spider have? "))
for i in range (n):
    turtle.forward (50)
    turtle.stamp ()
    turtle.backward (50)
    turtle.right (360 / n)
 
