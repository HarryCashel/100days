"""Calculates area"""

# One can of paint covers 5sqm

# Given random height and width of wall - calculate how many cans of paint are needed


def find_area(h: int, w: int) -> int:
    """Function that returns area of a square, given height and width as integers"""
    return h * w


find_area()

# Using a lambda
find_area_lambda = lambda x, y: x * y

