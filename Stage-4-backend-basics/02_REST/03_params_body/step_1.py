# Step 1: Route params

method = "GET"
path = "/articles/2"

print("Client request:", method, path)

if method == "GET" and path.startswith("/articles/"):
    parts = path.split("/")
    article_id = parts[2]  # route param
    print("Server: route param =", article_id)
else:
    print("Server: no route params detected")