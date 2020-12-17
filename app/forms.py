from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from app import models

authors = models.Author.query.all()
class BooksForm(FlaskForm):
    title = StringField('book', validators=[DataRequired()])
    author = SelectMultipleField(
        'author',
        choices=[(author.name, author.name) for author in authors])
    available = BooleanField('available')
