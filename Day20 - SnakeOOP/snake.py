from turtle import *

MOVE_SPEED = 20
STARTING_POS = [(0, 0), (20, 0), (40, 0)]

class Snake:
    """Models our snake"""

    def __init__(self):
        self.food = 0
        self.body = []
        self.create_body()
        self.head = self.body[-1]

    def create_body(self):
        """Creates the initial snake body"""

        for i in STARTING_POS:
            piece = Turtle()
            piece.penup()
            piece.shape("square")
            piece.color("white")
            piece.shapesize(1)
            piece.goto(i)
            self.body.append(piece)

    def move_body(self):
        """Moves the snake body"""
        for i, ix in enumerate(self.body):
            if ix != self.head:
                new_x = self.body[i + 1].xcor()
                new_y = self.body[i + 1].ycor()
                ix.goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def move_left(self):
        self.head.left(90)
