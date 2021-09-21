"""This program is a tip calculator"""

# Greeting for user
print("Welcome to the tipping calculator!")

# Ask user for total bill
initial_bill = input("Enter the bill in dollars and cents: ")
initial_bill = float(initial_bill)

# Ask user for the percentage tip
tip_percent = input("How much would you like to tip? (eg, 10 for 10%)\n")
tip_percent = (int(tip_percent) / 100)

# Ask how many people will be splitting the bill
number_to_split = input("How many people are splitting the bill?\n")
number_to_split = int(number_to_split)

# Calculate the tip
total_tip = initial_bill * tip_percent
total_tip_per_person = total_tip / number_to_split
total_bill = initial_bill + total_tip
price_per_person = initial_bill / number_to_split + total_tip_per_person
# Show user the bill, the tip, the tip per person and the bill with tip totals

data = f"The bill is: {initial_bill}\n" \
       f"The tip is: {total_tip}\n" \
       f"The tip per-person is: {total_tip_per_person}\n" \
       f"The total bill including tip is: {total_bill}\n" \
       f"The total price per person is: {price_per_person} (Bill:{initial_bill/number_to_split}  Tip:{total_tip_per_person}"
print(data)
