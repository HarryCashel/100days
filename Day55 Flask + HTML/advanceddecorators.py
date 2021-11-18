def logging_decorator(function):
    def wrapper(*args):
        return f"You called {function.__name__}{args}\n" \
               f"It returned {function(*args)}"

    return wrapper


@logging_decorator
def a_function(x, y, z):
    return x + y + z


print(a_function(1, 2, 3))
