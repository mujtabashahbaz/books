from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample data (in-memory database)
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

# Serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify(book)

# Create a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if not new_book or not new_book.get('title') or not new_book.get('author'):
        return jsonify({'message': 'Invalid book data'}), 400
    new_book['id'] = max(book['id'] for book in books) + 1 if books else 1
    books.append(new_book)
    return jsonify(new_book), 201

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
