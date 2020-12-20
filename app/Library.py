from app import models, db


def remove_csrf(data):
    if 'csrf_token' in data:
        data.pop('csrf_token')
    return data


class Library:
    def __init__(self):
        books = models.Book.query.all()
        self.books = books
 
    def add_book(self, data):
        if 'csrf_token' in data:
            data.pop('csrf_token')
        new_book = models.Book(title=data['title'], borrowed=data['available'])
        for author in data['author']:
            new_book.authors.append(models.Author(name=author))
        db.session.add(new_book)
        db.session.commit()

    def get(self, id):
        book = models.Book.query.get(id)
        return book

    def change(self, id, data):
        if 'csrf_token' in data:
            data.pop('csrf_token')
        book = models.Book.query.get(id)
        book.title = data['title']
        book.borrowed = data['available']
        book.authors.clear()
        for author in data['author']:
            book.authors.append(models.Author(name=author))
        db.session.add(book)
        db.session.commit()
    
    def delete(self, id):
        book = models.Book.query.get(id)
        db.session.delete(book)
        db.session.commit()


books = Library()

