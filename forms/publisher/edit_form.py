from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import IntegerField
from wtforms import DateField


class EditPublisher(FlaskForm):
    publisher_id = HiddenField("publisherID")
    publisher_name = StringField("name")
    publisher_address = StringField("address")
    publisher_amount_of_books = IntegerField("amountOfBooks")
    publisher_founder_date = DateField("founderDate")
