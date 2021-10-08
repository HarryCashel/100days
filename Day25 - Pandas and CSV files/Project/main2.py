import turtle
import pandas

# Screen properties
screen = turtle.Screen()
screen.title("USA States")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# import csv
state_data = pandas.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < len(list(state_data.state)):


    num_of_correct = len(guessed_states)
    guess = screen.textinput(f"You have {num_of_correct}/50 states", prompt="Guess a state").title()

    if guess == "Exit":
        break
    # Check if answer_state is one of states in 50_states.csv

    # Need to convert to list to check for membership using in keyword
    all_states = state_data["state"].tolist()
    if guess.title() in all_states:
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        state = state_data[state_data.state == guess]
        pen.goto(int(state.x), int(state.y))
        pen.write(guess)
        guessed_states.append(guess)

    else:
        print("no")


# States in guessed and not in all_states list
# Create a list of missed states and convert to csv
states_to_learn = [i for i in all_states if i not in guessed_states]
states_to_learn = pandas.DataFrame(states_to_learn)

states_to_learn.to_csv("statestolearn.csv")

