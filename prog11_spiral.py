import turtle
import random

turtle.speed(0)
turtle.bgcolor('Black')
colors=['Red','Yellow','Orange'
        ,'Green','Cyan','White']

for x in range(300):
    turtle.color(colors[x%6])
    turtle.fd(x)
    turtle.left(59)
