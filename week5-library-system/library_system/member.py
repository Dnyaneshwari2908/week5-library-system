class Member:

    def __init__(self, name, member_id):

        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, isbn):

        if len(self.borrowed_books) < 5:

            self.borrowed_books.append(isbn)

            return True

        return False

    def return_book(self, isbn):

        if isbn in self.borrowed_books:

            self.borrowed_books.remove(isbn)

            return True

        return False