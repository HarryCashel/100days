from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Create a New Database
app = Flask(__name__)  # create flask application/object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # link database
db = SQLAlchemy(app)  # assign data of SQLAlchemy to Flask app


# Create a New Table
class Book(db.Model):  # create Table Object
    """Models a Book"""
    id = db.Column(db.Integer, primary_key=True)  # primary key
    title = db.Column(db.String(250), unique=True,
                      nullable=False)  # A table row that cannot be empty and must be unique
    author = db.Column(db.String(250), nullable=False)  # A table row that cannot be empty
    rating = db.Column(db.Float, nullable=False)  # A table row that cannot be empty


# Create table
db.create_all()


# CRUD - Create Read Update Delete

# Create a New Record
def create_book():
    new_book = Book(title="Harry Potter 2", author="J. K. Rowling", rating=9.1)
    db.session.add(new_book)
    db.session.commit()


create_book()
# Read All Records
all_books = db.session.query(Book).all
# Read a Particular Record By Query
book = Book.query.filter_by(title="Harry Potter 1").first()

# Update A Particular Record By Query
book_to_update = Book.query.filter_by(title="Harry Potter 1").first()
book_to_update.title = "Harry Potter and the Philosopher's Stone"
db.session.commit()

# Update A Record By Primary Key
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()

# Delete A Record By Primary Key
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()

create_book()
# Delete A Record By Query
book_to_delete = Book.query.filter_by(title="Harry Potter 1").first()
