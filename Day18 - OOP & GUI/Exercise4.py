from turtle import *
import random

turtle_colours = ["red", "green", "blue", "purple", "orange", "violet"]
direction = [90, 180, 270, 360]

tim = Turtle()
tim.pensize(6)

for i in range(1000):
    tim.speed(20)
    tim.forward(25)
    tim.color(random.choice(turtle_colours))
    tim.setheading(random.choice(direction))
