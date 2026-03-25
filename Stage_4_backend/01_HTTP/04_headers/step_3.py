headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer abc123"
}

content_type = headers.get("Content-Type")
if content_type == "application/json":
    print("Client sent JSON")

auth = headers.get("Authorization")
if auth:
    print("Authorization token received")

accept = headers.get("Accept")
print(f"Client expects: {accept}")

response_headers = {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
}

print("Server response headers:", response_headers)