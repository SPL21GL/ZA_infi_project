from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.fields.simple import StringField, HiddenField


class EditAuthor(FlaskForm):
    author_id = HiddenField("authorID")
    author_email = StringField("email")
    author_address = StringField("address")
    author_birthday = DateField("birthday")
    author_mobile_number = StringField("mobileNumber")
