from models import Book

class BookNotFoundException(Exception):
    def __init__(self,book:Book,  message = "The book is not in the library."):
        self.book = book
        self.message = message
        super().__init__(message)
    def __str__(self):
        return f"{self.book.name} --> {self.message}"

class BookAlreadyBorrowedException(Exception):
    def __init__(self, book: Book, message="The book is borrowed from the library."):
        self.book = book
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.book.name} --> {self.message}"

class MemberLimitExceededException(Exception):
    def __init__(self,  message="Allowed to borrow up to  3 books."):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"--> {self.message}"
