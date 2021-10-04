from turtle import *


class Snake:
    """Models our snake"""

    def __init__(self):
        self.food = 0
        self.body = []
        self.starting_pos = [(0, 0), (20, 0), (40, 0)]
        self.create_body()

    def create_body(self):
        """Creates the initial snake body"""

        for i in range(3):
            piece = Turtle()
            piece.penup()
            piece.shape("square")
            piece.goto(self.starting_pos[i - 1])
            self.body.append(piece)

snake = Snake()

exitonclick()