print("\n=== POST ===")

method = "POST"
path = "/cars"
version = "HTTP/1.1"
body = '{"car": "Toyota"}'

print(f"{method} {path} {version} \n\n{body}")

print("\n=== PATCH ===")

method = "PATCH"
path = "/cars/1"
version = "HTTP/1.1"
body = '{"car": "Mazda"}'

print(f"{method} {path} {version} \n\n{body}")

print("\n=== GET ===")

method = "GET"
path = "/cars/1"
version = "HTTP/1.1"

print(f"{method} {path} {version}")