from turtle import *
import random

tim = Turtle()
tim.shape("turtle")
turtle_colours = ["red", "green", "blue", "purple", "orange", "violet"]


def draw_shape(sides):
    """Draws a shape with right angles with as many sides as input"""
    angle = sides
    for i in range(angle):
        tim.fd(100)
        tim.left(360/angle)


for shapes in range(3,101):
    tim.color(random.choice(turtle_colours))
    draw_shape(shapes)
