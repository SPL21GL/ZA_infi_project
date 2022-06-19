import sqlalchemy
from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect
from forms.book.add_form import AddBook
from forms.book.delete_form import DeleteBook
from forms.book.edit_form import EditBook
from model.models import db, Book

books_blueprint = Blueprint('books_blueprint', __name__)


@books_blueprint.route("/books", methods=["get", "post"])
def books():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    page = request.args.get('page', 1, type=int)
    book_list = session.query(Book).order_by(Book.bookID).paginate(
        page, 10, error_out=False)

    return render_template("/books/book.html", books=book_list)


@books_blueprint.route("/books/add_book", methods=["get", "post"])
def add_book():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_book_form = AddBook()

    if request.method == 'POST':
        if add_book_form.validate_on_submit():
            new_book = Book()

            new_book.title = add_book_form.book_title.data
            new_book.category = add_book_form.book_category.data
            new_book.releaseDate = add_book_form.book_release_date.data
            new_book.authorID = add_book_form.book_author_id.data

            try:
                db.session.add(new_book)
                db.session.commit()
            except:
                flash("An Exception is raised")
                add_book_form = AddBook()
                return render_template("/books/add_book.html", form=add_book_form)

            return redirect("/books")
        else:
            return render_template("books/add_book.html", form=add_book_form)
    else:
        return render_template("books/add_book.html", form=add_book_form)


@books_blueprint.route("/books/edit_book", methods=["get", "post"])
def edit_book():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_book_form = EditBook()

    book_id = request.args["bookID"]

    book_to_edit = session.query(Book).filter(
        Book.bookID == book_id).first()

    if request.method == "POST":
        if edit_book_form.validate_on_submit():
            book_id = edit_book_form.book_id.data
            book_to_edit = db.session.query(Book).filter(
                Book.bookID == book_id).first()

            book_to_edit.title = edit_book_form.book_title.data
            book_to_edit.category = edit_book_form.book_category.data
            book_to_edit.releaseDate = edit_book_form.book_release_date.data
            book_to_edit.authorID = edit_book_form.book_author_id.data

            db.session.commit()
        return redirect("/books")
    else:
        edit_book_form.book_id.data = book_to_edit.bookID
        edit_book_form.book_title.data = book_to_edit.title
        edit_book_form.book_category.data = book_to_edit.category
        edit_book_form.book_release_date.data = book_to_edit.releaseDate
        edit_book_form.book_author_id.data = book_to_edit.authorID

        return render_template("books/edit_book.html", form=edit_book_form)


@books_blueprint.route("/books/delete_book", methods=["get", "post"])
def delete_book():
    delete_book_form = DeleteBook()
    if delete_book_form.validate_on_submit():
        book_id = delete_book_form.bookID.data
        book_to_delete = db.session.query(Book).filter(
            Book.bookID == book_id)
        book_to_delete.delete()
        db.session.commit()
    return redirect("/books")
