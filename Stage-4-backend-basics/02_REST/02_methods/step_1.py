method = "GET"
path = "/articles/2"

articles = [
    {"id": "1", "title": "Boom"},
    {"id": "2", "title": "Cool"},
    {"id": "3", "title": "Wow"}
]

print("Client request:", method, path)

if method == "GET" and path == "/articles":
    print("Server: return all articles")

elif method == "GET" and path.startswith("/articles/"):
    article_id = path.split("/")[2]
    print(f"Server: return article {article_id}")

else:
    print("Server: 404 Not Found")