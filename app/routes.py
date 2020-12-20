from flask import (request, render_template, redirect,
                   url_for, jsonify, abort, make_response)
from app import app, models, forms, db
from app.Library import books



@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = forms.BooksForm()
    reads = models.Book.query.all()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            books.add_book(form.data)
        else:
            print(form.errors)
        return redirect(url_for("books_list"))

    return render_template(
        "form.html",
        form=form,
        books=reads,
        error=error
    )


@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id)
    data = {
        'title': book.title,
        'author': ", ".join([author.name for author in book.authors]),
        'available': book.borrowed
    }
    form = forms.BooksForm(data=data)
    if request.method == "POST":
        if form.validate_on_submit():
            books.change(book_id, form.data)
        else:
            print(form.errors)
        return redirect(url_for("books_list"))
    return render_template(
        "books_details.html",
        form=form,
        book_id=book_id
    )


@app.route("/delete/<int:book_id>/", methods=["GET"])
def delete_book(book_id):
    book = books.delete(book_id)
    return redirect(url_for("books_list"))


@app.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify({'error': 'Not found', 'status_code': 404}), 404
    )


@app.errorhandler(400)
def bad_request(error):
    return make_response(
        jsonify({'error': 'Bad request', 'status_code': 400}), 400
    )
