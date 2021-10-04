from menu import Menu, MenuItem


class CoffeeMachine:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            'water': 0,
            'milk': 500,
            'coffee': 240,
        }

    def report(self):
        """Reports available resources to user"""
        for item, amount in self.resources.items():
            if item == 'water' or item == 'milk':
                print(f"{item}: {amount}ml")
            else:
                print(f"{item}: {amount}g")

    def check_resources(self, choice):
        """Returns True when resources in machine are greater than
        required resources for drink. Returns False if resources are insufficient"""
        try:
            for item in choice.ingredients:
                if choice.ingredients[item] > self.resources[item]:
                    print(f"Sorry there is not enough {item}.")
                    return False
                return True
        except AttributeError:
            print("This item is not available")

    def make_coffee(self, choice):
        """Deducts required resources for particular drink from machine"""
        try:
            for item in choice.ingredients:
                self.resources[item] -= choice.ingredients[item]
            return f"Here is your {choice.name}"
        except AttributeError:
            pass

    def fill_machine(self):
        for item in self.resources:
            try:
                self.resources[item] += int(input(f"How much would you like to fill {item}? "))
            except ValueError:
                print("Please enter integer")