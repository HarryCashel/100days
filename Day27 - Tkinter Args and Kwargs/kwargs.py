"""Multiple Keyword arguments"""


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(5, add=5, multiply=5)


class Car:
    # Using dictionary method .get() will avoid KeyError when keys are not initialised -> returns None
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")

my_car.model = "Skyline"

print(my_car.model)
