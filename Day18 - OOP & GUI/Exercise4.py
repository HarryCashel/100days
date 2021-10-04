import turtle
from turtle import *
import random

direction = [90, 180, 270, 360]
turtle.colormode(255)


def random_rbg():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r, b, g


tim = Turtle()
tim.pensize(6)

for i in range(1000):
    tim.speed(20)
    tim.forward(25)
    tim.color(random_rbg())
    tim.setheading(random.choice(direction))
