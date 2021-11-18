from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, fuckers!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media1.giphy.com/media/3o6Mbnle3md0HeKj4I/200.webp?cid' \
           '=ecf05e47rokns28n07dmgptq74rm7p5ihrlbgrj5eztfuu9t&rid=200.webp&ct=g"> '



@app.route("/bye")
@make_bold
def bye():
    return "Bye!"


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
