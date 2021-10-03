"""A virtual coffee machine"""

from data import *

# Get user to select coffee
print("What coffee would you like? 'cappuccino/latte/espresso?")
# coffee = input("Enter c/l/e or 1/2/3 or type the full name: ")


# Function to process coins and notes
def process_payment():
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

# Function to check if machine has enough resources for selected coffee
# for k, v in resource_costs['latte'].items():
#     if v < machine_resources[k]:
#         print(k)
#     elif v > machine_resources[k]:
#         print(f"Not enough {k}")

print(process_payment())
