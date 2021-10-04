from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_back():
    tim.backward(10)


def move_left():
    heading = tim.heading() + 10
    tim.setheading(heading)


def move_right():
    heading = tim.heading() - 10
    tim.setheading(heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_right)
screen.onkey(key="space", fun=clear)

screen.exitonclick()
