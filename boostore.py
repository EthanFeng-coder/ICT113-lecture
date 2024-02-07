# Example: List example
# Author: Umesh Poudel
# Date: 18 Sep 2022

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

class BookStore:
    def __init__(self):
        self.books = []

    def append(self, book):
        self.books.append(book)

    def getList(self):
        return self.books

    def size(self):
        return len(self.books)

    def isEmpty(self):
        return len(self.books) == 0

    def at(self, index):
        return self.books[index]

def main():
    print("\nWIN Books")
    print("-"*40)

    # Bookstore instance
    store = BookStore()

    # Creating Book objects/instances
    b1 = Book("Title 1", "Author 1", 2015)
    b2 = Book("Title 2", "Author 1", 2020)
    b3 = Book("Title 3", "Author 2", 2022)

    # Adding books to store
    store.append(b1)
    store.append(b2)
    store.append(b3)

    print("Book list is empty: ", store.isEmpty())
    print("\nBooks count:", store.size())

    # Book listing
    books = store.getList()
    print()
    print("{:20}{:20}{:20}".format("Title", "Author", "Year"))
    print("-"*60)
    for book in books:
        print("{:20}{:20}{:20}".format(book.getTitle(), book.getAuthor(), book.getYear()))
    print("-"*40)

main()
