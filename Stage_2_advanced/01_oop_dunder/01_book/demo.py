from book import Book

b1 = Book("1984", "Orwell")
b2 = Book("War", "Tolstoy")
b3 = Book("1984", "Orwell")

print(b1 == b2)
print(b1 == b3)

print(b1 < b2)
print(b2 < b1)

print(b1 > b2)

print(b1)
print(b2)

print(repr(b1))