from turtle import *

tim = Turtle()
tim.shape("turtle")

angle = int(input("How many sides?"))
for i in range(angle):
    tim.fd(100)
    tim.left(360/angle)
