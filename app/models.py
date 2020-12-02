from datetime import datetime
from app import db, app


association_table = db.Table('association',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    authors = db.relationship("Author", lazy='subquery', secondary=association_table,
                               backref=db.backref('books', lazy=True))
    borrowed = db.Column(db.Boolean)

    def __str__(self):
        return f"<User {self.title}>"


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)

    def __str__(self):
        return f"<Author {self.name} ...>"

    
