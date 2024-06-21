class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        
    def borrow(self):
        if(self.available is False):
            return f'This book -> {self.title} is already borrowed.'
        else:
            self.available = False
            return f'This book -> {self.title} has been borrowed.'

    def return_book(self):
        self.available = True
        return f'This book -> {self.title} is now returned and available.'
    
    def __str__(self):
        return f'Book: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}' #trying a different syntax
        
class Library:
    def __init__(self) -> None: #trying a different syntax
        self.books = []

    def add_book(self, book):
        book.library = self
        self.books.append(book)
        return f'Book "{book.title}" added to the library.'

    def remove_book(self, isbn):
        for book in self.books:
            if (book.isbn == isbn):
                self.books.remove(book)
                return f'This book has been removed.'
        return "Book was not found."

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return "Book was not found."
    
    def list_available_books(self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book)
        if available_books:
            return '\n'.join(str(book) for book in available_books)
        else:
            return 'No books available.'
        

library1 = Library()
library2 = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
book2 = Book("1984", "George Orwell", "2345678901")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "3456789012")

print(library1.add_book(book1))
print(library2.add_book(book2))
print(library1.add_book(book3))

# print(library1.list_available_books())
# print(library2.list_available_books())
# print(book1.borrow())
# print(library1.list_available_books())
# print(library2.list_available_books())

print(library1.remove_book("3456789012"))
print(library1.list_available_books())
print(library2.list_available_books())
