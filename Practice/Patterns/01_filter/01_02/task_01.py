users = [
    {"name": "bob", "age": 17},
    {"name": "alice", "age": 22},
    {"name": "mike", "age": 19},
    {"name": "kate", "age": 15},
]

filtered = []
for user in users:
    if user["age"] >= 18:
        filtered.append(user)

result = []
for user in filtered:
    name_upper = user["name"].upper()
    result.append(name_upper)

print(result)