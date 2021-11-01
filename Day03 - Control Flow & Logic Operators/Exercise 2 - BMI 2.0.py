"""Upgraded version of our BMI calculator - Provide user with more information"""

"""Program to calculate a persons BMI"""

# BMI = weight(kgs)/ height^2(m^2)

# Ask user to enter their height + weight, store these values in variables
user_height = input("Enter your height in m\t")
user_weight = input("Enter your weight in kgs\t")

# convert to data type int and calculate bmi
user_bmi = int(user_weight) // float(user_height) ** 2

if user_bmi > 35:
    print(f"Your BMI is {user_bmi}, you are clinically obese.")
elif user_bmi > 30:
    print(f"Your BMI is {user_bmi}, you are  obese.")
elif user_bmi > 25:
    print(f"Your BMI is {user_bmi}, you are overweight.")
elif user_bmi > 18.5:
    print(f"Your BMI is {user_bmi}, you have a normal weight.")
elif user_bmi > 0:
    print(f"Your BMI is {user_bmi}, you are underweight.")
else:
    print("Off the charts?!")