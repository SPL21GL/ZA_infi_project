import sqlalchemy
from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect
from forms.author.add_form import AddAuthor
from forms.author.delete_form import DeleteAuthor
from forms.author.edit_form import EditAuthor
from model.models import db, Author

authors_blueprint = Blueprint('authors_blueprint', __name__)


@authors_blueprint.route("/authors", methods=["get", "post"])
def authors():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    page = request.args.get('page', 1, type=int)
    author_list = session.query(Author).order_by(Author.authorID).paginate(
        page, 10, error_out=False)

    return render_template("/authors/author.html", authors=author_list)


@authors_blueprint.route("/authors/add_author", methods=["get", "post"])
def add_author():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_author_form = AddAuthor()

    if request.method == 'POST':
        if add_author_form.validate_on_submit():
            new_author = Author()

            new_author.email = add_author_form.author_email.data
            new_author.address = add_author_form.author_address.data
            new_author.birthday = add_author_form.author_birthday.data
            new_author.mobileNumber = add_author_form.author_mobile_number.data

            try:
                db.session.add(new_author)
                db.session.commit()
            except:
                flash("An Exception is raised")
                add_author_form = AddAuthor()
                return render_template("/authors/add_author.html", form=add_author_form)

            return redirect("/authors")
        else:
            return render_template("authors/add_author.html", form=add_author_form)
    else:
        return render_template("authors/add_author.html", form=add_author_form)


@authors_blueprint.route("/authors/edit_author", methods=["get", "post"])
def edit_author():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_author_form = EditAuthor()

    author_id = request.args["authorID"]
    author_to_edit = session.query(Author).filter(
        Author.authorID == author_id).first()
    if request.method == "POST":
        if edit_author_form.validate_on_submit():
            author_id = edit_author_form.author_id.data
            author_to_edit = db.session.query(Author).filter(
                Author.authorID == author_id).first()

            author_to_edit.email = edit_author_form.author_email.data
            author_to_edit.address = edit_author_form.author_address.data
            author_to_edit.birthday = edit_author_form.author_birthday.data
            author_to_edit.mobileNumber = edit_author_form.author_mobile_number.data

            db.session.commit()
        return redirect("/authors")
    else:
        edit_author_form.author_id.data = author_to_edit.authorID
        edit_author_form.author_email.data = author_to_edit.email
        edit_author_form.author_address.data = author_to_edit.address
        edit_author_form.author_birthday.data = author_to_edit.birthday
        edit_author_form.author_mobile_number.data = author_to_edit.mobileNumber

        return render_template("authors/edit_author.html", form=edit_author_form)


@authors_blueprint.route("/authors/delete_author", methods=["get", "post"])
def delete_author():
    delete_author_form = DeleteAuthor()
    if delete_author_form.validate_on_submit():
        author_id = delete_author_form.authorID.data
        author_to_delete = db.session.query(Author).filter(
            Author.authorID == author_id)
        author_to_delete.delete()
        db.session.commit()
    return redirect("/authors")
