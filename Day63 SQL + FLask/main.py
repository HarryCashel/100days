from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

all_books = []


class BookBuilder(FlaskForm):
    name = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookBuilder()
    if form.validate_on_submit():
        all_books.append({
            "title": form.name.data,
            "author": form.author.data,
            "rating": form.rating.data
        })
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

