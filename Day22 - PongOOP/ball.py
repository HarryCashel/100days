from turtle import *
import random
POSSIBLE_HEADINGS = [(0, 35), (145, 235), (325, 360)]


class Ball(Turtle):
    """Models the Pong ball"""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color("green")
        self.speed(5)
        self.refresh()

    def refresh(self):
        """Refreshing ball heading and x/y cords"""
        choice = random.choice(POSSIBLE_HEADINGS)
        random_int = random.randint(choice[0], choice[1])
        self.setheading(random_int)

    def detect_wall(self):
        pass

    def detect_paddle(self):
        pass

    def detect_score(self):
        pass
