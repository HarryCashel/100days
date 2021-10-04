from turtle import Turtle

timmy = Turtle()

timmy.shape("turtle")
timmy.penup()
timmy.setheading(360 - 45)
timmy.forward(50)

timmy.pendown()
timmy.setheading(90)

for i in range(4):
    timmy.forward(100)
    timmy.left(90)

