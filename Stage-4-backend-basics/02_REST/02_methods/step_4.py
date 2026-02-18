method = "DELETE"
path = "/articles/2"

articles = [
    {"id": "1", "title": "Boom"},
    {"id": "2", "title": "Old title"}
]

print("Client request:", method, path)

if method == "DELETE" and path.startswith("/articles/"):
    article_id = path.split("/")[2]

    target = next((article for article in articles if article["id"] == article_id), None)

    if not target:
        print("Server: already deleted")
    else:
        articles.remove(target)
        print("Server: deleted resource:", target)
else:
    print("Server: 404 Not Found")