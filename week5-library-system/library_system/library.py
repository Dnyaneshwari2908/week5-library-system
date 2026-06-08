import json

from library_system.book import Book
from library_system.member import Member


class Library:

    def __init__(self):

        self.books = {}
        self.members = {}

    def add_book(self, book):

        self.books[book.isbn] = book

    def register_member(self, member):

        self.members[member.member_id] = member

    def search_book(self, keyword):

        for isbn, book in self.books.items():

            if keyword.lower() in book.title.lower():

                print(book)

    def save_data(self):

        books_data = {}

        for isbn, book in self.books.items():

            books_data[isbn] = {
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "available": book.available
            }

        with open("data/books.json", "w") as file:

            json.dump(books_data, file, indent=4)

    def load_data(self):

        try:

            with open("data/books.json", "r") as file:

                data = json.load(file)

                for isbn, info in data.items():

                    book = Book(
                        info["title"],
                        info["author"],
                        isbn,
                        info["year"]
                    )

                    book.available = info["available"]

                    self.books[isbn] = book

        except FileNotFoundError:

            pass