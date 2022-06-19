from flask_wtf import FlaskForm
from wtforms.fields import IntegerField


class DeleteAuthor(FlaskForm):
    authorID = IntegerField("authorID")
