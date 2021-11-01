"""Program to determine who pays the bill"""
import random
# Greeting
print("Welcome to Banker Roulette.\nLet's find out who is paying today!")

list_of_names = []
number_of_people = int(input("How many people ate today?\n"))

while len(list_of_names) < number_of_people:
    name = input("Who ate today?\n")
    list_of_names.append(name)

random.shuffle(list_of_names)
print(f"{list_of_names.pop()} is paying!")
