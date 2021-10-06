from turtle import Turtle, Screen
import random

POSSIBLE_START = range(-250, 275, 25)
COLOURS = ["red", "green", "white", "violet"]


class Car:
    """Models our cars"""

    def __init__(self):
        self.all_cars = []

    def spawn_car(self):
        """Spawns a car"""
        new_car = Turtle("square")
        new_car.shape("square")
        new_car.penup()
        new_car.color(random.choice(COLOURS))
        new_car.setheading(180)
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.goto(x=350, y=random.choice(POSSIBLE_START))
        self.all_cars.append(new_car)

    def move(self):
        """Moves the car"""
        for x in self.all_cars:
            x.forward(10)

    def limit_cars(self):
        """Check for cars too close and remove them from all_cars list"""
        for x in range(len(self.all_cars)):
            try:
                if self.all_cars[x].distance(self.all_cars[x + 1]) < 30:
                    self.all_cars.remove(x)
                    self.all_cars.remove(x+1)
            except ValueError:
                pass
            except IndexError:
                pass

    def remove_car(self):
        for x in self.all_cars:
            if x.xcor() < -350:
                x.goto(x=350, y=random.choice(POSSIBLE_START))




