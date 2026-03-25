method = "GET"
path = "/users/42"
query_params = {"active": True}

print("Client request:")
print(method, path, query_params)

if method == "GET" and path.startswith("/users/"):
    user_id = path.split("/")[2]
    print("Server:", f"Return user with id = {user_id}")