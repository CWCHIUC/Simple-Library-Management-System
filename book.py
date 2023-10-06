import json

from database import Books

books = Books()
books = books.init()

borrowed_books = []

class Book():
    def __init__(self, book_name=''):
        self.book_name = book_name
    
    def book_database(self):
        books = Books()
        books = books.init()
        
    def browse_book(self):
        book_names = []

        for key, value in books.items():
            book_names.append(key)

        for i in range(len(book_names)):
            print(book_names[i])
        
    def check_availability(self, book_name):
        status = books[f'{book_name}']['status']
        print(status)

    def print_rating(self, book_name):
        rating = books[f'{book_name}']['rating']
        print(rating)

    def check_out(self, book_name):
        status = books[f'{book_name}']['status']
        if status != "checked out":
            print(f"{book_name} has been checked out.")
            borrowed_books.append(book_name)
            # Add the 'due' key with a value of "7 days" when checking out
            books[f'{book_name}']['due'] = "7 days"
            print(f"{book_name} is due in {books[book_name]['due']}")
        else:
            print(f'{book_name} is unavailable')

    
    def check_in(self, book_name):
        if book_name in borrowed_books:
            print(borrowed_books)
            print(f"{book_name} has been checked in.")
            borrowed_books.remove(book_name)
        else:
            print("This item has not been checked out.")

    def update_status(self, book_name):
        file_path = 'json/books.json'

        with open(file_path, 'r', encoding='utf-8') as json_file:
            books = json.load(json_file)

        if books[f'{book_name}']['status'] == 'available':
            books[f'{book_name}']['status'] = 'checked out'
        elif books[f'{book_name}']['status'] == 'checked out':
            books[f'{book_name}']['status'] = 'available'

        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(books, json_file, indent=4)

    def open_book(self, book_name):
        if book_name in borrowed_books:
            book = open(f"books/{book_name}.txt", "r")
            print(book.read())
        else:
            print(f'{book_name} has not been checked out')

    def remove_due(self, book_name):
        with open('json/books.json', 'r') as file:
            data = json.load(file)

        if "key" in data[f"{book_name}"]:
            del data[f"{book_name}"]["key"]

        # Write the modified JSON data back to the file again (without "key": "value")
        with open('json/books.json', 'w') as file:
            json.dump(data, file, indent=4)

def valid_input(book_name):
    for key, value in books.items():
        if (f"{book_name}") == key:
            return True