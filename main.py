from flask import Flask, redirect, request, flash
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

application = Flask(__name__)
application.secret_key = "VerySecretSecretKey"

application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
application.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:8000/library"
db.init_app(application)

application.run()