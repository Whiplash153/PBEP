class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

books = [
    Book("The Hobbit", "Tolkien"),
    Book("1984", "Orwell"),
    Book("Crime and Punishment", "Dostoevsky")
]

for book in books:
    print(book)