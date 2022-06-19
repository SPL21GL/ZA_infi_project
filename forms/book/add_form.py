from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import IntegerField, DateField


class AddBook(FlaskForm):
    book_title = StringField("title")
    book_category = StringField("category")
    book_release_date = DateField("releaseDate")
    book_author_id = IntegerField("authorID")
