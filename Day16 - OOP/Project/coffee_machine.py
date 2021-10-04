from menu import Menu, MenuItem


class CoffeeMachine:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            'water': 500,
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
        for item in choice.ingredients:
            if choice.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
            return True

    def make_coffee(self, choice):
        """Deducts required resources for particular drink from machine"""
        try:
            for item in choice.ingredients:
                self.resources[item] -= choice.ingredients[item]
            return f"Here is your {choice.name}"
        except AttributeError:
            pass


cm = CoffeeMachine()
menu = Menu()

drink = menu.find_drink('latte')

print(cm.make_coffee(drink))
