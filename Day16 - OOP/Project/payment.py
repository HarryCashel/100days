class Payment:
    """Models the payment system of coffee machine"""
    CURRENCY = "$"

    COIN_NOTE_VALUE = {
        "20c": .2,
        "50c": .5,
        "1": 1,
        "2": 2,
        "5": 5

    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Reports session profit"""
        print(f"Current profit: {self.CURRENCY}{self.profit}")

    def process(self):
        """Returns the total entered money"""
        print("Please enter amount of coins/notes")
        for item in self.COIN_NOTE_VALUE:
            self.money_received += int(input(f"{item}: ")) * self.COIN_NOTE_VALUE[item]
        return self.money_received

    def make_payment(self, cost):
        """Adds cost of drink to profit and returns change
        Returns True if payment successful, False if not"""
        self.process()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is your change: {self.CURRENCY}{change}")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print(f"Sorry that is not enough money. Refunding {self.money_received}")
            self.money_received = 0
            return False
