from turtle import Screen
from paddle import Player1, Player2
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=700)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

p1 = Player1()
p2 = Player2()
ball = Ball()
score = ScoreBoard()

ball.speed("slow")

screen.listen()
screen.onkeypress(p1.move_up, "w")
screen.onkeypress(p1.move_down, "s")
screen.onkeypress(p2.move_up, "Up")
screen.onkeypress(p2.move_down, "Down")

game_on = True

while game_on:
    score.update_scoreboard()
    screen.update()

    if score.left_score or score.right_score > 1:
        game_on = False
        ball.hideturtle()
        score.game_over()
        screen.update()
    time.sleep(.08)
    ball.move_forward()

    # Check for wall collision
    if abs(ball.ycor()) > 335:
        new_heading = 360 - ball.heading()
        ball.setheading(new_heading)

    # Check for score
    if (ball.xcor()) > 390:
        ball.refresh()
        score.increase_left_score()
    elif ball.xcor() < -390:
        ball.refresh()
        score.increase_right_score()

    # Check for paddle collision p1
    if abs(ball.distance(p1)) < 30:
        new_heading = 180 - ball.heading()
        ball.setheading(new_heading)

    # Check for paddle collision p2
    if abs(ball.distance(p2)) < 30:
        new_heading = 180 - ball.heading()
        ball.setheading(new_heading)

screen.exitonclick()
