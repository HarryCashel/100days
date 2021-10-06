from turtle import Turtle, Screen
import time


# screen properties
screen = Screen()
screen.bgcolor("grey")
screen.tracer(0)
screen.setup(800, 700)


# Game conditional and logic
game = True
while game:
    time.sleep(.1)
    screen.update()

screen.exitonclick()
