import sqlalchemy
from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect
from forms.publisher.add_form import AddPublisher
from forms.publisher.delete_form import DeletePublisher
from forms.publisher.edit_form import EditPublisher
from model.models import db, Publisher

publishers_blueprint = Blueprint('publishers_blueprint', __name__)


@publishers_blueprint.route("/publishers", methods=["get", "post"])
def publishers():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    page = request.args.get('page', 1, type=int)
    publisher_list = session.query(Publisher).order_by(Publisher.publisherID).paginate(
        page, 10, error_out=False)

    return render_template("/publishers/publisher.html", publishers=publisher_list)


@publishers_blueprint.route("/publishers/add_publisher", methods=["get", "post"])
def add_publisher():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_publisher_form = AddPublisher()

    if request.method == 'POST':
        if add_publisher_form.validate_on_submit():
            new_publisher = Publisher()

            new_publisher.name = add_publisher_form.publisher_name.data
            new_publisher.address = add_publisher_form.publisher_address.data
            new_publisher.amountOfBooks = add_publisher_form.publisher_amount_of_books.data
            new_publisher.founderDate = add_publisher_form.publisher_founder_date.data

            try:
                db.session.add(new_publisher)
                db.session.commit()
            except:
                flash("An Exception is raised")
                add_publisher_form = AddPublisher()
                return render_template("/publishers/add_publisher.html", form=add_publisher_form)

            return redirect("/publishers")
        else:
            return render_template("publishers/add_publisher.html", form=add_publisher_form)
    else:
        return render_template("publishers/add_publisher.html", form=add_publisher_form)


@publishers_blueprint.route("/publishers/edit_publisher", methods=["get", "post"])
def edit_publisher():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_publisher_form = EditPublisher()

    publisher_id = request.args["publisherID"]

    publisher_to_edit = session.query(Publisher).filter(
        Publisher.publisherID == publisher_id).first()

    if request.method == "POST":
        if edit_publisher_form.validate_on_submit():
            publisher_id = edit_publisher_form.publisher_id.data
            publisher_to_edit = db.session.query(Publisher).filter(
                Publisher.publisherID == publisher_id).first()

            publisher_to_edit.name = edit_publisher_form.publisher_name.data
            publisher_to_edit.address = edit_publisher_form.publisher_address.data
            publisher_to_edit.amountOfBooks = edit_publisher_form.publisher_amount_of_books.data
            publisher_to_edit.founderDate = edit_publisher_form.publisher_founder_date.data

            db.session.commit()
        return redirect("/publishers")
    else:
        edit_publisher_form.publisher_id.data = publisher_to_edit.publisherID
        edit_publisher_form.publisher_name.data = publisher_to_edit.name
        edit_publisher_form.publisher_address.data = publisher_to_edit.address
        edit_publisher_form.publisher_amount_of_books.data = publisher_to_edit.amountOfBooks
        edit_publisher_form.publisher_founder_date.data = publisher_to_edit.founderDate

        return render_template("publishers/edit_publisher.html", form=edit_publisher_form)


@publishers_blueprint.route("/publishers/delete_publisher", methods=["get", "post"])
def delete_publisher():
    delete_publisher_form = DeletePublisher()
    if delete_publisher_form.validate_on_submit():
        publisher_id = delete_publisher_form.publisherID.data
        publisher_to_delete = db.session.query(Publisher).filter(
            Publisher.publisherID == publisher_id)
        publisher_to_delete.delete()

        db.session.commit()
    return redirect("/publishers")
