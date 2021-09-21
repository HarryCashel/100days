"""Create a program that tells the user how many days, weeks and months they have left
to live, assuming they live to 90."""

# Set variables for the time remaining
total_months = 12 * 90
total_days = 365 * 90
total_weeks = 52 * 90

# Ask user for their age
user_age = input("What is your current age?\n")
user_age_as_int = int(user_age)
# Convert age to months/weeks/days

months_remaining = total_months - user_age_as_int * 12
days_remaining = total_days - user_age_as_int * 365
weeks_remaining = total_weeks - user_age_as_int * 52

print(f"Your have {days_remaining} days or, {weeks_remaining} weeks or, {months_remaining} months left.")
