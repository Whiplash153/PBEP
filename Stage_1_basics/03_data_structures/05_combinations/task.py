hobby = {
    "Alice": ["reading", "driving"],
    "Bob": ["PC games", "reading"],
    "Victor": ["swimming", "thinking"]
}

print("Hobbies:", hobby)

print("Alice hobbies:", hobby["Alice"])

for user in hobby:
    print(user, "Hobbies:", hobby[user])

