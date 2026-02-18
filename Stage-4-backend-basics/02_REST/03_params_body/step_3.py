# Step 3: Body handling

method = "POST"
path = "/articles"

body = {
    "title": "New Article",
    "author": "Jane",
    "year": 2024
}

print("Client request:", method, path)
print("Server received body:", body)