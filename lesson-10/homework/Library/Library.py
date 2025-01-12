from CustomExceptions import BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException
from models import Book, Member

class Library:
    def __init__(self,books=None,members=None,borrowed_books=None):
        self.books = books
        self.members = members
        self.borrowed_books = borrowed_books

    def borrow (self, member, book):
        try :
            if member.borrowed_books >= 3:
                raise MemberLimitExceededException()
            if book.is_borrowed:
                raise BookAlreadyBorrowedException(book)
            if book in self.books :
                self.books.remove(book)
                self.borrowed_books.append(book)
                member.borrowed_books.append(book)
                return f"{member.name} has borrowed {book.name}."

            else:
                raise BookNotFoundException(book)
        except BookNotFoundException as e:
            print(e)
        except MemberLimitExceededException as e:
            print(e)
        except BookAlreadyBorrowedException as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

    def return_book (self, member, book):
        """Return a book to the library."""
        try:
            # Remove the book from borrowed_books and add it back to the library
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
                self.books.append(book)
                print(f"{member.name} has returned {book.name}.")
            else:
                # Raise the exception when the book is not found in borrowed_books
                raise BookNotFoundException(book, "The book has not been borrowed ")
        # Catch the exception and display the appropriate error message
        except BookNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_book(self, book):
        self.books.append(book)
    def add_member(self, member):
        self.members.append(member)

    def save(self,books, members,borrowed_books):
        """Save tasks using a specific file format handler."""
        members.save(self.members)
        books.save(self.books)
        borrowed_books.save(self.borrowed_books)
        print(" saved successfully.")

    @staticmethod
    def make_member_object():
        """Create a Member object from user input."""
        try:
            member_name = input("Enter member name: ")
            if member_name.strip() == "":
                raise ValueError("Member name cannot be empty.")
            return Member(member_name)

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def make_book_object():
        """Create a Book object from user input."""
        try:
            book_name = input("Enter book name: ")
            if book_name.strip() == "":
                raise ValueError("Book name cannot be empty.")

            book_author = input("Enter book author: ")
            if book_author.strip() == "":
                raise ValueError("Book author cannot be empty.")
            return Book(book_name, book_author)

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
