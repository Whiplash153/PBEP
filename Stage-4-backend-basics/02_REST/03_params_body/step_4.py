# Step 4: Mixed params (route + query + body)

method = "PATCH"
path = "/articles/2?public=true&lang=en"

body = {"title": "Updated title"}

print("Client request:", method, path)

# extract route param
route_part = path.split("?")[0]
article_id = route_part.split("/")[2]

# extract query params
query_params = {}
if "?" in path:
    query_str = path.split("?")[1]
    query_params = dict(param.split("=") for param in query_str.split("&"))

print("Route param:", article_id)
print("Query params:", query_params)
print("Body:", body)