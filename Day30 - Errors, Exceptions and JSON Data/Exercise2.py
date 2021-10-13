# IndexError handling

fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Regular fruit pie")
    else:
        print(f"{fruit} pie")


make_pie(7)
make_pie(1)
