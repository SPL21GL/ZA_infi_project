from flask import Flask, render_template, request
from werkzeug.utils import redirect

from controllers.index import index_blueprint
from model.models import db, Book, Author, Publisher, Authorgroup, Version

# from flask_wtf.csrf import CSRFProtect

application = Flask(__name__)
application.secret_key = "VerySecretSecretKey"

application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
application.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:8000/library"
db.init_app(application)

application.register_blueprint(index_blueprint)


@application.route('/view/books', methods=['GET', 'POST'])
def load_books():
    page = request.args.get('page', 1, type=int)
    items = Book.query.paginate(page=page, per_page=10)
    return render_template("view/books.html",
                           title="Bibliothek ~ books",
                           items=items)


@application.route('/view/authors', methods=['GET', 'POST'])
def load_authors():
    authors = db.session.query(Author).all()
    return render_template("view/authors.html",
                           title="Bibliothek ~ authors",
                           items=authors)


@application.route('/view/publishers', methods=['GET', 'POST'])
def load_publishers():
    publishers = db.session.query(Publisher).all()
    return render_template("view/publishers.html",
                           title="Bibliothek ~ publishers",
                           items=publishers)


@application.route('/add/book', methods=['GET', 'POST'])
def add_book():
    print("here")
    return render_template("add/book.html",
                           title="Bibliothek ~ books")


@application.route('/view/authorgroups', methods=['GET', 'POST'])
def load_authorgroups():
    page = request.args.get('page', 1, type=int)
    items = Authorgroup.query.paginate(page=page, per_page=10)
    return render_template("view/authorgroups.html",
                           title="Bibliothek ~ authorgroups",
                           items=items)


@application.route('/view/versions', methods=['GET', 'POST'])
def load_versions():
    versions = db.session.query(Version).all()
    return render_template("view/versions.html",
                           title="Bibliothek ~ authorgroups",
                           items=versions)


@application.route('/view', methods=['GET', 'POST'])
def edit_mode():
    print("none")
    return redirect("/")


application.run(debug=True)
