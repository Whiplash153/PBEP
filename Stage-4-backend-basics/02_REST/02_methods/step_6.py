articles = [
    {"id": "1", "title": "First", "author": "A"},
    {"id": "2", "title": "Second", "author": "B"}
]

method = "GET"
path = "/articles"
body = {"title": "New", "author": "C"}

print("Client request:", method, path)

def find_article(article_id):
    return next ((a for a in articles if a["id"] == article_id), None)

if method == "GET":
    if path == "/articles":
        print("Server:", articles)

    elif path.startswith("/articles/"):
        article_id = path.split("/")[2]
        target = find_article(article_id)
        if target:
            print("Server:", target)
        else:
            print("Server: 404 Not Found")

elif method == "POST" and path == "/articles":
    new_id = str(len(articles) + 1)
    created = {"id": new_id, **body}
    articles.append(created)
    print("Server: created:", created)

elif method == "PUT" and path.startswith("/articles/"):
    article_id = path.split("/")[2]
    target = find_article(article_id)
    if target:
        updated = {"id": article_id, **body}
        articles[articles.index(target)] = updated
        print("Server: replaced:", updated)
    else:
        print("Server: 404 Not Found")

elif method == "PATCH" and path.startswith("/articles/"):
    article_id = path.split("/")[2]
    target = find_article(article_id)
    if target:
        target.update(body)
        print("Server: updated:", target)
    else:
        print("Server: 404 Not Found")

elif method == "DELETE" and path.startswith("/articles/"):
    article_id = path.split("/")[2]
    target = find_article(article_id)
    if target:
        articles.remove(target)
        print("Server: deleted", article_id)
    else:
        print("Server already deleted")

else:
    print("Server: 404 Not Found")





