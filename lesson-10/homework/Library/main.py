from Library import Library
from json_handler import JSONHandler


def main():
    members = JSONHandler("members.json")
    books = JSONHandler("books.json")
    borrowed_books = JSONHandler("borrowed_books.json")
    library = Library(members.load(), books.load(), borrowed_books.load())

    print("Welcome to the Library!")
    print("0. Add a new member")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. View borrowed books")
    print("6. Exit")

    while True:
        try:
            input_choice = int(input("Enter your choice: "))
            if input_choice == 0:
                # Add a new book
                new_member = library.make_member_object()
                if new_member :
                    library.add_member(new_member)

                    print(f"{new_member.name} - added successfully!")
            if input_choice == 1:
                # Add a new book
                book = library.make_book_object()
                if book is not None:
                    library.add_book(book)
                    print("Book added successfully!")

            elif input_choice == 2:
                # View all books
                if len(library.books) == 0:
                    print("No books available in the library.")
                else:
                    print("\nLibrary Books:")
                    for book in library.books:
                        print(f" - {book.name} by {book.author}")

            elif input_choice == 3:
                # Borrow a book
                member_name = input("Enter your name: ").strip()
                book_name = input("Enter the name of the book to borrow: ").strip()

                try:
                    # Find the member and book
                    member = next(filter(lambda m: m.name == member_name, library.members), None)
                    book = next(filter(lambda b: b.name == book_name, library.books), None)

                    if member and book:
                        message = library.borrow(member, book)
                        print(message)
                    else:
                        print("Member or book not found.")

                except Exception as e:
                    print(f"Error: {e}")

            elif input_choice == 4:
                # Return a book
                member_name = input("Enter your name: ").strip()
                book_name = input("Enter the name of the book to return: ").strip()

                try:
                    # Find the member and book
                    member = next(filter(lambda m: m.name == member_name, library.members), None)
                    book = next(filter(lambda b: b.name == book_name, library.borrowed_books), None)

                    if member and book:
                        library.return_book(member, book)
                    else:
                        print("Member or book not found or the book was not borrowed.")

                except Exception as e:
                    print(f"Error: {e}")

            elif input_choice == 5:
                # View borrowed books
                if len(library.borrowed_books) == 0:
                    print("No books currently borrowed.")
                else:
                    print("\nBorrowed Books:")
                    for book in library.borrowed_books:
                        print(f" - {book.name} by {book.author}")

            elif input_choice == 6:
                # Exit
                print("Exiting the system. Goodbye!")
                library.save(members, books, borrowed_books)
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()