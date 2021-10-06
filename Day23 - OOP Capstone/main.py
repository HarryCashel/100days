from scoreboard import ScoreBoard
from turtle import Screen
from player import Player
from car import Car
import random
import time


def level_up():
    if player.ycor() > 340:
        scoreboard.level_up()
        player.refresh()


DIFFICULTY = {'easy': 18, 'medium': 9, 'hard': 6, 'insane': 3}


# screen properties
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(800, 700)
screen.title("RUN")

# create class instances
player = Player(screen.textinput(title="colour", prompt="What colour would you like?"))
difficulty = DIFFICULTY[screen.textinput(title="select", prompt="'easy', 'medium', 'hard', or 'insane'")]
car = Car()
scoreboard = ScoreBoard()

# Game conditional and logic
test = True

# listen for keypress
screen.listen()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")

while test:
    car.limit_cars()
    car.remove_car()
    car.move()
    time.sleep(.1)
    screen.update()
    level_up()
    for _ in car.all_cars:
        if _.distance(player) < 20:
            test = False

    roll = random.randint(1, difficulty)
    if roll < 2:
        car.spawn_car()
    car.move()

scoreboard.game_over()
screen.exitonclick()