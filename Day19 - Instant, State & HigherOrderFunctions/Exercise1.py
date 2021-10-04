from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()

screen.onkeypress(key="Up", fun=move_forward)

screen.exitonclick()