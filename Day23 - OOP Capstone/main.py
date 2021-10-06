from turtle import Screen
from player import Player
import time


# screen properties
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(800, 700)
screen.title("RUN")

# create class instances
player = Player(screen.textinput(title="colour", prompt="What colour would you like?"))

# Game conditional and logic
game = True
while game:
    time.sleep(.1)
    screen.update()

screen.exitonclick()
