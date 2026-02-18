articles = [
    {"id": "1", "title": "A"},
    {"id": "2", "title": "B"}
]

print("Initial state:", articles)

method = "PUT"
path = "/articles/2"
incoming = {"title": "New"}

if method == "PUT" and path.startswith("/articles/"):
    article_id = path.split("/")[2]
    updated = {"id": article_id, **incoming}
    print("PUT applied:", updated)

if method == "PUT" and path.startswith("/articles/"):
    article_id = path.split("/")[2]
    updated = {"id": article_id, **incoming}
    print("PUT applied again:", updated)

method = "POST"
path = "/articles"
incoming = {"title": "New post"}

if method == "POST" and path == "/articles":
    articles.append({"id": "3", **incoming})
    print("POST applied:", articles[-1])

if method == "POST" and path == "/articles":
    articles.append({"id": "4", **incoming})
    print("POST applied again:", articles[-1])