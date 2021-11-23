from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
Bootstrap(app)


class Book(db.Model):
    """Models a Book"""
    id = db.Column(db.Integer, primary_key=True)  # primary key
    title = db.Column(db.String(250), unique=True,
                      nullable=False)  # A table row that cannot be empty and must be unique
    author = db.Column(db.String(250), nullable=False)  # A table row that cannot be empty
    rating = db.Column(db.Float, nullable=False)  # A table row that cannot be empty


# db.drop_all()
db.create_all()


class BookBuilder(FlaskForm):
    name = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField("Submit")


class EditRating(FlaskForm):
    new_rating = StringField("New Rating", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookBuilder()
    if request.method == "POST":
        new_book = Book(
            title=form.name.data,
            author=form.author.data,
            rating=form.rating.data
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/edit<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    edit_form = EditRating()
    book_to_update = Book.query.get(book_id)
    if request.method == "POST":
        book_to_update.rating = edit_form.new_rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=edit_form, current_book=book_to_update)


@app.route("/delete<int:book_id>")
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
