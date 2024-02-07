class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __repr__(self):
        return f"{self.title} by {self.author}"

# Example list of books in a library
library = [
    Book("1984", "George Orwell", "978-0451524935"),
    Book("To Kill a Mockingbird", "Harper Lee", "978-0446310789"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
]

# Processing each book in the list
for book in library:
    print(book)

# Example output:
# 1984 by George Orwell
# To Kill a Mockingbird by Harper Lee
# The Great Gatsby by F. Scott Fitzgerald
