class Library:

    def __init__(self):
        self.noBook = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBook = len(self.books)

    def showInfo(self):
        print(f"The Library Has {self.noBook} Books. \nThe Books Are")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBook("Programming In C")
l1.addBook("Programming In Javascript")
l1.addBook("Programming In python")
l1.showInfo()
