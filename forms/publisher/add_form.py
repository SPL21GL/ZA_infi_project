from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import IntegerField, DateField


class AddPublisher(FlaskForm):
    publisher_name = StringField("name")
    publisher_address = StringField("address")
    publisher_amount_of_books = IntegerField("amountOfBooks")
    publisher_founder_date = DateField("founderDate")
