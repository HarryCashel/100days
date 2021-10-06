from turtle import Turtle

SPEED = 20


class Player(Turtle):
    """Models our movable player character"""
    def __init__(self, colour):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color(colour)
        self.refresh()

    def refresh(self):
        """Refresh player position"""
        self.goto(x=0, y=-320)
        self.setheading(90)

    def move_up(self):
        """Moves player north"""
        self.forward(SPEED)

    def move_left(self):
        """Moves player west"""
        self.left(SPEED)

    def move_right(self):
        """Moves player east"""
        self.right(SPEED)
