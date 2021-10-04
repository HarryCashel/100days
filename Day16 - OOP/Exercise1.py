from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("yellow")
my_screen = Screen()
my_screen.setup(width=.75, height=.75, startx=None, starty=None)

print(my_screen)


timmy.forward(200)
# timmy.home()
# timmy.setheading(90)
# timmy.forward(200)

my_screen.exitonclick()