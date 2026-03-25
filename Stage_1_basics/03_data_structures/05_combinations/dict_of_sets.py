roles = {
    "Alice": {"admin", "editor"},
    "Bob": {"viewer"},
    "Charlie": {"editor", "viewer"}
}

print("All roles:", roles)

print("Alice roles:", roles["Alice"])

print("Is Bob an editor?:", "editor" in roles["Bob"])