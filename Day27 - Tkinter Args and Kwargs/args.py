"""Define functions with multiple arguments"""


def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(10, 10, 10, 10))
print(add(7, 3, 5, 5, 25))
