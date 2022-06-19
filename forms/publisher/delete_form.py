from flask_wtf import FlaskForm
from wtforms.fields import IntegerField


class DeletePublisher(FlaskForm):
    publisherID = IntegerField("publisherID")
