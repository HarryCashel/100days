from turtle import Screen
from paddle import Player1, Player2
from ball import Ball

screen = Screen()
screen.setup(width=800, height=700)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


p1 = Player1()
p2 = Player2()
ball = Ball()
ball.forward(100)
screen.update()

screen.listen()
screen.onkeypress(p1.move_up, "w")
screen.onkeypress(p1.move_down, "s")
screen.onkeypress(p2.move_up, "Up")
screen.onkeypress(p2.move_down, "Down")

screen.exitonclick()
