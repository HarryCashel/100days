# # FileNotFound
#
# try:
#     file = open("some.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["a kk"])
# except FileNotFoundError:
#     file = open("some.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("No person is over 3 meters.")

bmi = weight / weight ** 2
print(bmi)