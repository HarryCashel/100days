import turtle
from turtle import *
import random

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")


def random_rbg():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r, b, g


def draw(degree):

    for _ in range(int(360/degree)):
        tim.color(random_rbg())
        tim.circle(100)
        tim.setheading(tim.heading() + degree)

draw(10)
