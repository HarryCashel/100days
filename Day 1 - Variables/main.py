# 1. Create a greeting for the program
print("Welcome to the Band Name Generator")

# 2. Ask the user for the city they grew up in
city = input("What city did you grow up in?\n")

# 3. Ask the user for the name of a pet
pet = input("What is the name of a pet?\n")

# 4. Combine the name of their city and pet and show them their band name
band_name = f"{city}{pet}"
print(f"Your band name could be {band_name}.")
