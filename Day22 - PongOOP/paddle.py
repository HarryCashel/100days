from turtle import *

MOVEMENT_SPEED = 40


class Paddle(Turtle):

    def __init__(self, ):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        """Creates properties and state for objects"""
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=4)
        self.setheading(90)

    def move_up(self):
        """Moves paddle up"""
        if self.ycor() < 300:
            self.forward(MOVEMENT_SPEED)

    def move_down(self):
        """Moves paddle up"""
        if self.ycor() > - 300:
            self.back(MOVEMENT_SPEED)


class Player1(Paddle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.goto(-385, 0)


class Player2(Paddle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.goto(385, 0)

