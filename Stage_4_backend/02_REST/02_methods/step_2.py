method = "POST"
path = "/articles"

articles = [
    {"id": "1", "title": "Boom"},
    {"id": "2", "title": "Cool"},
]

new_article = {"title": "New post from client"}

print("Client request:", method, path)

if method == "POST" and path == "/articles":

    new_id = str(len(articles) + 1)
    created = {"id": new_id, **new_article}

    articles.append(created)

    print("Server: created article:", created)

else:
    print("Server: 404 Not Found")

