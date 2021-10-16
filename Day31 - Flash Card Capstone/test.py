try:
    with open("./data/score.txt", mode="r") as file:
        content = file.read()
        content = int(content)
except FileNotFoundError:
    with open("./data/score.txt", mode="w") as file:
        file.write("0")
        content = 0


def add(num1, num2):
    return num1 + num2

add(1, 5)