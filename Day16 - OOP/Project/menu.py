class MenuItem:
    """Models individual menu items"""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    """Models the Menu with drink items"""
    def __init__(self):
        self.menu = [
            MenuItem(name='latte', water=200, milk=150, coffee=20, cost=2.5),
            MenuItem(name='cappuccino', water=250, milk=100, coffee=20, cost=3.5),
            MenuItem(name='espresso', water=100, milk=0, coffee=20, cost=2),
        ]

    def get_items(self):
        """Searches the menu and returns the names of available drinks"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, choice):
        """Searches for exact menu item by name.
        Returns that item if exists in menu, otherwise returns None"""
        for item in self.menu:
            if item.name == choice:
                return item

