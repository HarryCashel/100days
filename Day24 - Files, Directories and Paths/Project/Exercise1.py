# file = open("my_file.txt")
# content = file.read()
#
# print(content)
#
# file.close()


# Same functionality but will automatically close (Y)
# Mode is defaulted to read- only
with open("my_file.txt") as file:
    content = file.read()
    print(content)

# Write - will write over the entire content of file
with open("my_file.txt", mode="w") as file:
    file.write("Cool")

# Append - will add to the end of the file
with open("my_file.txt", mode="a") as file:
    file.write("Cool")

# You can create a non-existing new file by using write and a new file name
with open("my_new_file.txt", mode="w") as file:
    file.write("CoolBeans")

