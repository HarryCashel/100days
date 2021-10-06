from turtle import Screen
from player import Player
from car import Car
import random
import time

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

# Game conditional and logic
test = True

# listen for keypress
screen.listen()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")

while test:
    time.sleep(.1)
    screen.update()
    car.limit_cars()
    car.remove_car()
    while len(car.all_cars) < 100:
        if player.ycor() > 340:
            player.refresh()
        time.sleep(.1)
        screen.update()
        roll = random.randint(1, difficulty)
        if roll < 2:
            car.spawn_car()
        car.move()
    car.move()
