# import sqlite3

# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1,'Harry Potter', 'J.K Rowling', '9.3')")
# db.commit()



from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

new_book = Book(id = 1, title='Harry Potter', author='J.K Rowling', rating=9.3)

db.session.add(new_book)
db.session.commit()


# ------------------TO CREATE A NEW RECORD WITH SQLALCHEMY----------------------- #
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# -------------------TO READ ALL RECORD WITH SQLALCHEMY ------------------------- #
# all_books = db.session.query(Book).all()

# -------------------TO READ ONE RECORDS WITH SQLALCHEMY ------------------------ #
# book = Book.query.filter_by(title='Harry Potter').first()

# -------------------TO UPDATE A RECORD BY QUERY WITH SQLALCHEMY ---------------- #
# book_to_update = Book.query.filter_by(title='Harry Potter').first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# -------------------TO UPDATE A RECORD BY PRIMARYKEY WITH SQLALCHEMY ----------- #
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "harry potter and the Goblet of Fire"
# db.session.commit()

# -------------------TO DELETE A RECORD BY QUERY WITH SQLALCHEMY ---------------- #
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()

##You can also delete by querying for a particular value e.g.
#  by title or one of the other properties. ##




