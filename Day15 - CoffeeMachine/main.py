"""A virtual coffee machine"""

from data import *

# Get user to select coffee
print("What coffee would you like? 'cappuccino/latte/espresso?")
coffee = input("Enter c/l/e or 1/2/3 or type the full name: ")


def check_resources():
    """Function to check and print current resources in the machine"""
    print("Machine resources:")
    for k, v in machine_resources.items():
        if k == "milk" or k == "water":
            print(f"{k}: {v}ml")
        else:
            print(f"{k}: {v}g")


def refill_resources():
    """Function to refill the resources of the machine"""
    for k, v in machine_resources.items():
        if k == "milk" or k == "water":
            amount = int(input(f"How much would you like to fill {k} (ml): "))
        else:
            amount = int(input(f"How much would you like to fill {k} (g): "))

        machine_resources[k] += amount


def process_payment() -> float:
    """Function to process users coin deposit\nReturns total dollar amount as float"""
    dic_payments = {"20c": .2, "50c": .5, "$1": 1, "$2": 2,}
    total = 0
    # loop through list and take each denomination from user
    for k, v in dic_payments.items():
        try:
            num_of = int(input(f"Enter amount of {k} coins: "))
            total += dic_payments[k] * num_of

        except ValueError:
            print("Please enter digits.")
            try:
                num_of = int(input(f"Enter amount of {k} coins: "))
                total += dic_payments[k] * num_of
            except ValueError:
                break
    return total


def has_resources(coffee_selection):
    """Function to check if enough resources available in machine to make select coffee"""

    for k, v in resource_costs[coffee_selection].items():
        if v > machine_resources[k]:
            return False, f"Not enough {k}"
        elif v < machine_resources[k]:
            continue
    return True


def check_payment(coffee_selection, payment, ):
    """Function to check payment given is equal to or higher than the cost of the select coffee"""
    payment = payment
    global bank
    cost = money_cost[coffee_selection]

    if cost > payment:
        return f"A {coffee_selection} costs: ${cost}" \
               f" Refunding ${payment}"
    elif cost < payment:
        bank += cost
        return f"Making {coffee_selection}" \
               f" Refunding ${payment - cost}"

    elif money_cost[coffee_selection] == payment:
        bank += payment
        return f"Making {coffee_selection}"


