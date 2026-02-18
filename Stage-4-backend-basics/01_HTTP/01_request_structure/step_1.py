print("=== Start line ===")

raw_request = "GET /products?id=10 HTTP/1.1"

method, path, version = raw_request.split(" ")

print("Method:", method)
print("Path:", path)
print("Version:", version)