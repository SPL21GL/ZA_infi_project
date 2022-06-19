from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import IntegerField
from wtforms import DateField


class EditBook(FlaskForm):
    book_id = HiddenField("bookID")
    book_title = StringField("title")
    book_category = StringField("category")
    book_release_date = DateField("releaseDate")
    book_author_id = IntegerField("authorID")
