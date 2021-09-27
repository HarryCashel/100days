"""Program to mimic functionality of simple calculator"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculate():
    """User input to determine with calculation function to run"""

    # dictionary to hold the operation sign as key and related function as value
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,

    }

    n1 = int(input("First digit: "))
    n2 = int(input("Second digit: "))

    # My initial way of coding the logic to determine the operation

    # ask = input("Multiply/Divide/Add/Subtract?: ")

    # if "m".lower() in ask:
    #     return multiply(n1, n2)
    # elif "d".lower() in ask:
    #     return divide(n1, n2)
    # elif "dd".lower() in ask:
    #     return add(n1, n2)
    # elif "s".lower() in ask:
    #     return subtract(n1, n2)
    # else:
    #     return "Please enter a valid operation."

    # Using a dictionary to determine the operation function

    for key in operations.keys():
        print(key, end=" ")
    operation = input("\nWhat operation would you like to perform? ")
    return operations[operation](n1, n2)


def run():
    """To continually run function"""
    run_function = True
    while run_function:
        print(calculate())
        run_again = input("Do you want to run again?: y/n")
        if "n" in run_again:
            run_function = False


run()
