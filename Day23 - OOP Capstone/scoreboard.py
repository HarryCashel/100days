from turtle import Turtle

FONT = ("Courier", 12, "normal")
END_FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.goto(-350, 340)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Shows level"""
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        """levels up da scoreboard"""
        self.level += 1
        self.clear()
        self.update_scoreboard()