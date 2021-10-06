from turtle import Turtle
LEFT_ALIGNMENT = "left"
RIGHT_ALIGNMENT = "right"
FONT = ("Courier", 12, "normal")
END_FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    """Models a scoreboard for Pong"""

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates score and refreshes scoreboard"""

        self.write(f"--Score: {self.left_score}", align=LEFT_ALIGNMENT, font=FONT)
        self.write(f"Score: {self.right_score}", align=RIGHT_ALIGNMENT, font=FONT)

    def game_over(self):
        """Shows the game over scoreboard"""

        self.goto(0, 0)
        winner = max(self.left_score, self.right_score)
        if winner == self.left_score:
            self.write(f"Player 1 wins", align="center", font=END_FONT)
        elif winner == self.right_score:
            self.write(f"Player 2 wins", align="center", font=END_FONT)

    def increase_left_score(self):
        """Adds point to left team"""
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_right_score(self):
        """Adds point to right team"""
        self.right_score += 1
        self.clear()
        self.update_scoreboard()
