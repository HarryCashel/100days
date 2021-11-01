"""Program to calculate a persons BMI"""

# BMI = weight(kgs)/ height^2(m^2)

# Ask user to enter their height + weight, store these values in variables
user_height = input("Enter your height in m\t")
user_weight = input("Enter your weight in kgs\t")

# convert to data type int and calculate bmi
user_bmi = int(user_weight) // float(user_height) ** 2

print(int(user_bmi))
