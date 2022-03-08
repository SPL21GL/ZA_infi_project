# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Authorgroup(db.Model):
    __tablename__ = 'authorgroups'

    groupID = db.Column(db.Integer, primary_key=True, unique=True)
    authorID = db.Column(db.Integer)
    bookID = db.Column(db.Integer)


class Author(db.Model):
    __tablename__ = 'authors'

    authorID = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(64))
    address = db.Column(db.String(128))
    birthday = db.Column(db.Date)
    mobileNumber = db.Column(db.Integer)


class Book(db.Model):
    __tablename__ = 'books'

    bookID = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(64))
    category = db.Column(db.String(64))
    releaseDate = db.Column(db.Date)
    authorID = db.Column(db.Integer)


class Publisher(db.Model):
    __tablename__ = 'publishers'

    publisherID = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(128))
    amountOfBooks = db.Column(db.Integer)
    founderDate = db.Column(db.Date)


class Version(db.Model):
    __tablename__ = 'versions'

    versionID = db.Column(db.Integer, primary_key=True, unique=True)
    publisherID = db.Column(db.Integer)
    bookID = db.Column(db.Integer)
