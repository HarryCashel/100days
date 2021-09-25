"""Secret Auction Program"""

from art import logo

# Greeting and logo

print(logo)
print("\nWelcome to the Secret Auction")


def user_name():
    """function that asks for name"""
    name = input("What is your name?: ")
    return name


def user_bid():
    """function that asks for user bid"""
    bid = int((input("What is your bid?: ")).replace("$", ""))
    return bid


def ask():
    """function that asks for another bidder"""
    question = input("Is there another bidder?: ")
    if question == 'yes' or "y" in question.lower():
        return True
    return False


# define empty dictionary
bidders = {}


def run():
    """function to run program and populate dictionary"""
    name = user_name()
    bid = user_bid()

    bidders[name] = bid


def largest_num(dic):
    """function to find largest integer value in dictionary and return the key, value pair"""
    num = 0
    name = ""
    for k, v in dic.items():
        if v > num:
            num = v
            name = k
    return name, num


# Set bool as conditional for while loop
run_program = True

# Loop to run until no bidders left
while run_program:
    run()
    run_program = ask()


winner = largest_num(bidders)
print(f"The winner is {winner[0]}")
