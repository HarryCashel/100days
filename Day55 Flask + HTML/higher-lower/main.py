from flask import Flask
import random

app = Flask(__name__)

r_number = random.randint(1, 9)
print(r_number)

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


@app.route('/')
def hello_world():
    print(r_number)
    return '<h1 style="text-align: center">Hello, fuckers!</h1>' \
           '<p>Guess a number between 0 and 9</p>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"> '


@app.route("/bye")
@make_bold
def bye():
    return "Bye!"


@app.route("/<int:number>")
def greet(number):
    if number > r_number:
        return '<h1 style="color: red; text-align: center"> Too High!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < r_number:
        return '<h1 style="color: green; text-align: center"> Too Low!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"> '
    else:
        return '<h1 style="color: purple; text-align: center"> Just Right!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
