"""Password Generator App"""
import random
import string

# Create strings of our usable ASCII characters
characters = string.printable[:-2]
numbers = characters[:10]
letters = characters[10:62]
symbols = characters[-36:-4]

# Greeting - print to user
print("Welcome to the PyPassword Generator!\n")

# Ask user how many letters
# num_of_letters = int(input("How many letters? "))
# num_of_letters = random.choices(letters, k=num_of_letters)
#
# # Ask user how many symbols
# num_of_symbols = int(input("How many symbols? "))
# num_of_symbols = random.choices(symbols, k=num_of_symbols)
#
# # Ask user how many numbers
# num_of_nums = int(input("How many numbers? "))
# num_of_nums = random.choices(numbers, k=num_of_nums)
#
#
# password = (num_of_letters + num_of_symbols + num_of_nums)
# random.shuffle(password)
# new_password = "".join(password)
# print(new_password)

# My preferred generator

# length_of_password = int(input("How long should the password be? "))
password = letters + numbers + symbols
password = random.choices(password, k=10)
random.shuffle(password)
new_password = "".join(password)
print(new_password)
