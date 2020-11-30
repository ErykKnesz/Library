from datetime import datetime
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    author = db.relationship("Author", backref="book", lazy="dynamic")
    availability = db.relationship(
        "Availability",
        uselist=False,
        back_populates="Book")
    
    def __str__(self):
        return f"<User {self.username}>"


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Author {self.id} ...>"


class Availability(db.Model):
    available = db.Boolean
    #lent_date = db.Column(db.DateTime, index=True, default=datetime.utcnow) może dorobić jak zostanie czas
    #return_date = db.Column(db.DateTime, index=True) 
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    availability = db.relationship(
        "Book",
        uselist=False,
        back_populates="Availability")
    
    def __str__(self):
        return f"<Available {self.available} ...>"
    
