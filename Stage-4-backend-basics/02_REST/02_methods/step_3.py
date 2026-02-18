method = "PUT"
path = "/articles/2"

articles = [
    {"id": "1", "title": "Boom", "author": "A"},
    {"id": "2", "title": "Old title", "author": "B"}
]

incoming = {"title": "New title"}

print("Client request:", method, path)

if path.startswith("/articles/"):
    article_id = path.split("/")[2]

    target = next((article for article in articles if article["id"] == article_id), None)

    if not target:
        print("Server: 404 Not Found")
    else:
        if method == "PUT":
            updated = {"id": article_id, **incoming}
            print("Server: replaced resource:", updated)

        elif method == "PATCH":
            target.update(incoming)
            print("Server: updated resource:", target)

else:
    print("Server: 404 Not Found")





