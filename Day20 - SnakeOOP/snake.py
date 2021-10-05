from turtle import *

MOVE_SPEED = 20
STARTING_POS = [(0, 0), (20, 0), (40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Models our snake"""

    def __init__(self):
        self.food = 0
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for cord in STARTING_POS:
            self.create_piece(cord)

    def create_piece(self, piece_pos):
        """Creates the initial snake body"""
        piece = Turtle()
        piece.penup()
        piece.shape("square")
        piece.color("white")
        # piece.shapesize(1)
        piece.goto(piece_pos)
        self.body.append(piece)

    def add_piece(self):
        """Adds a segment to the end of the snake"""
        last_piece_pos = self.body[-1].position()
        self.create_piece(last_piece_pos)

    def move_body(self):
        """Moves the snake body"""
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
