# Step 2: Query params

method = "GET"
path = "/articles?author=John&year=2020"

print("Client request:", method, path)

if "?" in path:
    base, query_str = path.split("?", 1)  # отделяем путь от параметров
    params = dict(param.split("=") for param in query_str.split("&"))
    print("Server: query params =", params)
else:
    print("Server: no query params detected")