from flask_wtf import FlaskForm
from wtforms.fields import IntegerField


class DeleteBook(FlaskForm):
    bookID = IntegerField("bookID")
