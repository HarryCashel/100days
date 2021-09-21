"""Program that works out whether a given year is a leap year"""


# Ask user for any year
year = input("What year are we checking? ")

# Make sure our variable is of integer type
year = int(year)

# Set a Boolean for conditional checking
is_leap = False

# Check if year is a leap year
if year % 400 == 0 and year % 100 == 0:
    is_leap = True

# Check if year is leap year
elif year % 4 == 0:
    is_leap = True
    # Condition to check if not leap year
    if year % 100 == 0:
        is_leap = False


"""Another way to frame this code"""
is_leap = False

if year % 4 == 0:
    is_leap = True
    if year % 100 == 0:
        is_leap = False
        if year % 400 == 0:
            is_leap = True
print(is_leap)
