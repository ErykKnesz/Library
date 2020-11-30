from flask import (request, render_template, redirect,
                   url_for, jsonify, abort, make_response)
from forms import BooksForm
from models import Books


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = BooksForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            Books.create(form.data)
        return redirect(url_for("books_list"))

    return render_template(
        "form.html",
        form=form,
        books=Books.all(),
        error=error
    )


@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = Books.get(book_id)
    form = BooksForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            Books.update(book_id, form.data)
        return redirect(url_for("books_list"))
    return render_template(
        "books_details.html",
        form=form,
        book_id=book_id
    )


@app.route("/api/v1/books/", methods=["POST"])
def create_book():
    if not request.json:
        abort(400)
    book = {
            'date': request.json['date'],
            'item': request.json['item'],
            'quantity': request.json.get('quantity'),
            'book': request.json.get('book')
    }
    Books.create(book)
    return jsonify({'book': book}), 201


@app.route("/api/v1/books/", methods=["GET"])
def books_list_api_v1():
    return jsonify(Books.all())


@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Books.get(book_id)
    if not book:
        abort(404)
    return jsonify({"book": book})


@app.route("/api/v1/books/<int:book_id>", methods=['DELETE'])
def delete_books(book_id):
    result = Books.delete(book_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


@app.route("/api/v1/books/<int:book_id>", methods=["PUT"])
def update_books(book_id):
    book = Books.get(book_id)
    if not book:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'date' in data and not isinstance(data.get('date'), str),
        'item' in data and not isinstance(data.get('item'), str),
        'quantity' in data and not isinstance(data.get('quantity'), int),
        'book' in data and not isinstance(data.get('book'), float)
    ]):
        abort(400)
    book = {
        'id': book_id,
        'date': data.get('date', book['date']),
        'item': data.get('item', book['item']),
        'quantity': data.get('quantity', book['quantity']),
        'book': data.get('book', book['book'])
    }
    Books.update(book_id, book)
    return jsonify({'book': book})


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

