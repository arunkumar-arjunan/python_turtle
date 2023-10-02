import turtle

turtle.speed(10)
turtle.bgcolor('Black')
colors=['Red','Yellow','Cyan','Orange','Pink','Purple']

for x in range(100):
    turtle.circle(x)
    turtle.color(colors[x%6])
    turtle.left(60)

