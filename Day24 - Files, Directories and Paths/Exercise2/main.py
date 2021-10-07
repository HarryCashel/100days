

# Use list comprehension to create a list of names from the text file
los = [name.strip() for name in open("./Input/Names/invited_names.txt")]

# Store the starting letter str in a variable
with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()

# loop through each name in list and replace placeholder with personal name
# write new file in /Output with name as file name
for name in los:
    file_with_name = content.replace("[name]", name)
    print(file_with_name)
    with open(f"./Output/ReadyToSend/LetterTo{name}", mode="w") as file:
        file.write(file_with_name)
