"""Program to build a Pizza"""

# Set initial price of pizza to 0
price = 0
# Program greeting
print("Welcome to Python Pizza!")

# Get the size form user
size = input("What size pizza do you want? s/m/l\n")

# Ask the user if they would like pepperoni
add_pepperoni = input("Would you like pepperoni?\n")

# Ask the user if they would like cheese
add_cheese = input("Would you like cheese?\n")


# Conditionals to check what size of pizza the user would like and adjust the price as such
if "s" in size.lower():
    price += 15
elif "med" in size.lower() or size.lower() == "m":
    price += 20
elif "la" in size.lower() or size.lower() == "l":
    price += 25
else:
    print("Please enter s/m/l")

# Check whether user would like pepperoni and cheese, and adjust the price as such

if "y" in add_pepperoni.lower():
    if "s" in size.lower():
        price += 2
    else:
        price += 3

if "y" in add_cheese.lower():
    price += 1

print(price)