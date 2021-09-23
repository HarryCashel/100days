"""Program to calculate the average height from a list of heights"""

# Greeting

print("Welcome to the average height calculator")

add_height = True
total_height = []
while add_height:
    height = input("Enter a height or press Enter to continue\n")
    if height == "":
        add_height = False
    else:
        try:

            height = float(height)
            total_height.append(height)

        except ValueError:
            print("That is not a number!")


total_sum = 0
for i in total_height:
    total_sum += i

average_height = total_sum/len(total_height)
print(f"The average height is {round(average_height, 2)}m")