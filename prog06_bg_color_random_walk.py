import turtle
import random

turtle.speed(10)
turtle.bgcolor('Black')
turns = 100
distance = 10

for x in range(turns):
    right = turtle.right(random.randint(0,360))
    left = turtle.left(random.randint(0,360))
    turtle.color(random.choice(['Blue','Red','Green','Cyan','Magenta','Pink',
                                'Violet']))
    random.choice([right,left])
    turtle.forward(distance)
                 
