from flask import Flask, render_template, request
from werkzeug.utils import redirect

from controllers.index import index_blueprint
from model.models import db, Book, Author, Publisher
# from flask_wtf.csrf import CSRFProtect

application = Flask(__name__)
application.secret_key = "VerySecretSecretKey"

application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
application.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:8000/library"
db.init_app(application)

application.register_blueprint(index_blueprint)


@application.route('/books', methods=['GET', 'POST'])
def load_books():
    books = db.session.query(Book).all()
    print(books)
    return render_template("books.html",
                           title="Bibliothek ~ books",
                           items=books)

@application.route('/authors', methods=['GET', 'POST'])
def load_authors():
    authors = db.session.query(Author).all()
    return render_template("author.html",
                           title="Bibliothek ~ authors",
                           items=authors)

@application.route('/publishers', methods=['GET', 'POST'])
def load_publishers():
    publishers = db.session.query(Publisher).all()
    return render_template("publishers.html",
                           title="Bibliothek ~ publishers",
                           items=publishers)

@application.route('/data', methods=['GET', 'POST'])
def edit_mode():
    print("none")
    return redirect("/")


application.run(debug=True)
