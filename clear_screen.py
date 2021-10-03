import os


# The screen clear function
def screen_clear():
    # for mac and linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platform
        _ = os.system('cls')