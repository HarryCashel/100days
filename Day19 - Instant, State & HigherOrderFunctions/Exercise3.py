"""Object State and Instances"""

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(1000, 800)

actors = {'c1': 'green', 'c2': 'red', "c3": "violet", "c4": "yellow", "c5": "blue", "c6": "orange"}
list_of_names = []

# Create turtle objects from our dictionary
for name in actors.keys():
    actor = Turtle()
    actor.shape("turtle")
    actor.color(actors[name])
    list_of_names.append(actor)

# Set starting positions
start_x = -450
start_y = -350
for i in list_of_names:
    i.speed("fastest")
    i.penup()
    i.goto(start_x, start_y)
    start_y += 800 / len(list_of_names)

guess = (screen.textinput(prompt="Who will win the race? Enter the colour: ", title="Guess")).lower()

run_game = True

while run_game:

    for i in list_of_names:
        if i.xcor() > 40:
            run_game = False
            winner = i.pencolor()

            if winner == guess:
                print(f"Correct the winning colour was {winner}.")
            else:
                print(f"Sorry the winning colour was {winner}.")
        i.forward(random.randint(0, 10))


screen.exitonclick()
