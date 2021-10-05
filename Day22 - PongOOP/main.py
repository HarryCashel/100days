from turtle import Screen
from paddle import Player1, Player2
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=700)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


p1 = Player1()
p2 = Player2()
ball = Ball()
ball.speed("fastest")


screen.listen()
screen.onkeypress(p1.move_up, "w")
screen.onkeypress(p1.move_down, "s")
screen.onkeypress(p2.move_up, "Up")
screen.onkeypress(p2.move_down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    ball.move_forward()

    # Check for wall collision
    if abs(ball.ycor()) > 350:
        new_heading = 360 - ball.heading()
        ball.setheading(new_heading)

    # Check for score
    if abs(ball.xcor()) > 390:
        ball.refresh()


screen.exitonclick()
