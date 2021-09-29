"""Number Guessing Game"""

import random


answer = random.randint(1, 100)


def welcome():
    """Function that returns difficulty"""

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # print(f"Hint: {answer}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return difficulty


def check_guess(n1, n2):
    """Takes guess and answer as inputs. Returns True or a str telling user too high or too low"""

    if n1 == n2:
        return True
    elif n1 > n2:
        return False
    elif n1 < n2:
        return False


def first_guess():
    """The first guess"""

    try:
        initial_guess = int(input("Guess a number: "))
    except ValueError:
        print("Please enter an integer.")
        initial_guess = first_guess()
    return initial_guess


def game():
    """Runs the game"""
    difficulty = welcome()

    if difficulty == 'hard':
        lives = 5
    elif difficulty == 'easy':
        lives = 10
    else:
        lives = 5

    print(f"You have {lives} guesses remaining.")
    initial_guess = first_guess()

    if check_guess(initial_guess, answer):
        return f"Correct. The correct answer was {answer}"
    else:
        lives -= 1
        if initial_guess > answer:
            print("Too High")
        else:
            print("Too Low")
    while lives != 0:
        print(f"You have {lives} guesses remaining.")
        try:
            guess = int(input("Guess again: "))
        except ValueError:
            print("Please enter an integer.")
            continue

        if check_guess(guess, answer):
            return f"Correct. The correct answer was {answer}"
        elif not check_guess(guess, answer):
            lives -= 1
            if guess > answer:
                print("Too High")
            else:
                print("Too Low")
    return f"The answer was {answer}"


print(game())
