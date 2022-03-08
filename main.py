from flask import Flask
from controllers.index import index_blueprint
from model.models import db

application = Flask(__name__)
application.secret_key = "VerySecretSecretKey"

application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
application.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:8000/library"
db.init_app(application)


application.register_blueprint(index_blueprint)

application.run()
