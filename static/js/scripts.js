// Fetch all books on page load
document.addEventListener('DOMContentLoaded', function() {
    fetchBooks();
});

// Function to fetch and display books
function fetchBooks() {
    fetch('/books')
    .then(response => response.json())
    .then(data => {
        const bookList = document.getElementById('book-list');
        bookList.innerHTML = '';
        data.forEach(book => {
            const li = document.createElement('li');
            li.innerHTML = `
                ${book.title} by ${book.author}
                <button onclick="deleteBook(${book.id})">Delete</button>
            `;
            bookList.appendChild(li);
        });
    });
}

// Handle form submission for adding a new book
document.getElementById('book-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;

    fetch('/books', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title: title, author: author })
    })
    .then(response => response.json())
    .then(data => {
        fetchBooks();
        document.getElementById('title').value = '';
        document.getElementById('author').value = '';
    });
});

// Function to delete a book
function deleteBook(bookId) {
    fetch(`/books/${bookId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        fetchBooks();
    });
}
