"""Program to calculate the highest number"""

# Greeting
print("Welcome to the highest number!\n")

# program as a function

high_number = 0


def highest_number(list_of_numbers):
    global high_number
    high_number = high_number
    for i in list_of_numbers.split(","):
        try:
            if int(i) > high_number:
                high_number = int(i)
        except ValueError:
            exit("You entered an invalid character")
    return high_number


print(f"The highest number is: {highest_number(input('Enter a list of numbers, separated by commas.'))}")
