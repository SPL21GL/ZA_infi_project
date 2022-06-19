from flask import Flask, render_template
from model.models import db

from flask_wtf.csrf import CSRFProtect
from controllers.index import index_blueprint
from controllers.books import books_blueprint
from controllers.authors import authors_blueprint
from controllers.publishers import publishers_blueprint

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:8000/library"

csrf = CSRFProtect(app)

db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(index_blueprint)
app.register_blueprint(books_blueprint)
app.register_blueprint(authors_blueprint)
app.register_blueprint(publishers_blueprint)


app.run(debug=True)
