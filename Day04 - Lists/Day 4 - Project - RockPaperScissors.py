"""Program to play SPR against computer"""
import copy
import random
# Greeting
print("Welcome to the Scissor Paper Rock game!!")

computer_choices = ["Rock", "Paper", "Scissors"]
player_choices = copy.copy(computer_choices)

# computer_choice = random.choice(computer_choices)
#
# player_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors?\n"))
#
# print(f"Computer throws {computer_choice}")
# print(f"Player throws {player_choices[player_choice]}")
# if player_choice == 0:
#     if computer_choice == "Rock":
#         print("Tie")
#     elif computer_choice == "Paper":
#         print("Computer wins")
#     elif computer_choice == "Scissors":
#         print("Player wins")
#
# elif player_choice == 1:
#     if computer_choice == "Rock":
#         print("Player wins")
#     elif computer_choice == "Paper":
#         print("Tie")
#     elif computer_choice == "Scissors":
#         print("Computer wins")
#
# elif player_choice == 2:
#     if computer_choice == "Rock":
#         print("Computer wins")
#     elif computer_choice == "Paper":
#         print("Player wins")
#     elif computer_choice == "Scissors":
#         print("Tie")


# A more efficent way to achieve this is using the indices in the lists

computer_choice = random.randint(0, 2)
player_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors?\n"))

if player_choice == 0 and computer_choice == 2:
    print("Player wins")
elif player_choice > computer_choice:
    print("Player wins")
elif player_choice < computer_choice:
    print("Computer wins")
elif player_choice == computer_choice:
    print("Tie")
else:
    print("Invalid number. You lose!")

print(f"Computer threw {computer_choices[computer_choice]}")
print(f"User threw {player_choices[player_choice]}")