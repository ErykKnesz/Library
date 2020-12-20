# Library
Download as ZIP or by cloning the repository
# How to use

>pip install -r requirements.txt
>run library.py
>use forms to add new books, edit books, or delete a book by clicking on the "delete" button


# What is it made of?

The app uses Flask SQAlchemy as an ORM tool for governing sqlite queries. Data is stored in library.db. The authors included are just examples. You can add more authors to the form using your console: FLASK_APP=app flask shell will enable you to run commands in the terminal: e.g. book = Book.query.first(), book.authors.append(models.Author(name='name'))
