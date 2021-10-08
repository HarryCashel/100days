import turtle
import pandas

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
state_data = pandas.read_csv("50_states.csv")

# Create a dictionary with state names as keys and the coordinates
# of that state as the values
# we will use these to verify user input data and print the state name
# to our map

state_name_key = list(state_data["state"])
state_x = tuple(state_data["x"])
state_y = tuple(state_data["y"])
coords = list(zip(state_x, state_y))

state_dict = {state: cords for state, cords in zip(state_name_key, coords)}

# print(state_name_key)
screen = turtle.Screen()
screen.title("USA States")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

screen.bgpic(picname="blank_states_img.gif")


# function to find x, y cords on the turtle screen
def mouse_coord(x, y):
    print(x, y)


# Set a conditional for our game loop
play = True

while play:
    import time
    # Take input from user and store in variable, title function as states in the csv are in that format
    s_answer = screen.textinput(title="Guess", prompt="What's a state in the US? ").title()
    try:
        # If user input is in our data find the coords from our dictionary and use a turtle object to print
        # to that location using our function
        if s_answer in state_dict.keys():
            correct = s_answer
            x = state_dict[correct][0]
            y = state_dict[correct][1]
            pen.goto(x, y)
            pen.write(arg=correct)
    except AttributeError:
        pen2 = turtle.Turtle()
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0, 0)
        pen2.write(arg="NO, try again")
        time.sleep(1)
        pen2.clear()
