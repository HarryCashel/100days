"""Program to mimic functionality of simple calculator"""

from art import logo
import os


def cls():
    os.system('clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculate(n1, n2):
    """User input to determine with calculation function to run"""

    # dictionary to hold the operation sign as key and related function as value
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,

    }
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
    print(logo)
    run_function = True
    n1 = float(input("First digit: "))
    n2 = float(input("Second digit: "))
    answer = calculate(n1, n2)
    print(answer)
    while run_function:
        run_again = input("Do you want to run again?: y/n")
        if "n" in run_again:
            run_function = False
        restart = input("Do you want to restart or continue?('r' or 'c': ")
        if "r".lower() in restart:
            cls()
            run()
        elif "c".lower() in restart:
            cls()
            n3 = float(input("Next digit: "))
            new_answer = calculate(answer, n3)
            print(new_answer)


run()
