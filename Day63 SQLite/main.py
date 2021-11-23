from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()
# db.drop_all()
db.session.commit()
book_1 = Book(id=1, title="Harry Potter 1", author="JK. Rowling", rating=9.3)
book_2 = Book(id=2, title="Harry Potter 2", author="JK. Rowling", rating=9.5)
db.session.add(book_1)
db.session.add(book_2)
db.session.commit()



# import sqlite3
#
# # Create database file
# db = sqlite3.connect("books-collection.db")
#
# # Create a cursor object
# cursor = db.cursor()
#
# # Create a table called books with 4 fields
# # cursor.execute(
# #     "CREATE TABLE books (id INTEGER PRIMARY KEY, "
# #     "title varchar(250) NOT NULL UNIQUE, "
# #     "author varchar(250) NOT NULL, "
# #     "rating FLOAT NOT NULL)"
# # )
#
# # Add data to our database table books
# cursor.execute(
#     "INSERT INTO books VALUES("
#     "2, 'Harry Potter 2', 'J.K. Rowling', 9.3)"
# )
# db.commit()
