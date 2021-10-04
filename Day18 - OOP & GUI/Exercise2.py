from turtle import *

tim = Turtle()

tim.penup()
tim.setx(200)
tim.pendown()

tim.setheading(180)

for i in range(50):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()
