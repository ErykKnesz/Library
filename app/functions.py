from app import db
from models import Book

class Library:
    def __init__(self):
        books = models.Book.query.all()
        self.books = books
    
    def add_book(self, data):
        if 'csrf_token' in data:
            data.pop('csrf_token')
        new_book = Book(title=data['title'], borrowed=data['available'])
        new_book = Book.append(Author(name=data['author']))
        db.session.add(new_book)
        db.session.commit()

books = Library()