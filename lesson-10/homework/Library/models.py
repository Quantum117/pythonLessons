
class Book:
    def __init__(self, name, author, is_borrowed=False):
        self.name = name
        self.author = author
        self.is_borrowed: bool = is_borrowed

class Member:
    def __init__(self, name ):
        self.name = name
        self.borrowed_books:list[Book] = []
