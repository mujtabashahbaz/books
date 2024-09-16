import requests

BASE_URL = 'http://127.0.0.1:5000/books'

def get_books():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return response.text

def get_book(book_id):
    response = requests.get(f'{BASE_URL}/{book_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return response.text

def add_book(title, author):
    response = requests.post(BASE_URL, json={'title': title, 'author': author})
    if response.status_code == 201:
        return response.json()
    else:
        return response.text

def update_book(book_id, title=None, author=None):
    data = {}
    if title:
        data['title'] = title
    if author:
        data['author'] = author
    response = requests.put(f'{BASE_URL}/{book_id}', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return response.text

def delete_book(book_id):
    response = requests.delete(f'{BASE_URL}/{book_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return response.text

if __name__ == '__main__':
    print('Getting all books:')
    print(get_books())

    print('\nAdding a new book:')
    print(add_book('The Great Gatsby', 'F. Scott Fitzgerald'))

    print('\nGetting all books:')
    print(get_books())

    print('\nGetting a specific book (ID: 1):')
    print(get_book(1))

    print('\nUpdating a book (ID: 1):')
    print(update_book(1, author='George Orwell Updated'))

    print('\nGetting all books:')
    print(get_books())

    print('\nDeleting a book (ID: 1):')
    print(delete_book(1))

    print('\nGetting all books:')
    print(get_books())
