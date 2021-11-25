from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)
db = SQLAlchemy(app)


# Create Table
class Movie(db.Model):
    """Models a book"""
    __table_args__ = (db.UniqueConstraint('title', 'year'),)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float(3), nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(125), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.drop_all()
# create database+table
db.create_all()


# drop database table


# create a new record
new_movie = Movie(
    title="Good Will Hunting",
    year=1997,
    description="Will Hunting (Matt Damon) has a genius-level IQ but chooses to work as a janitor at MIT. When he "
                "solves a difficult graduate-level math problem, his talents are discovered by Professor Gerald "
                "Lambeau (Stellan Skarsgard), who decides to help the misguided youth reach his potential.",
    rating=9,
    ranking=1,
    review="Good movie",
    img_url="https://cdn.shopify.com/s/files/1/0057/3728/3618/products/7ef5f3a2970c9eb8dba5bd10d294522c_21e9a29b-ad54"
            "-4578-9006-050039f589ce_480x.progressive.jpg?v=1573588853 "
)
db.session.add(new_movie)
db.session.commit()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)


if __name__ == '__main__':
    app.run(debug=True)
