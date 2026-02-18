class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.title < other.title
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Book):
            return self.title > other.title
        return NotImplemented