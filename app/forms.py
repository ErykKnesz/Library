from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField
from wtforms.validators import DataRequired


class BooksForm(FlaskForm):
    title = StringField('book', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    available = BooleanField('available', validators=[DataRequired()])
