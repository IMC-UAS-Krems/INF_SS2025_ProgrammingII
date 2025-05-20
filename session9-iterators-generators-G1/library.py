class Book():
    def __init__(self, name, authors):
        self.name = name
        self.authors = authors
        # self.index = -1

    def __repr__(self):
        return self.name

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     self.index += 1
    #     if self.index < len(self.authors):
    #         return self.authors[self.index]
    #     else:
    #         raise StopIteration()

class BookIterator():
    def __init__(self, books):
        self.books = books
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index < len (self.books):
            return self.books[self.index]
        else:
            raise StopIteration()


class Library():
    def __init__(self):
        self.__books = []

    def addBook (self, book):
        self.__books.append((book))

    def __iter__(self):
        return BookIterator(self.__books)


library = Library()
library.addBook(Book("Huckleberry Finn", ["Mark Twain"]))
library.addBook(Book("Tom Sawyer", ["Mark Twain"]))
library.addBook(Book("Animal Farm", ["Gerorge Orweil"]))
library.addBook(Book("Lord of the flies", ["William Golding"]))

for book in library:
    print (book)