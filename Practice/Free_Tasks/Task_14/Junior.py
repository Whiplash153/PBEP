class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return self.title + " - " + self.author + ", " + str(self.pages) + " pages"

    def __lt__(self, other):
        return self.pages < other.pages


book1 = Book("1984", "George Orwell", 328)
book2 = Book("Brave New World", "Aldous Huxley", 288)

print(book1)
print(book1 < book2)