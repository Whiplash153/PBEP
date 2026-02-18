method = "PATCH"
path = "/users/10/posts/5?notify=true&draft=false"

body = {"title": "New", "tags": ["x"]}

print("Client request:", method, path)

route_part = path.split("?")[0]
route_params = route_part.split("/")[2]

query_params = {}
if "?" in path:
    query_str = path.split("?")[1]
    query_params = dict(param.split("=") for param in query_str.split("&"))

print("Route param:", route_part)
print("Query params:", query_params)
print("Body:", body)

