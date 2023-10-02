import turtle
import time

turtle.color("green")

for angle in range(0,360,5):
    turtle.seth(angle)
    turtle.circle(100)
    time.sleep(1)
