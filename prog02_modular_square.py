import turtle
import time

def square(length):
    for i in range(4):
        print(i)
        turtle.forward(length)
        turtle.left(90)

if __name__=="__main__":
    square(150)
    square(50)
    time.sleep(5)
    turtle.bye()
