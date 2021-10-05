from turtle import *
import random
POSSIBLE_HEADINGS = [(0, 45), (145, 235), (300, 360)]


class Ball(Turtle):
    """Models the Pong ball"""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color("green")
        self.refresh()

    def refresh(self):
        """Refreshing ball heading and x/y cords"""
        choice = random.choice(POSSIBLE_HEADINGS)
        random_int = random.randint(choice[0], choice[1])
        self.goto(0, 0)
        self.setheading(random_int)

    def move_forward(self):
        """Moves the ball"""
        self.forward(20)
