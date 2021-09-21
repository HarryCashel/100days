"""Program to determine whether a given number is odd or even"""


# Function that returns True when parameter(number) is even and False when it is not.
def is_even(number):
    if number % 2 == 0:
        return True
    return False


# Ask user for a number
user_number = input("Give me a number and I will tell you if it is odd or even: ")
user_number = int(user_number)

if is_even(user_number):
    print("Your number is even")
else:
    print("Your number is odd")