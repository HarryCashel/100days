from flask import Flask, render_template
import random
import datetime, dateutil
app = Flask(__name__)
current_year = datetime.datetime.now().year

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", number=random_number, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
