from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import DateField


class AddAuthor(FlaskForm):
    author_email = StringField("email")
    author_address = StringField("address")
    author_birthday = DateField("birthday")
    author_mobile_number = StringField("mobileNumber")
