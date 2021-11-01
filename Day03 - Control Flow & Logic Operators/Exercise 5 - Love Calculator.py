"""Program that calculates the compatibility between two people - very scientific"""

# Program greeting
print("Welcome to the Love Calculator!!")

# Ask user for two names - stores these in variables

name1 = input("First name: ")
name2 = input("Second name: ")

# Concatenate the names
full_name = name1 + name2


# function that counts occurrences of letters in two words
def letter_checker(name, word):
    count = 0
    # Loops through first parameter (name) and checks if each index is in the second parameter (word)
    for i in name.lower():
        if i in word.lower():
            # Will count for each matching occurrence
            count += 1
    return count


# run the names through our function to get a digit for each name
first_digit = letter_checker(full_name, "TRUE")
second_digit = letter_checker(full_name, "LOVE")

# concatenate the digits
score = str(first_digit) + str(second_digit)

# Conditional statements to check what range the final score lands in
# Prints appropriate statement
if 10 > int(score) or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 50 > int(score) > 40:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
