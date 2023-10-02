import turtle

turtle.speed(0)
turtle.bgcolor('Black')
colors=['Red','Yellow','Pink','Orange',
        'Blue','Green','Cyan','White']

for x in range(300):
    turtle.color(colors[x%8])
    turtle.fd(x)
    turtle.left(90)
