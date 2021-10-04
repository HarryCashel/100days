from turtle import *

tim = Turtle()
tim.shape("turtle")


def draw_shape(sides):
    """Draws a shape with right angles with as many sides as input"""
    angle = sides
    for i in range(angle):
        tim.fd(100)
        tim.left(360/angle)


for shapes in range(3,101):
    draw_shape(shapes)
