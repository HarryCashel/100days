from flask import Flask, render_template
import requests

app = Flask(__name__)


class GuessAge:
    def __init__(self, name):
        self.url = "https://api.agify.io"
        self.name = {"name": name}

    def make_request(self):
        request = requests.get(self.url, params=self.name)
        response = request.json()
        return response


class GuessGender:
    def __init__(self, name):
        self.url = "https://api.genderize.io"
        self.name = {"name": name}

    def make_request(self):
        request = requests.get(self.url, params=self.name)
        response = request.json()
        return response


def bold_decorator(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


@app.route('/')
def home():
    return render_template("index.html")


# Old style
# @bold_decorator
# @app.route("/guess/<name>")
# def guess(name):
#     age = GuessAge(name)
#     current_age = age.make_request()['age']
#     gender = GuessGender(name)
#     current_gender = gender.make_request()['gender']
#     return f"Hey {name},\n" \
#            f"I think you are {current_gender},\n" \
#            f"And maybe {current_age} years old."

# render the python with jinja markup
@app.route("/guess/<name>")
def guess(name):
    age = GuessAge(name)
    age = age.make_request()['age']
    gender = GuessGender(name)
    gender = gender.make_request()['gender']
    return render_template("guess.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
