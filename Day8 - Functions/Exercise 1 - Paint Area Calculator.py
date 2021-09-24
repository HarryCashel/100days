"""Calculates area"""
import math

# One can of paint covers 5sqm

# Given random height and width of wall - calculate how many cans of paint are needed

# Using a lambda
# find_area_lambda = lambda x, y: x * y

def find_area(h: int, w: int) -> int:
    """Function that returns area of a square, given height and width as integers"""
    return h * w


# single line function definition
def find_area2(h: int, w: int) -> int: return h * w


height = int(input("Enter the height in m: "))
width = int(input("Enter the width in m: "))

area = find_area(height, width)

# Calculate how many cans are needed
cans_required = math.ceil(area / 5)

print(f"You need {cans_required} cans of paint to paint an area of {area}sqm")
