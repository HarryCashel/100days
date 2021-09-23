"""Program that plays hangman with user"""

# imports
import random
from words import easy, medium, hard


# function to select difficulty
def select_difficulty():
    difficulty = input("Select difficulty = 'easy', 'medium' or 'hard': ")

    if difficulty.lower() == 'easy':
        word_list = easy
    elif difficulty.lower() == 'medium':
        word_list = medium
    elif difficulty.lower() == 'hard':
        word_list = hard
    return word_list


# function to continually run select difficulty until user correctly enters difficulty
def run_selection():

    try:
        return select_difficulty()
    except UnboundLocalError:
        print("Please enter 'easy', 'medium', or 'hard'.")
        run_selection()


answer = random.choice(run_selection())
print(answer)

guess = (input("Guess a letter! ")).lower()

if guess in answer:
    print("Yes")