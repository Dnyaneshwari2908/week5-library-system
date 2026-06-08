from library_system.book import Book
from library_system.member import Member
from library_system.library import Library


def menu():

    library = Library()

    library.load_data()

    while True:

        print("\n" + "=" * 40)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("=" * 40)

        print("1. Add Book")
        print("2. Register Member")
        print("3. Search Book")
        print("4. View All Books")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            year = input("Year: ")

            book = Book(
                title,
                author,
                isbn,
                year
            )

            library.add_book(book)

            print("Book Added Successfully!")

        elif choice == "2":

            name = input("Member Name: ")
            member_id = input("Member ID: ")

            member = Member(
                name,
                member_id
            )

            library.register_member(member)

            print("Member Registered!")

        elif choice == "3":

            keyword = input("Enter title: ")

            library.search_book(keyword)

        elif choice == "4":

            for book in library.books.values():

                print(book)

        elif choice == "5":

            library.save_data()

            print("Data Saved Successfully!")

            break

        else:

            print("Invalid Choice")