import streamlit as st

# In-memory "database"
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

# Title
st.title("Book Collection")

# Display Books
st.header("All Books")
if st.button("Fetch Books"):
    for book in books:
        st.write(f"{book['id']}: {book['title']} by {book['author']}")

# Add a Book
st.header("Add a New Book")
new_title = st.text_input("Title")
new_author = st.text_input("Author")

if st.button("Add Book"):
    if new_title and new_author:
        new_id = max(book["id"] for book in books) + 1
        books.append({"id": new_id, "title": new_title, "author": new_author})
        st.write("Book added successfully!")
    else:
        st.write("Please enter both title and author.")

# Delete a Book
st.header("Delete a Book")
book_id_to_delete = st.number_input("Enter Book ID to delete", min_value=1, step=1)

if st.button("Delete Book"):
    global books
    books = [book for book in books if book["id"] != book_id_to_delete]
    st.write(f"Book with ID {book_id_to_delete} deleted!")
