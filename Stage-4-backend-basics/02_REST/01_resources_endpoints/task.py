articles = [
    {"id": "1", "title": "Boom", "author": "Andrew", "views": "1999"},
    {"id": "2", "title": "Really", "author": "Mack", "views": "100"},
    {"id": "3", "title": "Wow", "author": "Niut", "views": "555"},
]

collection = "/articles"
element = "/articles/1"
filtration = "/articles?author=Mack"

print("Collection:", collection)
print("Element:", element)
print("Filtration:", filtration)

method = "GET"
path = "/articles/1"

if method == "GET" and path == "/articles":
    print("Return all articles")

elif method == "GET" and path.startswith("/articles/"):
    article_id = path.split("/")[2]
    print(f"Return article {article_id}")
