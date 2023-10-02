import turtle

turtle.speed(0)
turtle.bgcolor('Black')
colors=['Red','Yellow','Pink','Orange']

for x in range(300):
    turtle.color(colors[x%4])
    turtle.fd(x)
    turtle.left(90)
