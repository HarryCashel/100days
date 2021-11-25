from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os
from wtforms.validators import DataRequired
import requests

API_KEY = os.environ["API_KEY"]
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


def search_movie(movie_name):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": API_KEY,
        "query": movie_name,
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    return response.json()['results']


def get_movie_data(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    paramas = {
        "api_key": API_KEY
    }
    response = requests.get(url=url, params=paramas)
    response.raise_for_status()
    return response.json()


# print(get_movie_data('603'))


# Create Table
class Movie(db.Model):
    """Models a book"""
    # __table_args__ = (db.UniqueConstraint('title', 'year'),)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float(3), nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(125), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

#
# db.drop_all()
# # create database+table
db.create_all()

# drop database table


# create a new record
# new_movie = Movie(
#     title="Good Will Hunting",
#     year=1997,
#     description="Will Hunting (Matt Damon) has a genius-level IQ but chooses to work as a janitor at MIT. When he "
#                 "solves a difficult graduate-level math problem, his talents are discovered by Professor Gerald "
#                 "Lambeau (Stellan Skarsgard), who decides to help the misguided youth reach his potential.",
#     rating=9,
#     ranking=1,
#     review="Good movie",
#     img_url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/7ef5f3a2970c9eb8dba5bd10d294522c_21e9a29b-ad54"
#             "-4578-9006-050039f589ce_480x.progressive.jpg?v=1573588853 "
# )
# db.session.add(new_movie)
# db.session.commit()


# Forms
class EditMovie(FlaskForm):
    new_rating = StringField("Your rating out of 10 e.g. 7.5")
    new_review = StringField("Your Review")
    submit = SubmitField("Done")


class AddMovie(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditMovie()
    movie_to_update = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = float(form.new_rating.data)
        movie_to_update.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie_to_update)


@app.route("/delete<int:movie_id>")
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_name = form.title.data
        data = search_movie(movie_name)
        return render_template('select.html', options=data)
    return render_template('add.html', form=form)


@app.route("/select<int:movie_id>", methods=["GET", "POST"])
def select(movie_id):
    form = EditMovie()
    movie_to_update = Movie.query.get(movie_id)
    if movie_id:
        data = get_movie_data(movie_id)
        new_movie = Movie(
            title=data["original_title"],
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            img_url=f"{MOVIE_DB_IMAGE_URL}/{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', movie_id=new_movie.id))


if __name__ == '__main__':
    app.run()
