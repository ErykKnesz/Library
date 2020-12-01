from datetime import datetime
from app import db, app

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    author = db.relationship("Author", backref="book", lazy="dynamic")
    borrowed = db.relationship(
        "Borrowed",
        uselist=False,
        back_populates="book")
    
    def __str__(self):
        return f"<User {self.username}>"


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Author {self.id} ...>"


class Borrowed(db.Model):
    __tablename__ = 'borrowed'
    available = db.Column(db.Boolean, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    borrowed = db.relationship(
        "Book",
        back_populates="borrowed")
    
    def __str__(self):
        return f"<Available {self.available} ...>"
    
