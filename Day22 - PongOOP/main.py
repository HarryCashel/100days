from turtle import Screen
from paddle import Player1, Player2

screen = Screen()
screen.setup(width=800, height=700)
screen.title("Pong")
screen.bgcolor("black")
# screen.tracer(0)


p1 = Player1()
p2 = Player2()

screen.listen()
screen.onkeypress(p1.move_up, "w")
screen.onkeypress(p1.move_down, "s")
screen.onkeypress(p2.move_up, "Up")
screen.onkeypress(p2.move_down, "Down")

screen.exitonclick()
