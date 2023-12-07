import turtle
turtle.speed(10)
scale = 50
for i in range(12):
    turtle.right(60)
    turtle.forward(1*scale)
    turtle.right(60)
    turtle.forward(1*scale)
    turtle.right(270)
turtle.up()
for x in range(-8, 3+1):
    for y in range(-8, 3+1):
        turtle.goto((x*scale, y*scale))
        turtle.dot(2)
input()