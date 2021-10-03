"""High Lower game
User is given two instagram accounts and must select the one with the higher following"""

from art import logo, vs
from data import data
import random

# Program greeting
print(logo)

# Set variable for our data to access and set score to 0
data = data
score = 0


def higher_following(c1, c2):
    """Function to compare the followings' key value of two dictionaries from our data set
    Returns True if c1 is larger int, False if c2 is larger int"""

    if c1['follower_count'] > c2['follower_count']:
        return True
    return False


def check_guess(c1, c2):
    """Function to compare user guess to both options\nUpdates count and returns True if user correct"""

    guess = input(f"{c1['name']} or {c2['name']}\nEnter '1' for {c1['name']}, '2' for {c2['name']}, or enter the "
                  f"name: ")

    if guess == '1' or guess == c1['name']:
        return higher_following(c1, c2)
    elif guess == '2' or guess == c2['name']:
        return higher_following(c2, c1)


# Select two random indices from our data list
random_choices = random.sample(data, 2)
choice_2 = random_choices[1]

# Set a boolean for our game loop
game_loop = True

while game_loop:

    # User is now comparing the second option with a new option
    # While loop to change if the options are the same

    choice_1 = choice_2
    choice_2 = random.choice(data)
    while choice_1['name'] == choice_2['name']:
        choice_2 = random.choice(data)

    # Display options to user
    print(f"""
    {choice_1['name']} is a {choice_1['description']} from {choice_1['country']}
    {vs}\n
    {choice_2['name']} is a {choice_2['description']} from {choice_2['country']}""")

    game_loop = check_guess(choice_1, choice_2)
    if game_loop:
        score += 1
        print(f"Your score is {score}")

print(f"GG. Your score was {score}")
