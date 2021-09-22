"""Coin Toss Program"""
import random

# Greeting
print("Welcome to the Coin Flip!")


def cointoss():
    random_number = random.randint(0, 1)
    if random_number == 1:
        return "Heads"
    return "Tails"


run = True
while run:
    flip_again = input("Flip? Enter 'q' to quit.")
    if flip_again == "q":
        run = False
    else:
        print(cointoss())
