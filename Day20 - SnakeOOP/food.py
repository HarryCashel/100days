from turtle import Turtle
import random


class Food(Turtle):
    """Models the food"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(.5)
        self.penup()
        self.speed("fastest")
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(random_x, random_y)
