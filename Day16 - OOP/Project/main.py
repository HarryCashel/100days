from payment import Payment
from coffee_machine import CoffeeMachine
from menu import Menu

coffee_machine = CoffeeMachine()
menu = Menu()
payment = Payment()

is_on = True

while is_on:
    options = menu.get_items()
    print("Secret menu: 'close', 'check', 'fill'")
    drink = input(f"What would you like to order? {options}\n")
    if drink == "1":
        drink = "latte"
    elif drink == "2":
        drink = "cappuccino"
    elif drink == "3":
        drink = "espresso"

    if drink == "close":
        is_on = False
    elif drink == "check":
        coffee_machine.report()
        payment.report()
    elif drink == "fill":
        coffee_machine.fill_machine()
    else:
        drink = menu.find_drink(drink)
        can_make = coffee_machine.check_resources(drink)
        if can_make:
            is_payment = payment.make_payment(drink.cost)

        if can_make and is_payment:
            coffee_machine.make_coffee(drink)



