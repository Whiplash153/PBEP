print("=== POST ===")
method = "POST"
path = "/users"
body = '{"name": "Misha"}'
print(method, path, body)

print("=== PUT ===")
method = "PUT"
path = "/users/10"
body = '{"name": "Misha", "age": 25}'
print(method, path, body)

print("=== PATCH ===")
method = "PATCH"
path = "/users/10"
body = '{"age": 26}'
print(method, path, body)