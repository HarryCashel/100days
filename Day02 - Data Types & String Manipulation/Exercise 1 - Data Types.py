"""Program to add two digits of a number together"""

# Ask user for a two digit number
two_digit_number = input("Enter a two digit number: ")

# Assign each digit to a variable
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[-1])

# Add the two digits together and store in variable
answer = first_digit + second_digit

# Print answer
print(answer)
