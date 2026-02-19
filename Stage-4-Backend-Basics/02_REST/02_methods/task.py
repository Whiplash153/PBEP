books = [
    {"id": "1", "title": "First", "author": "A", "year": 1998},
    {"id": "2", "title": "Second", "author": "B", "year": 2001},
    {"id": "3", "title": "Third", "author": "C", "year": 2005},
]

#Parameters
method = "GET"
path = "/books"
body = {"title": "New", "author": "D", "year": 2010}

print("Client request:", method, path)

#id_Func
def find_book(id):
    for book in books:
        if book["id"] == id:
            return book
    return None

#GET
if method == "GET":
    if path == "/books":
        print("Server:", books)

    elif path.startswith("/books/"):
        book_id = path.split("/")[2]
        target = find_book(book_id)
        if target:
            print("Server:", target)
        else:
            print("Server: 404 not found")

#POST
elif method == "POST" and path == "/books":
    new_id = str(len(books) + 1)
    created = {"id": new_id, **body}
    books.append(created)
    print("Server: created:", created)

#PUT
elif method == "PUT" and path.startswith("/books/"):
    book_id = path.split("/")[2]
    target = find_book(book_id)
    if target:
        updated = {"id": book_id, **body}
        books[books.index(target)] = updated
        print("Server: replaced:", updated)
    else:
        print("Server: 404 Not Found")

#PATCH
elif method == "PATCH" and path.startswith("/books/"):
    book_id = path.split("/")[2]
    target = find_book(book_id)
    if target:
        target.update(body)
        print("Server: updated:", target)
    else:
        print("Server: 404 not found")

#DELETE
elif method == "DELETE" and path.startswith("/books/"):
    book_id = path.split("/")[2]
    target = find_book(book_id)
    if target:
        books.remove(target)
        print("Server: deleted", book_id)
    else:
        print("Server already deleted")

else:
    print("Server: 404 Not Found")


